import sys
from func.generator import generate, generate_only_folders
from func.scrap import list_anime, list_league
from func.weight import insert_weight, list_selection, truncate_weight, remove_weight, query
from func.games.rps_game import rps_game
from func.games.russian_game import russian_game
from func.pending_games import insert_game, truncate_games, remove_game, list_selection_games, update_game, query_game

arg = [ '-h', '--help', '-g', '--generator', '-sc', '--scrap', '-w', '--weight', '-ga', '--game', '-pg', '--pending']

try:
    error = ['argument not recognized', f'error: argument [{sys.argv[1]}]: expected one or two arguments', f'error: argument [{sys.argv[1]}]: expected one argument', f'error: argument [{sys.argv[1]}]: expected four arguments', f'error: argument [{sys.argv[1]}]: expected three arguments', f'error: argument [{sys.argv[1]}]: expected no arguments', f'error: argument [{sys.argv[1]}]: expected three or four arguments', f'error: argument [{sys.argv[1]}]: expected two arguments']
    
except:
    print('[!] you did not entered arguments')
    print("optional arguments:"+"""
                -h,  --help  show the avaiable arguments
                """ )
    quit()
    
def task_help():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')

        print('the avaiable arguments are: %s' %(arg))
        print("""
                -h/--help = show the avaiable arguments
                -g/--generator = generate a folder system for projects
                -sc/--scrap = permits the user to scrapping last animes and football result
                -w/--weight = permits the user to have a daily control of the weight and meal
                -ga/--game permits the user to select multiple options of games
                -pg/--pending permits the user to have a daily control of the pending games
                """ )
    else:
        print('[!] %s ' %(error[5]))
        print("""
        expected no arguments
        """ )

def task_generator():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -g,  --generator  generate a folder system for projects
            """ )
        
    elif len(sys.argv) == 3:
        if sys.argv[2] == '?':
            print('[?] arg1 = folder name')
        else:
            generate_only_folders(sys.argv[2])
        
    elif len(sys.argv) == 4 and sys.argv[2] != '?':
        if sys.argv[3] == '?':
            print('[?] arg2 = task code')
        else:
            generate(sys.argv[2], sys.argv[3])
       
    else:
        print('[!] %s ' %(error[1]))
        print("""
        arg1 = folder name
        arg2 = task code
        """ )
                    
def task_scrap():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -sc,  --scrap permits the user to scrapping last animes and football result
            """ )
    elif len(sys.argv) == 3: 
        if sys.argv[2] == '?':
            print('[?] arg1 = -a/--anime to scrap last anime emissions or -f/--football to scrap last informations about leagues')
        elif sys.argv[2] == '-a' or sys.argv[2] == '--anime':
            list_anime()
        elif sys.argv[2] == '-f' or sys.argv[2] == '--football':
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
            print("""
            arg2 = 'laliga' if you want to scrap laliga information or 'premier' if you want to scrap premier league information
            """ )
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = -a/--anime to scrap last anime emissions or -f/--football to scrap last informations about leagues
            """ )
    elif len(sys.argv) == 4 and (sys.argv[2] == '-f' or sys.argv[2] == '--football'):
        try:
            if sys.argv[3] == '?':
                print("[?] arg2 = 'laliga' if you want to scrap laliga information or 'premier' if you want to scrap premier league information")
            else:
                list_league(sys.argv[3])
        except:
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
            print("""
            arg2 = 'laliga' if you want to scrap laliga information or 'premier' if you want to scrap premier league information
            """ )
    elif sys.argv[2] == '-a' or sys.argv[2] == '--anime':
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected no arguments'))
            print("""
            expected no arguments
            """ )
    else:
        print('[!] %s ' %(error[2]))
        print("""
        arg1 = -a/--anime to scrap last anime emissions or -f/--football to scrap last informations about leagues
        """ )
def task_weight():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -w,  --weight permits the user to have a daily control of the weight and meal
            """ )
    elif len(sys.argv) == 3:
        if sys.argv[2] == '--list' or sys.argv[2] == '-l':
            list_selection("*")
        elif sys.argv[2] == '--add':
            print('[!] %s ' %(error[4]))
            print("""
            arg1 = the weight of today
            arg2 = the meal you have eaten today
            arg3 = true if you trained or false if not
            """ )
        elif sys.argv[2] == '--truncate':
            truncate_weight()
            
        elif sys.argv[2] == '?':
            print('[?] arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_weight \nor --query '+
            'to select, add, remove or update')
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_weight \n            or --query to select, add, remove or update
            """ )
    elif len(sys.argv) == 4 or len(sys.argv) == 6:
        if sys.argv[2] == '--filter' and len(sys.argv) == 4:
            list_selection(sys.argv[3])
                
        elif sys.argv[2] == '--add':
            try:
                if sys.argv[3] == '?':
                    print('[?] arg1 = the weight of today')
                elif sys.argv[4] == '?':
                    print('[?] arg2 = the meal you have eaten today')
                elif sys.argv[5] == '?':
                    print('[?] arg3 = true if you trained or false if not')
                else:
                    insert_weight(sys.argv[3], sys.argv[4], sys.argv[5])
            except:
                print('[!] %s ' %(error[4]))
                print("""
                arg1 = the weight of today
                arg2 = the meal you have eaten today
                arg3 = true if you trained or false if not
                """ )
        elif sys.argv[2] == '--truncate':
            try:
                
                if sys.argv[3] == '?':
                    print('[?] arg1 = the query filter to remove in db')
                else:
                    remove_weight(sys.argv[3])
            except:
                print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
                print("""
                arg1 = the query filter to remove in db
                """ )
        elif sys.argv[2] == '--query':
            if sys.argv[3] == '?':
                    print('[?] arg1 = valid query to select, add, remove or update values from t_weight')
            else:
                query(sys.argv[3])
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_weight \n            or --query to select, add, remove or update
            """ )
    else:
        print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
        print("""
        arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_weight \n            or --query to select, add, remove or update
        """ )
        
