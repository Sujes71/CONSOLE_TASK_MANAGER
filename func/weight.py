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
                        MEAL VARCHAR(255) NOT NULL
                    )
                """)
    print('[+] new table created successfully')
    
    conn.commit()
    conn.close()

def select_by_query(query):
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
        arg1 = filter that permits you filter from db the information
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
    
def insert_weight(weight, comidas):
    conn = create_connection(database) 
    cur = conn.cursor()
    
    now = date.today()
    
    ratios = select_all_weights()
    
    if len(ratios) != 0: 
        ratio = weight - int(ratios[len(ratios) - 1][0])
        ratio = round(ratio, 2)
    else:
        ratio = 0
    
    tuple = [(now, weight, ratio, comidas)]
    cur.executemany("INSERT INTO T_WEIGHT VALUES (?,?,?,?)", tuple)
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
    if query == "*":
        selected = select_all()
    else:
        selected = select_by_query(query)

    list_weights = []
    list_ratios = []
    list_comidas = []
    list_dates = []
    
    for element in selected:
        list_weights.append(element[1])
        list_ratios.append(element[2])
        list_comidas.append(element[3])
        list_dates.append(element[0])
        
    print("TABLE WEIGHTS\n")
    df = pd.DataFrame({'WEIGHT':list_weights, 'RATIO':list_ratios, 'MEAL':list_comidas, 'DATE':list_dates})
    df.index = df.index + 1
    print(tabulate(df, showindex=True, headers=df.columns))