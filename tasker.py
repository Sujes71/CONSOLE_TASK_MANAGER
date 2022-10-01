import sys
from func.generator import generate, generate_only_folders
from func.timer import ring
from func.exec import exec, insert, list_apps, remove, create_table, truncate
from func.shutdown import shutdown
from func.out  import signout, listout
from func.scrap import list_anime, list_league
from os import _exit

arg = [ '-h', '--help', '-g', '--generator', '-a', '--alarm', '-e', '--exec', '-s', '--shutdown', '--outsign', '-o', '-sc', '--scrap']

try:
    error = ['argument not recognized', f'error: argument [{sys.argv[1]}]: expected one or two arguments', f'error: argument [{sys.argv[1]}]: expected one argument', f'error: argument [{sys.argv[1]}]: expected four arguments', f'error: argument [{sys.argv[1]}]: expected three arguments', f'error: argument [{sys.argv[1]}]: expected no arguments', f'error: argument [{sys.argv[1]}]: expected three or four arguments']
    
except:
    print('[!] you did not entered arguments')
    print("optional arguments:"+"""
                -h,  --help  show the avaiable arguments
                """ )
    _exit(0)
    
def task_help():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')

        print('the avaiable arguments are: %s' %(arg))
        print("""
                -h/--help = show the avaiable arguments
                -g/--generator = generate a folder system for projects
                -a/--alarm = program an alarm at the specified time specifying or not a youtube video
                -e/--exec = execute a program or open a website and permits you check, add or remove apps from exec db
                -s/--shutdown = program a time to shutdown pc
                -o/--outsign = permits the user to sign out from work metaenlace
                -sc/--scrap = permits the user to scrapping last animes and football result
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

def task_alarm():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -a,  --alarm  program an alarm at the specified time specifying or not a youtube video
            """ )
        
    elif len(sys.argv) == 3:
        if sys.argv[2] == '?':
            print('[?] arg1 = time to ring alarm HH:MM:SS or HH:MM')
        else:
            ring(sys.argv[2], 'None')
    
    elif len(sys.argv) == 4 and sys.argv[2] != '?':
        if sys.argv[3] == '?':   
            print('[?] arg2 = youtube video to ring')
        else:
            ring(sys.argv[2], sys.argv[3])
        
    else:
        print('[!] %s ' %(error[1]))
        print("""
        arg1 = time to ring alarm HH:MM:SS or HH:MM
        arg2 = youtube video to ring
        """ )
        
def task_exec():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -e,  --exec  execute a program or open a website and permits you check, add or remove apps from exec db
            """ )
    
    elif len(sys.argv) == 3:  
        if sys.argv[2] == '--list' or sys.argv[2] == '-l':
            list_apps()
        elif sys.argv[2] == '--init':
            create_table()
        elif sys.argv[2] == '--add':
                print('[!] %s ' %(error[4]))
                print("""
                arg1 = name of the program to add
                arg2 = description of the program to add
                arg3 = path of the program to add
                """ )
        elif sys.argv[2] == '--remove' or sys.argv[2] == '-r':
                print('[!] %s ' %(error[2]))
                print("""
                arg1 = name of the program to remove
                """ )
        elif sys.argv[2] == '--truncate':
            truncate()
            
        elif sys.argv[2] == '?':
            print('[?] arg1 = name of the program or web domain, -l/--list to list all available, --add to include a new one, --remove to remove or --init to initialize the table, --truncate to remove all db elements')
        else:
            exec(sys.argv[2])
        
    elif len(sys.argv) > 3 and len(sys.argv) <= 6:
        if sys.argv[2] == '--add':
            try:
                if len(sys.argv) == 6 and sys.argv[5] != '?' and sys.argv[4] != '?' and sys.argv[3] != '?':
                    insert(sys.argv[3], sys.argv[4], sys.argv[5])
                elif sys.argv[3] == '?':
                    print('[?] arg1 = name of the program to add')
                elif sys.argv[4] == '?':
                    print('[?] arg2 = description of the program to add')
                elif sys.argv[5] == '?':
                    print('[?] arg3 = path of the program to add')
            except:
                print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected three arguments'))
                print("""
                arg1 = name of the program to add
                arg2 = description of the program to add
                arg3 = path of the program to add
                """ )
        elif sys.argv[2] == '--remove':
            if len(sys.argv) == 4 and sys.argv[3] != '?':
                remove(sys.argv[3])
            elif sys.argv[3] == '?':
                print('[?] arg1 = name of the program to remove')
            else:
                print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected one argument'))
                print("""
                arg1 = name of the program to remove
                """ )
        elif sys.argv[2] == '--list' or sys.argv[2] == '-l':
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected no arguments'))
            print("""
            expected no arguments
            """ )
            
        elif sys.argv[2] == '--init':
            print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected no arguments'))
            print("""
            expected no arguments
            """ )
        else:
            print('[!] %s ' %(error[2]))
            print("""
            arg1 = name of the program or web domain, -l/--list to list all available, --add to include a new one, --remove to remove or --init to initialize the table, --truncate to remove all db elements'
            """ )
    else:
        print('[!] %s ' %(error[2]))
        print("""
        arg1 = name of the program or web domain, -l/--list to list all available, --add to include a new one, --remove to remove or --init to initialize the table, --truncate to remove all db elements'
        """ )

def task_shutdown():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -s,  --shutdown  program a time to shutdown pc
            """ )
    elif len(sys.argv) == 3: 
        if sys.argv[2] == '?':
            print('[?] arg1 = time to shutdown HH:MM:SS or HH:MM')
        else:
            shutdown(sys.argv[2])
            
    else:
        print('[!] %s ' %(error[2]))
        print("""
        arg1 = time to shutdown HH:MM:SS or HH:MM
        """ )
        
