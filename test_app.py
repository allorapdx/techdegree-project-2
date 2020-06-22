"""
--------------------------------
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
Version 1.0
--------------------------------
"""

#Import player data, copy module, random module, itertools module
import constants
import copy
import itertools
import random

#Copy of tables and create new ones
teams_copy = copy.deepcopy(constants.TEAMS)
players_copy = copy.deepcopy(constants.PLAYERS)
Teams = dict.fromkeys(teams_copy, [])

NUM_PLAYERS_TEAM = len(constants.PLAYERS) / len(constants.TEAMS)
teams_iter = itertools.cycle(teams_copy)


#'Height' saved as an integer
def clean_height():
    for player in players_copy:
        player['height'] = int(player['height'][:2])


#'Experience' saved as a boolean value  
def clean_experience():
    for player in players_copy:
        player['experience'] = True if player['experience'].lower() == 'yes' else False


#'Guardians' split up string into a list
def clean_guardians():
    for player in players_copy:
        player['guardians'] = player['guardians'].split(' and ')


#Balance the players across the three teams with equal experienced
def random_player_balance():
    exp = 0
    for player in players_copy:
        if player['experience'] == bool('TRUE'):
            exp += 1
    num_exp_players_team = exp / len(constants.TEAMS)
    num_non_exp_players_team = NUM_PLAYERS_TEAM - num_exp_players_team
    
    print(NUM_PLAYERS_TEAM)
    print(num_exp_players_team)
    
    random.shuffle(players_copy)
    count = 0
    while count < NUM_PLAYERS_TEAM:
        Teams[next(teams_iter)].append(players_copy[count])
        count += 1


#Display menu to user and continuously loop until user selects 'Quit'
def start_menu():
    print('\n     BASKETBALL TEAM STATS TOOL\n','\n           -----MENU-----\n\n',' Here are your choices:\n','  1) Display Team  Stats\n','  2) Quit\n')
    number_selection = input('Enter an option:  ')
    next = False
    while next is False:
        if number_selection == "1":
            next = True
            stats_menu()
        elif number_selection == '2':
            next = True
            print('\nGoodbye!\n')
        else:
            print('The selection was not a valid option.')
            number_selection = input('Enter an option:  ')


#Display layer two menu used in stat_menu() only
def stats_menu():
    print('\n Here are your choices:\n','  1) Panthers\n','  2) Bandits\n','  3) Warriors\n','  4) Quit\n')
    second_number_selection = input('Enter an option:  ')
    next = False
    while next is False:
        if second_number_selection == '1':
            next = True
            print('\n Team: Panthers Stats\n', '-'*20)
            stats(Teams['Panthers'])
        elif second_number_selection == '2':
            next = True
            print('\n Team: Bandits Stats\n', '-'*20)
            stats(Teams['Bandits'])
        elif second_number_selection == '3':
            next = True
            print('\n Team: Warriors Stats\n', '-'*20)
            stats(Teams['Warriors'])
        elif second_number_selection == '4':
            next = True
            print('\nGoodbye!\n')
        else:
            print('The selection was not a valid option.')
            second_number_selection = input('Enter an option:  ')


#Print stats for selected team used in stats_menu() only
def stats(input_team):
    total_height = 0
    exp = 0
    players_list = []
    guardians_list = []
    for player in input_team:
        total_height += player['height']
        players_list.append(player['name'])
        guardians_list.extend(player['guardians'])
        if player['experience'] == bool('TRUE'):
            exp += 1
    average_height = round(total_height / len(input_team),2)
               
    print(' Total players: {}'.format(len(input_team)))
    print(' Total experienced: {}'.format(exp))
    print(' Total inexperienced: {}'.format(exp))      
    print(' Average height: {}'.format(average_height))   
    print(' \nPlayers on Team: \n ' + ', '.join(players_list))
    print(' \nGuardians: \n ' + ', '.join(guardians_list)) 
    input('\nPress ENTER to continue... ')
    start_menu()   


if __name__ == "__main__":
    clean_height()
    clean_experience()
    clean_guardians()
    random_player_balance()
    start_menu()
