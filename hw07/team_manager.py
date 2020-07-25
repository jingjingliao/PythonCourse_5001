from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    # Here's where we create objects for the team and the bench. These
    # objects will be able to call the methods we've defined in their
    # respective classes. When the constructor functions are called here,
    # the classes' __init__() method is called with these values
    # passed to it. In both of these cases no arguments are passed, here.
    # However, the `self` argument is always implicitly passed with any
    # method call.
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return  # this return statement exits main, ending the session.
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


# set the name of the team and check whether the input name is valid. It should
# contain space and alphanumeric characters.
def do_set_team_name(team):
    name = input("What do you want to name the team?\n").title()
    while name.replace(" ", "").isalnum() is False:
        print("All characters in the team name should be alphanumeric")
        name = input("What do you want to name the team?\n").title()
    team.set_team_name(name)


# displays the roster
def do_show_team_roster(team):
    team.team_roster()


# check whether the position has already filled. Check whether the input
# position is valid, making it all lowercase
def do_check_position_filled(team):
    dodgeball_position = ['catcher', 'corner', 'sniper', 'thrower']
    position = input("What position are you checking for?\n").lower()
    while position not in dodgeball_position:
        print("Your check position is invalid,"
              " please input 'catcher' or 'corner' or 'sniper' or 'thrower'")
    is_position = team.is_position_filled(position)
    if is_position:
        print("Yes, the {} position is filled".format(position))
    else:
        print("No, the {} position is not filled".format(position))


# add players to the team and check the validity of their name, number, and
# position
# player_name: contains alphabets and space
# player_number: contains numbers only
# player_position: should be one of position in dodgeball_position list
def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n").title()
    while player_name.replace(" ", "").isalpha() is False:
        print("All characters in the name should be alphabets")
        player_name = input("What's the player's name?\n").title()

    player_number = input("What's " + player_name + "'s number?\n")
    while player_number.isdigit() is False:
        print("All characters in the player_number should be numbers")
        player_number = input("What's " + player_name + "'s number?\n")

    player_position = input("What's " + player_name + "'s position?\n").lower()
    dodgeball_position = ['catcher', 'corner', 'sniper', 'thrower']
    while player_position not in dodgeball_position:
        print("Your input position is invalid,"
              " please input 'catcher' or 'corner' or 'sniper' or 'thrower'",
              "as a position")
        player_position = input("What's "
                                + player_name + "'s position?\n").lower()

    team.add_player(player_name, player_number, player_position)
    print("Added", player_name, "to", team.name)


# send player to the bench
def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    for player in team.players:
        if name == player.player_name:
            bench.send_to_bench(name)
            break
    else:
        print(name, "isn't on the team.")


# get player from the bench, Whoever has been resting longest on the bench
# will always be the first player returned from the bench
def do_get_player_from_bench(bench):
    if len(bench.player_names) == 0:
        print("The bench is empty")
    else:
        print("Got {} from bench".format(bench.get_from_bench()))


# show the players on the bench
def do_show_bench(bench):
    print("The bench currently includes:")
    bench.show_bench()


# remove the player from the team, if the player is on bench, you cannot
# remove the player. If the player is not on the team, you can get a message
# otherwise, the player can be removed from the team
def do_cut_player(team, bench):
    cut_player = input("Who do you want to cut?\n")
    if cut_player in bench.player_names:
        print("You cannot cut a benched player")
    else:
        deleted = team.cut_player(cut_player)
        if deleted is False:
            print(cut_player, "isn't on the team.")


def do_not_understand():
    print("I didn't understand that command")


main()
