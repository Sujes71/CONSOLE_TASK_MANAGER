import sqlite3
import pandas as pd
from tabulate import tabulate
from os import _exit


database = r"DB\db.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("[!] Error al conectar con la base de datos")

    return conn

def create_table():
    conn = create_connection(database) 
    cur = conn.cursor()
        
    cur.execute(f"""
                    CREATE TABLE T_GAMES(
                        NAME VARCHAR(100) NOT NULL PRIMARY KEY,
                        STATUS INTEGER NOT NULL
                    )
                """)
    
    conn.commit()
    conn.close()
    print('[+] new table created successfully')

def select_by_query(query):
    if query == '?':
        print('[?] arg1 = insert the query to filter or -fl for get the current status and the status before')
        _exit(1)
    try:
        if query.isnumeric():
            raise Exception
        query = query.upper()
        conn = create_connection(database) 
        cur = conn.cursor()
        cur.execute("select * from t_games where "+ query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = insert the query to filter or -fl for get the current status and the status before
        """ )  
    _exit(1)

def select_all():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT * FROM T_GAMES ORDER BY STATUS DESC")

    rows = cur.fetchall()
    
    conn.close()
    
    return rows

def update_game(name, status):
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("UPDATE T_GAMES SET STATUS = " + str(status) + " WHERE NAME = '" + name + "'")
    
    conn.commit()
    conn.close()
    
    print('[-] updated successfully')

    
def insert_game(name):
    conn = create_connection(database) 
    cur = conn.cursor()

    tuple = [(name, 0)]
    
    cur.executemany("INSERT INTO T_GAMES VALUES (?,?)", tuple)
    conn.commit()
    conn.close()
    print('[+] new row inserted successfully')
    
def remove_game(query):
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("DELETE FROM T_GAMES WHERE " + query)
    
    conn.commit()
    conn.close()
    
    print('[-] deleted successfully')

def query_game(query):  
    try:
        conn = create_connection(database) 
        cur = conn.cursor()
        cur.execute(query)
        
        if "SELECT" in query or "select" in query: 
            rows = cur.fetchall()
            conn.close()
            list_selection_games(rows)
        else:
            conn.commit()
            conn.close()
            if "insert" in query or "INSERT" in query:
                print('[+] new row inserted successfully')
            elif "update" in query or "UPDATE" in query:
                print('[+] updated successfully')
            elif "delete" in query or "DELETE" in query:
                print('[-] deleted successfully')
    except:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = valid query to filter, add, remove or update values from t_games
        """ )  
        _exit(1)
    
def truncate_games():
    conn = create_connection(database) 
    cur = conn.cursor()
     
    cur.execute("DELETE FROM T_GAMES")

    conn.commit()
    conn.close()
    print('[-] truncated successfully')
    
def list_selection_games(query):
    list_names = []
    list_status = []
    
    if not isinstance(query, str):
        selected = query 
    elif query == "*":
        selected = select_all()
    else:
        selected = select_by_query(query)
    
    if (len(selected[0]) == 2):
        for element in selected:
            list_names.append(element[0])
            list_status.append(element[1])
        
    else:
        for element in selected:
            print(element)
        _exit(1)

    print("TABLE GAMES\n")
    df = pd.DataFrame({'NAME':list_names, 'STATUS':list_status})
    df.index = df.index + 1
        
    print(tabulate(df, showindex=True, headers=df.columns))
    print("\n\n0: PENDING\n1: CURRENT\n2: FINISHED")