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

    menu_choice = int(input(message))
    if menu_choice != 1 and menu_choice != 2:
        raise Exception("Please choose 1 or 2.")

    if menu_choice == 2:
        return
    else:
        for i in range(len(league_data)):
            print(f"\n{i+1}. {league_data[i]['team_name']}")

    teams = list(range(len(league_data)+1))[1:]
    team_choice = int(input("\nEnter an option > "))
    if team_choice not in teams:
        raise Exception("Please choose a number corresponding to a team.")
    if team_choice == 1:
        message = f'''
## Team {league_data[team_choice - 1]['team_name']} Stats

Total Players: {len(league_data[team_choice - 1]['players'])}
Total experienced: {league_data[team_choice - 1]['experienced']}
Total inexperienced: {league_data[team_choice - 1]['inexperienced']}
Average height: {league_data[team_choice - 1]['avg_height']}

Players on Team:
{league_data[team_choice - 1]['player_names']}

Guardians:
{league_data[team_choice - 1]['guardians']}'''

        print(message)


"""
## Team: Panthers Stats

Total players: 6
Total experienced: 3
Total inexperienced: 3
Average height: 42.5

Players on Team:
Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith

Guardians:
Heather Bledsoe, David Alaska, Jamie Alaska, Thomas Helm, Eva Jones, Henrietta Dumas, Hyman Krustofski, Rachel Krustofski, Jim Smith, Jan Smith

Press ENTER to continue...
"""
# number of inexperienced players on that team
# number of experienced players on that team
# the average height of the team
# the guardians of all the players on that team (as a comma-separated string)
#   You can calculate the average height for a given team by keeping a running sum total
#   of each players height on the team and dividing that total by the total number of players on that team.
pass


if __name__ == "__main__":
    results()
