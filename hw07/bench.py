

class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.player_names = []

    def send_to_bench(self, player_name):
        self.player_names.insert(0, player_name)

    def get_from_bench(self):
        if len(self.player_names) == 0:
            return "The bench is empty"
        else:
            return self.player_names.pop()

    def show_bench(self):
        for player in self.player_names:
            print(player)