def task_peding_games():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -pg,  --pending permits the user to have a daily control of the game´s im playing
            """ )
    elif len(sys.argv) == 3:
        if sys.argv[2] == '--list' or sys.argv[2] == '-l':
            list_selection_games("*")
        elif sys.argv[2] == '--add':
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = the name of the game
            """ )
        elif sys.argv[2] == '--truncate':
            truncate_games()
            
        elif sys.argv[2] == '?':
            print('[?] arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_games \n, --query or --update  '+
            'to select, add, remove or update')
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_games \n            , --query or --update to select, add, remove or update
            """ )
    elif len(sys.argv) >= 4 or len(sys.argv) <= 6:
        if sys.argv[2] == '--filter' and len(sys.argv) == 4:
            list_selection_games(sys.argv[3])
                
        elif sys.argv[2] == '--add':
            try:
                if sys.argv[3] == '?':
                    print('[?] arg1 = the name of the game')
                else:
                    insert_game(sys.argv[3])
            except:
                print('[!] %s ' %(error[2]))
                print("""
                arg1 = the name of the game
                """ )
        elif sys.argv[2] == '--update':
            try:
                if sys.argv[3] == '?':
                    print('[?] arg1 = the name of the game')
                elif sys.argv[4] == '?':
                    print('[?] arg2 = the status of the game')
                else:
                    update_game(sys.argv[3], sys.argv[4])
            except:
                print('[!] %s ' %(error[7]))
                print("""
                arg1 = the name of the game
                arg2 = the status of the game
                """ )
        elif sys.argv[2] == '--truncate':
            try:
                
                if sys.argv[3] == '?':
                    print('[?] arg1 = the query filter to remove in db')
                else:
                    remove_game(sys.argv[3])
            except:
                print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
                print("""
                arg1 = the query filter to remove in db
                """ )
        elif sys.argv[2] == '--query':
            if sys.argv[3] == '?':
                    print('[?] arg1 = valid query to select, add, remove or update values from t_games')
            else:
                query_game(sys.argv[3])
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_games \n            or , --query or --update to select, add, remove or update
            """ )
    else:
        print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
        print("""
        arg1 = -l/--list to list all available, --add to include a new one, --filter to filter data, --truncate to remove elements in t_games \n            or , --query or --update to select, add, remove or update
        """ )
        
def task_game():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""to
            -ga,  --game permits the user to select multiple options of games
            """ )
    elif len(sys.argv) == 3:
        if sys.argv[2] == '?':
            print('[?] arg1 = -rps to choose rock, paper or scissors game, ...')
        elif sys.argv[2] == '-rps':
            print('[?] this is the rock, paper or scissors game, if you want to play just put your selection here instead')
        elif sys.argv[2] == '-rg':
            print('[?] this the russian roulette game modified for being more fair')
        else:
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
            print("""
            arg1 = -rps to choose rock, paper or scissors game, -rg to choose the russian roulete, ...
            """ )
    elif len(sys.argv) == 4:
        if sys.argv[2] == '?':
             print('[?] arg1 = -rps to choose rock, paper or scissors game, -rg to choose the russian roulete, ...')
        elif sys.argv[2] == '-rps':
            if sys.argv[3] == '?':
                print('[?] arg2 = choose rock, paper or scissors')
            else:
                rps_game(sys.argv[3])
        elif sys.argv[2] == '-rg':
            if sys.argv[3] == '?':
                print('[?] arg2 = introduce the number of players')
            else:
                russian_game(int(sys.argv[3]), None)
    elif len(sys.argv) == 5:
        if sys.argv[2] == '?':
             print('[?] arg1 = -rps to choose rock, paper or scissors game, -rg to choose the russian roulete, ...')
        elif sys.argv[2] == '-rg':
            if sys.argv[3] == '?':
                print('[?] arg2 = introduce the number of players')
            elif sys.argv[4] == '?':
                print('[?] arg3 = introduce the number of rounds for multiply gun charmbers')
            else:
                russian_game(int(sys.argv[3]), int(sys.argv[4]))
            
        else:
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
            print("""
            arg1 = -rps to choose rock, paper or scissors game, -rg to choose the russian roulete, ...
            """ )
    else:
        print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
        print("""
        arg1 = -rps to choose rock, paper or scissors game, -rg to choose the russian roulete, ...
        """ )
        
sys_args = {
    arg[0]:task_help,
    arg[1]:task_help,
    arg[2]:task_generator,
    arg[3]:task_generator,
    arg[4]:task_scrap,
    arg[5]:task_scrap,
    arg[6]:task_weight,
    arg[7]:task_weight,
    arg[8]:task_game,
    arg[9]:task_game,
    arg[10]:task_peding_games,
    arg[11]:task_peding_games
}

try:
    sys_args[sys.argv[1]]()
    
except:
    print('[!] %s ' %(error[0]))
    print(f'you entered: [{sys.argv[1]}]')
    print('the avaiable arguments are: %s' %(arg))