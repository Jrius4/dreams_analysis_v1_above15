import pandas as pd, numpy as np
from sqlalchemy import create_engine


def connect_to_db():
    engine = create_engine("sqlite:///db/districts.db")
    return engine

conn = connect_to_db()

df = pd.read_json("./load/districts.min.json")

print(df.head)
conn.execute("DROP TABLE IF EXISTS districts")

df.to_sql(name="districts",con=conn)
res = conn.execute("select DistrictName from districts limit 5")

print(res.fetchall())

