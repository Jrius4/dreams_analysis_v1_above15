import pandas as pd, numpy as np
from sqlalchemy import create_engine
import glob



def connect_to_db():
    engine = create_engine("sqlite:///db/dreams_services.db")
    return engine



def create_table_from_excel(name_table:str):
    conn = connect_to_db()
    to_sql = pd.read_excel(f"load/{name_table}.xlsx")
    to_sql.to_sql(name=name_table,con=conn,if_exists='append')


path =r'load'
filenames = glob.glob(path + "/*.xlsx")

filename_real = []

for i in filenames:
    i = str(i).replace("load\\",'').replace('.xlsx','')
    create_table_from_excel(i)




# cur = conn.execute('SELECT * FROM stones')
# stones = pd.read_excel("load/events_stepping_stones.xlsx")
# stones.to_sql(name='stones',con=conn,if_exists='append')
# cur = conn.execute('SELECT * FROM stones')
# rows = cur.fetchall()
# print(rows)

