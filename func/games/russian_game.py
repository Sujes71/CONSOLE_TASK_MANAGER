from pynput import keyboard
from random import randint
from time import sleep
from os import system

def russian_game(num_players, round):
    global list_players, turn, bullet, current_player, chamber, list_players_alive
    if round == None:
        ronda = 3
    else:
        ronda = round
    list_players_alive = []
    list_players = []
    turn = randint(0, num_players - 1)
    chamber = num_players * ronda
    bullet = randint(0, chamber)
    
    count = 1
    
    while num_players > 0:
        player = input(f'Player {count}: ').strip()
        
        if player is not None and player not in list_players and player != "":
            list_players.append(player)
            count += 1
            num_players -= 1
        else:
            print('[!] Please choose a valid player name')
    system('cls') 
    current_player = list_players[turn]
    list_players_alive.append(list_players.pop(turn))
    turn = randint(0, len(list_players) - 1)
    chamber -= 1

    print(f'Player {current_player}: Press enter to shoot in your head!')
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def on_press(key):
    if key == keyboard.Key.delete:
        print('[-] russian game cancelled')
        quit()
    if key == keyboard.Key.enter: 
        global list_players, turn, bullet, current_player, chamber, list_players_alive
        
        if bullet == 0:
            print(f'Player {current_player} is deceased!')
            quit()
        else:
            if len(list_players) == 0:
                list_players = list_players_alive.copy()
                list_players_alive.clear()
                
            print(f'Player {current_player} has survived!')
            print("")
                
            if len(list_players) > 1:
                turn = randint(0, len(list_players) - 1)
            else:
                turn = 0
             
            print(f"Currently {len(list_players_alive)} players have survived this round")
            print(f"Currently {len(list_players)} players are still in risk of death")
            print(f"{chamber} remaining chambers ...\n")
            sleep(3)
            chamber -= 1
            bullet -= 1
            current_player = list_players[turn]   
            list_players_alive.append(list_players.pop(turn))
            
            print(f'Player {current_player}: press enter to shoot in your head!')