def task_signout():
    if len(sys.argv) == 2:
        print(f'usage: {sys.argv[0]} [{sys.argv[1]}]')
        print("optional arguments:"+"""
            -o,  --outsign program wich permits you to sign out work
            """ )
    elif len(sys.argv) >= 3 and len(sys.argv) < 6:
        try:
            if (sys.argv[2] == '-l' or sys.argv[2] == '--list') and len(sys.argv) == 3:
                listout()
            elif (sys.argv[2] == '-l' or sys.argv[2] == '--list') and len(sys.argv) > 3:
                print('[!] %s ' %(f'error: argument [{sys.argv[1]} {sys.argv[2]}]: expected no arguments'))
                print("""
                expected no arguments
                """ )
                
            elif sys.argv[2] == '?' and len(sys.argv) == 3:
                print('[?] arg1 = project to sign out or -l/--list to list all projects and tasks')
            elif sys.argv[3] == '?' and len(sys.argv) == 4 and sys.argv[2] != '?':
                print('[?] arg2 = task to sign out')
            elif sys.argv[4] == '?' and len(sys.argv) == 5 and sys.argv[2] != '?' and sys.argv[3] != '?':
                print('[?] arg3 = description of task')
            elif len(sys.argv) == 5 and sys.argv[2] != '?' and sys.argv[3] != '?' and sys.argv[4] != '?':
                signout(sys.argv[2], sys.argv[3], sys.argv[4], 'None')
            else:
                print('[!] %s ' %(error[6]))
                print("""
                arg1 = project to sign out or -l/--list to list all projects and tasks
                arg2 = task to sign out
                arg3 = description of task
                arg4 = time to sign out <optional>
                """ )
        except:
            print('[!] %s ' %(error[6]))
            print("""
            arg1 = project to sign out or -l/--list to list all projects and tasks
            arg2 = task to sign out
            arg3 = description of task
            arg4 = time to sign out <optional>
            """ )
    elif len(sys.argv) == 6 and sys.argv[2] != '?' and sys.argv[3] != '?' and sys.argv[4] != '?':
        if sys.argv[5] == '?':
            print('[?] arg4 = time to sign out or default/* for default time sign out')
        else:
            signout(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

    else:
        print('[!] %s ' %(error[6]))
        print("""
        arg1 = project to sign out or -l/--list to list all projects and tasks
        arg2 = task to sign out
        arg3 = description of task
        arg4 = time to sign out <optional>
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
        
sys_args = {
    arg[0]:task_help,
    arg[1]:task_help,
    arg[2]:task_generator,
    arg[3]:task_generator,
    arg[4]:task_alarm,
    arg[5]:task_alarm,
    arg[6]:task_exec,
    arg[7]:task_exec,
    arg[8]:task_shutdown,
    arg[9]:task_shutdown,
    arg[10]:task_signout,
    arg[11]:task_signout,
    arg[12]:task_scrap,
    arg[13]:task_scrap
}

try:
    sys_args[sys.argv[1]]()
    
except:
    print('[!] %s ' %(error[0]))
    print(f'you entered: [{sys.argv[1]}]')
    print('the avaiable arguments are: %s' %(arg))
