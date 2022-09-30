import os
import webbrowser
import sqlite3

database = r"C:\Users\Jesus\Documents\Scripts\console_task_manager\DB\exec.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("[!] Error al conectar con la base de datos")

    return conn

def create_table():
    if not os.path.exists(database):
        conn = create_connection(database) 
        cur = conn.cursor()
        
        cur.execute(f"""
                        CREATE TABLE exec(
                            NAME VARCHAR(15) PRIMARY KEY,
                            DESCRIPTION VARCHAR(255) NOT NULL,
                            PATH VARCHAR(255) NOT NULL
                        )
                    """)
        print('[+] new table created successfully')
        
        conn.commit()
        conn.close()
    else:
        print("[!] Database already exists")

def select_all():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT * FROM APPS")

    rows = cur.fetchall()
    
    conn.close()
    
    return rows

def select_path_byname(name):
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT PATH FROM APPS WHERE NAME=? ", (name,))

    rows = cur.fetchall()[0][0]
    
    conn.close()
    
    return rows

def insert(name, description, path):
    conn = create_connection(database) 
    cur = conn.cursor()
    
    tuple = [(name, description, path)]
    cur.executemany("INSERT INTO APPS VALUES (?,?,?)", tuple)
    print('[+] new row inserted successfully')
    
    conn.commit()
    conn.close()
    
def remove(name):
    conn = create_connection(database) 
    cur = conn.cursor()
   
    cur.execute("SELECT * FROM APPS WHERE NAME=? ", (name,))
    row = cur.fetchall()
    
    if row.__len__() == 1:
        cur.execute("DELETE FROM APPS WHERE NAME=? ", (name,))
        print('[-] row removed successfully')
        conn.commit()
    else:
        print('[!] row does not exists')
    conn.close()

def truncate():
    conn = create_connection(database) 
    cur = conn.cursor()
    
    cur.execute("DELETE FROM APPS")
    print('[-] truncated successfully')
    
    conn.commit()
    conn.close()

def exec(query):
    list = []
    for name in select_all():
        list.append(name[0])
        
    if '.com' in query or '.es' in query or '.net' in query:
        webbrowser.open(f'https://www.{query}')
        print('[+] web reached succesfully')
    elif query in list:
        os.startfile(select_path_byname(query))
        print('[+] program opened succesfully')
                
    else:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = name of the program or web domain, -l/--list to list all available, --add to include a new one, --remove to remove or --init to initialize the table, --truncate to remove all db elements
        """ )
        
def list_apps():
    for app in select_all():
        print("%-15s %1s" % (app[0], app[1]))