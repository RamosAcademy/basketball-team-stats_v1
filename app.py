import constants
import copy
import random

""" TODO
[X] Create app.py
[X] Proper use of Dunder Main
[X] Import from constants.py the players' data to be used within your program.
[X] Create a clean_data function
[ ] Create a balance_teams function
[ ] Console readability
[ ] Include additional stats for a given displayed team
[ ] Quit Menu Option
"""
# 1) read the existing player data from the PLAYERS constants provided in constants.py
TEAMS = constants.TEAMS
PLAYERS = constants.PLAYERS

# 2) clean the player data without changing the original data
# sauce: https://teamtreehouse.com/library/overwriting-data-in-python
league = copy.deepcopy(TEAMS)
my_players = copy.deepcopy(PLAYERS)


# Create a clean_data function
def clean_data():
    """Clean the player data without changing the original data"""
    clean_player_data = []
    for data in my_players:
        name = data['name']
        guardians = data['guardians'].split(" and ")  # guardians into list
        experience = data['experience']  # experience to bool
        if experience == "YES":
            experience = True
        else:
            experience = False
        height = int(data['height'][:2])  # heights to integer
        clean_player_info = {  # new collection of player data
            'name': name,
            'guardians': guardians,
            'experience': experience,
            'height': height,
        }
        clean_player_data.append(clean_player_info)

    return clean_player_data


def balance_teams():
    """ Make sure the teams have the same number of total players on them when your team balancing function has finished."""
    players = clean_data()
    total_players = len(players)
    total_teams = len(league)
    num_players_team = int(total_players / total_teams)
    # TODO: handle for an odd number of players in the league
    balance = int(num_players_team / 2)

    experienced = []
    inexperienced = []
    for player in players:
        if player['experience'] == True:
            experienced.append(player)
        else:
            inexperienced.append(player)
    random.shuffle(experienced)
    random.shuffle(inexperienced)

    awesome_league = []
    for team in league:
        team_roster = {  # new collection of player data
            'team_name': team,
            'players': [],
            'guardians': '',
            'experienced': 0,
            'inexperienced': 0,
            'avg_height': 0,
        }
        for i in range(balance):
            team_roster['players'].append(experienced.pop())
            team_roster['players'].append(inexperienced.pop())

        guardians = []
        heights = []
        for i in range(len(team_roster['players'])):
            guardian_list_to_str = ", ".join(
                team_roster['players'][i]['guardians'])
            guardians.append(guardian_list_to_str)

            if team_roster['players'][i]['experience'] == True:
                team_roster['experienced'] += 1
            else:
                team_roster['inexperienced'] += 1

            heights.append(team_roster['players'][i]['height'])

        team_roster['guardians'] = ", ".join(guardians)
        team_roster['avg_height'] = round(
            sum(heights) / len(team_roster['players']), 2)

        awesome_league.append(team_roster)
    return(awesome_league)


def results():
    league_data = balance_teams()

    print(league_data)
    # number of inexperienced players on that team
    # number of experienced players on that team
    # the average height of the team
    # the guardians of all the players on that team (as a comma-separated string)
    #   You can calculate the average height for a given team by keeping a running sum total
    #   of each players height on the team and dividing that total by the total number of players on that team.
    pass


if __name__ == "__main__":
    results()
