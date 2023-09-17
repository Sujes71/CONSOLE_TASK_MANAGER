import sqlite3
import os
from datetime import date
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
                    CREATE TABLE T_WEIGHTS(
                        DATE DATE NOT NULL PRIMARY KEY,
                        WEIGHT DECIMAL NOT NULL,
                        RATIO DECIMAL NOT NULL,
                        WEEK VARCHAR(255) NOT NULL,
                        TRAINED BOOLEAN NOT NULL
                    )
                """)
    conn.commit()
    conn.close()
    print('[+] new table created successfully')

def select_first_last():
        conn = create_connection(database) 
        cur = conn.cursor()
        rows = []
        cur.execute("SELECT * FROM (SELECT * FROM t_weights ORDER BY DATE DESC LIMIT 1), (SELECT * FROM t_weights ORDER BY DATE ASC LIMIT 1) ORDER BY DATE DESC")
        rows = cur.fetchall()
        conn.close()
        return rows

def select_by_query(query):
    if query == '?':
        print('[?] arg1 = insert the query to filter or -fl for get the current weight and the weight before')
        _exit(1)
    try:
        if query.isnumeric():
            raise Exception
        query = query.upper()
        conn = create_connection(database) 
        cur = conn.cursor()
        cur.execute("select * from t_weights where "+ query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = insert the query to filter or -fl for get the current weight and the weight before
        """ )  
    _exit(1)

def select_all():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT * FROM T_WEIGHTS ORDER BY DATE DESC")

    rows = cur.fetchall()
    
    conn.close()
    
    return rows

def select_all_weights():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT WEIGHT FROM T_WEIGHTS ORDER BY DATE DESC")

    rows = cur.fetchall()
    
    conn.close()
    
    return rows
    
def insert_weight(weight, comidas, trained):
    conn = create_connection(database) 
    cur = conn.cursor()

    now = date.today()
    
    ratios = select_all_weights()
    
    if trained == "true" or trained == "TRUE":
        trained =  True
    elif trained == "false" or trained == "FALSE":
        trained = False
        
    if len(ratios) != 0: 
        ratio = float(weight) - float(ratios[len(ratios) - 1][0])
        ratio = round(ratio, 2)   
    else:
        ratio = 0
    
    tuple = [(now, weight, ratio, comidas, trained)]
    
    cur.executemany("INSERT INTO T_WEIGHTS VALUES (?,?,?,?,?)", tuple)
    conn.commit()
    conn.close()
    print('[+] new row inserted successfully')
    
def remove_weight(query):
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("DELETE FROM T_WEIGHTS WHERE " + query)
    conn.commit()
    conn.close()
    print('[-] deleted successfully')

def query(query):  
    try:
        conn = create_connection(database) 
        cur = conn.cursor()
        cur.execute(query)
        
        if "SELECT" in query or "select" in query: 
            rows = cur.fetchall()
            conn.close()
            list_selection(rows)
        else:
            if "insert" in query or "INSERT" in query:
                print('[+] new row inserted successfully')
            elif "update" in query or "UPDATE" in query:
                print('[+] updated successfully')
            elif "delete" in query or "DELETE" in query:
                print('[-] deleted successfully')
            conn.commit()
            conn.close()
    except:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = valid query to filter, add, remove or update values from t_weights
        """ )  
        _exit(1)
    
def truncate_weight():
    conn = create_connection(database) 
    cur = conn.cursor()
    
    cur.execute("DELETE FROM T_WEIGHTS")
    
    conn.commit()
    conn.close()
    print('[-] truncated successfully')
    
def list_selection(query):
    list_weights = []
    list_ratios = []
    list_comidas = []
    list_dates = []
    list_trained = []
    
    if not isinstance(query, str):
        selected = query 
    elif query == "*":
        selected = select_all()
    elif query == "-fl":
        selected = select_first_last()
    else:
        selected = select_by_query(query)
    
    if query == "-fl":
        for element in selected:
            list_dates.append(element[0])
            list_weights.append(element[1])
            list_ratios.append(element[2])
            list_comidas.append(element[3])
            list_trained.append(element[4])
            list_dates.append(element[5])
            list_weights.append(element[6])
            list_ratios.append(element[7])
            list_comidas.append(element[8])
            list_trained.append(element[9])
        print("TABLE WEIGHTS\n")
        df = pd.DataFrame({'WEIGHT':list_weights, 'RATIO':list_ratios, 'WEEK':list_comidas, 'TRAINED':list_trained, 'DATE':list_dates})
        index = ["CURRENT", "BEFORE"]
        df.index = index
    else:
        if (len(selected[0]) == 5):
            for element in selected:
                list_dates.append(element[0])
                list_weights.append(element[1])
                list_ratios.append(element[2])
                list_comidas.append(element[3])
                list_trained.append(element[4])
            
        else:
            for element in selected:
                print(element)
            _exit(1)

        print("TABLE WEIGHTS\n")
        df = pd.DataFrame({'WEIGHT':list_weights, 'RATIO':list_ratios, 'WEEK':list_comidas, 'TRAINED':list_trained, 'DATE':list_dates})
        df.index = df.index + 1
        
    print(tabulate(df, showindex=True, headers=df.columns))