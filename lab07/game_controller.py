from pair_of_dice import PairOfDice


class GameController:
    def __init__(self):
        """creat a PairOfDice() object, initialize the point and score value"""
        self.pair = PairOfDice()
        self.point = None
        self.origin_point = None

    def start_play(self):
        """Start to play the game, roll the dice and get current value"""
        input("Please enter to roll the dice...\n")
        self.pair.roll_dice()
        self.point = self.pair.current_value()

    def show_result(self):
        """get the result based on the rules"""
        WIN_POINTS = [7, 11]
        LOSE_POINTS = [2, 3, 12]
        if self.point in LOSE_POINTS:
            print("You rolled {}. You lose.".format(self.point))
        elif self.point in WIN_POINTS:
            print("You rolled {}. You win.".format(self.point))
        else:
            print("You point is {}".format(self.point))
            self.origin_point = self.point
            self.continue_game()

    def continue_game(self):
        """didn't get the result, continue to play,
        compare the point with the origin_point"""
        LOSE_POINT = 7
        self.start_play()
        while self.point != self.origin_point and self.point != LOSE_POINT:
            print("You rolled {}.".format(self.point))
            self.start_play()
        else:
            if self.point == self.origin_point:
                print("You rolled {}. You win.".format(self.point))
            else:
                print("You rolled {}. You lose.".format(self.point))
