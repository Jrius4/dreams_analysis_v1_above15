import pandas as pd, numpy as np
from sqlalchemy import create_engine

def connect_to_db():
    engine = create_engine("sqlite:///db/dreams_services.db")
    return engine


conn = connect_to_db()


cur_1 = conn.execute('''SELECT CAST(SUBSTRING(ag."DREAMS ID No",14) AS INT) AS ID_NO, ag."First Name" , ag."Last Name" , ag."DREAMS ID No" , ag."Current Age" ,
                            ag."Age at entry (must be whole number e.g 10, 14, 17)" as age_entry, ag."Address Village" ,ag."Address Parish"  from all_girls ag 
                            where ag."Age at entry (must be whole number e.g 10, 14, 17)" = "15-19" OR  ag."Current Age" = "20 - 24"''')

cur_2 = conn.execute(''' select CAST(SUBSTRING(s."DREAMS ID No",14) AS INT) AS ID_NO, s."First Name" , s."Last Name" ,s."DREAMS ID No" ,
                        s."Current Age", s."Group Name" from stones s ''')

rows_1 = cur_1.fetchall()
rows_2 = cur_2.fetchall()

data_1 = []
data_2 = []
for i in rows_1:
    data_1.append(i[0])

for i in rows_2:
    data_2.append(i[0])

data_need_stones = []
for i in data_1:
    if i not in data_2:
        cur_2 = conn.execute(f''' SELECT CAST(SUBSTRING(ag."DREAMS ID No",14) AS INT) AS ID_NO, ag."First Name" , ag."Last Name" , ag."DREAMS ID No" , ag."Current Age" ,
                            ag."Age at entry (must be whole number e.g 10, 14, 17)" as age_entry, ag."Address Village" ,ag."Address Parish",ag."Phone Number" ,ag."Sim Card Number"  from all_girls ag 
                            where ID_NO = {i} ''') 

        row_1 = cur_2.fetchone() 

        data_need_stones.append(row_1)

numpy_data = np.array(data_need_stones)

# df = pd.DataFrame(data=numpy_data, index=["row1", "row2"], columns=["column1", "column2"])
df = pd.DataFrame(data=numpy_data, columns=["ID", "FIRST NAME","LAST NAME","DREAMS ID NO","AGE", "ENTRY AGE","VILLAGE","PARISH","Phone","Simcard"])
# print(df)

df.to_excel("output/data.xlsx")



        



  











