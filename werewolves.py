class Player:
    """
    """

    def __init__(self, user_id):
        self._user_id = user_id
        self._alive = True

    def vote(self, player):
        pass


class Game:
    """
    """

    def __init__(self, host, channel):
        self._players = [host]
        self._host = host
        self._channel = channel
        self._day = True

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
        return [p.user_id for p in self.players]

    @property
    def players(self):
        return self._players

    @property
    def alive_players(self):
        return [p for p in self.players if p.alive]

    def end_game(self):
        self = None

    async def announce(self, msg):
        """
        """
        await self._channel.send(msg)


    def add_player(self, user):
        user_id = user.id
        if user_id in self.user_ids:
            self.message("Can't join the same game twice!")
        else:
            self._players.append(user)

    async def command(self, player, command):
        commands = []
        if command not in commands:
            await self.announce('Unknown command')
        else:
            pass
