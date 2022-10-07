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
                    CREATE TABLE T_WEIGHT(
                        DATE DATE NOT NULL PRIMARY KEY,
                        WEIGHT DECIMAL NOT NULL,
                        RATIO DECIMAL NOT NULL,
                        MEAL VARCHAR(255) NOT NULL,
                        TRAINED BOOLEAN NOT NULL
                    )
                """)
    print('[+] new table created successfully')
    
    conn.commit()
    conn.close()

def select_first_last():
        conn = create_connection(database) 
        cur = conn.cursor()
        rows = []
        cur.execute("SELECT * FROM (SELECT * FROM t_weight ORDER BY DATE DESC LIMIT 1), (SELECT * FROM t_weight ORDER BY DATE ASC LIMIT 1) ORDER BY DATE DESC")
        rows = cur.fetchall()
        conn.close()
        return rows

def select_by_query(query):
    if query == '?':
        print('[?] arg1 = insert the query to filter or -fl for get the current weight and the weight before')
        _exit(0) 
    try:
        if query.isnumeric():
            raise Exception
        query = query.upper()
        conn = create_connection(database) 
        cur = conn.cursor()
        cur.execute("select * from t_weight where "+ query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        print(f'[!] error: arg1 [{query}]: expected one valid arg1' )
        print("""
        arg1 = insert the query to filter or -fl for get the current weight and the weight before
        """ )  
    _exit(0) 

def select_all():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT * FROM T_WEIGHT ORDER BY DATE DESC")

    rows = cur.fetchall()
    
    conn.close()
    
    return rows

def select_all_weights():
    conn = create_connection(database) 
    cur = conn.cursor()
    cur.execute("SELECT WEIGHT FROM T_WEIGHT ORDER BY DATE DESC")

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
        ratio = weight - float(ratios[len(ratios) - 1][0])
        ratio = round(ratio, 2)
    else:
        ratio = 0
    
    tuple = [(now, weight, ratio, comidas, trained)]
    cur.executemany("INSERT INTO T_WEIGHT VALUES (?,?,?,?,?)", tuple)
    print('[+] new row inserted successfully')
    
    conn.commit()
    conn.close()
    
def truncate_weight():
    conn = create_connection(database) 
    cur = conn.cursor()
    
    cur.execute("DELETE FROM T_WEIGHT")
    print('[-] truncated successfully')
    
    conn.commit()
    conn.close()
    
def list_selection(query):
    list_weights = []
    list_ratios = []
    list_comidas = []
    list_dates = []
    list_trained = []
    
    if query == "*":
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
        df = pd.DataFrame({'WEIGHT':list_weights, 'RATIO':list_ratios, 'MEAL':list_comidas, 'TRAINED':list_trained, 'DATE':list_dates})
        index = ["CURRENT", "BEFORE"]
        df.index = index
    else:
        for element in selected:
            list_dates.append(element[0])
            list_weights.append(element[1])
            list_ratios.append(element[2])
            list_comidas.append(element[3])
            list_trained.append(element[4])
        print("TABLE WEIGHTS\n")
        df = pd.DataFrame({'WEIGHT':list_weights, 'RATIO':list_ratios, 'MEAL':list_comidas, 'TRAINED':list_trained, 'DATE':list_dates})
        df.index = df.index + 1
        
    print(tabulate(df, showindex=True, headers=df.columns)) 
