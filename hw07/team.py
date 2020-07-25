from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        self.name = name

    def team_roster(self):
        print("The lineup for {} is:".format(self.name))
        if len(self.players) == 0:
            print("The team currently has no players")
        else:
            for each_player in self.players:
                print(each_player.player_number
                      + " " * (9 - len(each_player.player_number))
                      + each_player.player_name
                      + " " * (16 - len(each_player.player_name))
                      + each_player.player_position)

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        for i in range(len(self.players)):
            if self.players[i].player_name == player_name:
                self.players.pop(i)
                return True
        return False

    def is_position_filled(self, position):
        for player in self.players:
            if position == player.player_position:
                return True
        return False
