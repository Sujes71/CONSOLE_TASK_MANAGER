from random import randint
from os import system

ppt = {
    "rock":{
        "rock":"draw!",
        "paper":"you lose!",
        "scissors":"you win!"
    }    ,
    "paper":{
        "paper":"draw!",
        "scissors":"you lose!",
        "rock":"you win!"
    },
    "scissors":{
        "scissors":"draw!",
        "paper":"you win!",
        "rock":"you lose!"
    }
}

ppt_machine = {
    0:"rock",
    1:"paper",
    2:"scissors"
}
def rps_game(my_move):
    try:
        if my_move not in ppt:
            raise Exception
        computer_move = ppt_machine[randint(0,2)]
        print(f"(user) {my_move} vs {computer_move} (pc)\n")
        print(ppt[my_move][computer_move])
    except:
        print('[!] %s ' %(f'error: argument {[my_move]}: expected one valid argument'))
        print("""
        arg1 = choose rock, paper or scissors
        """ )
