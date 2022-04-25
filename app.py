import constants
import copy
import random

""" TODO
[X] Create app.py
[X] Proper use of Dunder Main
[X] Import from constants.py the players' data to be used within your program.
[X] Create a clean_data function
[X] Create a balance_teams function
[X] Console readability
[X] Include additional stats for a given displayed team
[X] Quit Menu Option
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
    # Future TODO: handle for an odd number of players in the league
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
            'player_names': '',
            'guardians': '',
            'experienced': 0,
            'inexperienced': 0,
            'avg_height': 0,
        }
        for i in range(balance):
            team_roster['players'].append(experienced.pop())
            team_roster['players'].append(inexperienced.pop())

        player_names = []
        guardians = []
        heights = []
        for i in range(len(team_roster['players'])):
            player_names.append(team_roster['players'][i]['name'])
            team_roster['player_names'] = ", ".join(player_names)

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

    message = '''
BASKETBALL TEAM STATS TOOL


---- MENU----

Here are your choices:

1. Display Team Stats
2. Quit

Enter an option > '''
    keep_running = True
    while keep_running:
        try:
            menu_choice = int(input(message))
            if menu_choice != 1 and menu_choice != 2:
                raise Exception(
                    "----------------------> Please choose 1 or 2.")
        except Exception:
            print("----------------------> Please choose 1 or 2")
        else:
            if menu_choice == 2:
                return
            else:
                for i in range(len(league_data)):
                    print(f"\n{i+1}. {league_data[i]['team_name']}")

            teams = list(range(len(league_data)+1))[1:]
            try:
                team_choice = int(input("\nEnter an option > "))
                if team_choice not in teams:
                    raise Exception(
                        "----------------------> Please choose a number corresponding to a team.")
            except Exception:
                print(
                    "----------------------> Please choose a number corresponding to a team.")
            else:
                print(f"""
Team: {league_data[team_choice - 1]['team_name']}
-----------------------
Total Players: {len(league_data[team_choice - 1]['players'])}
Total experienced: {league_data[team_choice - 1]['experienced']}
Total inexperienced: {league_data[team_choice - 1]['inexperienced']}
Average height: {league_data[team_choice - 1]['avg_height']}

Players on Team:
{league_data[team_choice - 1]['player_names']}

Guardians:
{league_data[team_choice - 1]['guardians']}\n""")

                restart = input("\nPress ENTER to continue...")
                if restart == "":
                    keep_running = True
                else:
                    keep_running = False


if __name__ == "__main__":
    results()
