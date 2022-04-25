import constants
import copy

""" TODO
[X] Create app.py
[X] Proper use of Dunder Main
[X] Import from constants.py the players' data to be used within your program.
[ ] Create a clean_data function
[ ] Create a balance_teams function
[ ] Console readability
[ ] Include additional stats for a given displayed team
[ ] Quit Menu Option
"""
# 1) read the existing player data from the PLAYERS constants provided in constants.py
TEAMS = constants.TEAMS
PLAYERS = constants.PLAYERS

# 2) clean the player data without changing the original data
my_teams = copy.deepcopy(TEAMS)
my_players = copy.deepcopy(PLAYERS)


def main():

    # Create a clean_data function
    def clean_data(PLAYERS):
        #  2) clean the player data without changing the original data
        #    Follow this tut: https://teamtreehouse.com/library/overwriting-data-in-python
        #    Height: This should be saved as an integer
        #    Experience: This should be saved as a boolean value (True or False)
        #  3) save it to a new collection
        #  4) clean guardian data
        #    There can be more than one guardian, indicated by the " and " between their names.
        pass

    def balance_teams():
        """ Make sure the teams have the same number of total players on them when your team balancing function has finished."""

        # To find out how many players should be on each team, divide the length of players by the number of teams. Ex:
        # num_players_team = len(PLAYERS) / len(TEAMS)
        # balance the teams so that each team has the same number of experienced vs. inexperienced players.
        #    If this is done correctly each team stats should display the same number count for experienced total and inexperienced total #    as   well as the same total number of players on the team.

        pass

    def results():
        # number of inexperienced players on that team
        # number of experienced players on that team
        # the average height of the team
        # the guardians of all the players on that team (as a comma-separated string)
        #   You can calculate the average height for a given team by keeping a running sum total
        #   of each players height on the team and dividing that total by the total number of players on that team.
        pass


if __name__ == "__main__":
    main()
