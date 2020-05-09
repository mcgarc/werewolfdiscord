ROLES = {
        0: Villager,
        1: Werewolf
        }

class Role:
    """
    """

    def __str__(self):
        raise NotImplemented

    def day_action(self):
        raise NotImplemented


class Villager(Role):

    def __str__(self):
        return 'Villager'

    def day_action(self):
        pass


class Werewolf(Role):

    def __str__(self):
        return 'Werewolf'


class Player:
    """
    """

    def __init__(self, user):
        self._user = user
        self._alive = True
        self._role = 0

    @property
    def str_role(self):
        return str(ROLES[self._role])

class Game:
    """
    """

    def __init__(self, host, channel):
        host_id = host.id
        self._players = {host_id: Player(host)}
        self._host_id = host_id
        self._channel = channel
        self._day = True
        self._started = False
        self._command_dispatcher = {
                'join': self.join,
                'reset': self.reset,
                'remind': self.remind,
                }

    @property
    def host(self):
        return self._players[self._host_id]

    @property
    def channel(self):
        return self._channel

    @property
    def day(self):
        return self._day

    @property
    def time(self):
        if self._day:
            return 'day'
        else:
            return 'night'

    @property
    def user_ids(self):
        return self._players.keys()

    @property
    def players(self):
        return self._players

    @property
    def alive_players(self):
        return [p for p in self.players if p.alive]

    def get_player(self, user):
        return self._players[user.id]

    def end_game(self):
        self = None

    async def announce(self, msg):
        """
        """
        await self._channel.send(msg)

    async def direct_message(self, user, msg):
        """
        """
        await user.send(msg)

    async def add_player(self, user):
        user_id = user.id
        if user_id in self.user_ids:
            await self.announce(f'{user.mention}, you can\'t join twice!')
        else:
            self._players[user_id] = Player(user)
            await self.announce(f'{user.mention} has joined the game!')

    async def command(self, user, command):
        command = command.split(' ')
        method = command[0]
        args = command[1:]
        print(method, args)
        if method not in self._command_dispatcher.keys():
            await self.announce('Unknown command')
        else:
            method = self._command_dispatcher[method]
            await method(user, *args)
        return 

    # User commands

    async def join(self, user):
        await self.add_player(user)

    async def reset(self, user):
        await self.announce(f'{user.mention} has reset the game')
        self.__init__(self.host, self.channel)

    async def remind(self, user):
        role = self.get_player(user).str_role
        msg = f'You are a {role}'
        await self.direct_message(user, msg)

#    async def players(self, user):
#        await se
