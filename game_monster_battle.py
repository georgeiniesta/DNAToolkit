#game 1 test
from random import randint

game_running = True
game_results = []

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])
def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])
def calculate_player_healing():
    return randint(player['heal_min'], player['heal_max'])

def game_ends(winner_name):
    print(f'{winner_name} won the game')

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Jorge', 'attack_min': 0, 'attack_max': 35, 'heal_min': 0, 'heal_max': 30, 'health': 100}
    monster = {'name': 'Shredder', 'attack_min': 0, 'attack_max': 30, 'health': 100}
    print('---' * 8)
    print('Enter Player Name: ')
    print('---' * 8)
    player['name'] = input()
    print('---' * 8)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:
        counter = counter + 1
        player_won = False
        monster_won = False
        
        print('---' * 8)
        print('Please select action')
        print('---' * 8)
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack()
            if monster['health'] <=0:
               player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <=0:
                    monster_won = True
        
        elif player_choice == '2':
            player['health'] = player['health'] + calculate_player_healing()
            player['health'] = player['health'] - calculate_monster_attack()

            if player['health'] <= 0:
                monster_won = True


        elif player_choice == '3':
            new_round = False
            game_running = False
        
        elif player_choice == '4':
            for player_stats in game_results:
                print(player_stats)
        
        else:
            print('Invalid input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' hp left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' hp left')
        
        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
            
        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': monster['name'], 'health': monster['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False
