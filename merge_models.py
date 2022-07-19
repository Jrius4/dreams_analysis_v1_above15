import pandas as pd, numpy as np
from sqlalchemy import create_engine

def connect_to_db():
    engine = create_engine("sqlite:///db/dreams_services.db")
    return engine


conn = connect_to_db()

query = """
with ses_as_ss AS (SELECT *
FROM ses
INNER JOIN stepping_stones ss ON ses."DREAMS ID No" = ss."DREAMS ID No") 
SELECT s."DREAMS ID No", s."First Name" , s."Last Name" ,s."DREAMS_SES Service" as SES_TYPE ,
s."Financial Literacy Training", s."Financial literacy training start date", s."Financial literacy training end date" , s."Number of days financial literacy done",
s."VSLA/SILC" ,s."VSLA/SILC Start Date" ,s."VSLA/SILC End Date", s."Number of days VSLA/SILC" ,
s."Asset financing Package" ,s."Asset financing training start date" ,s."Asset financing training end date" ,s."Number of days asset financing package done",
s."Education Status", s."Age at entry (must be whole number e.g 10, 14, 17)" ,s."Current Age", s."Date of Birth" ,
s."Number of stepping stones sessions attended"  ,s."Group Name" AS GRP,
CAST(SUBSTRING(s."DREAMS ID No",14) AS INT) AS ID_NO
FROM ses_as_ss as s order by SES_TYPE,GRP;
"""

results_ses_ss = conn.execute(query)

rows_results_ses_ss = results_ses_ss.fetchall()
col_names_results_ses_ss = [col for col in results_ses_ss.keys()]


numpy_data = np.array(rows_results_ses_ss)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_ses_ss)

df.to_excel("output/data_results_ses_ss.xlsx",index=False)



query = """
with condoms_as_ss AS (SELECT *
FROM condoms c 
INNER JOIN stepping_stones ss ON c."DREAMS ID No" = ss."DREAMS ID No") 
SELECT STRFTIME('%d/%m/%Y', cas."Event date" ) AS EVENT_DATE,cas."DREAMS ID No",cas."Date of Birth" , cas."Group Name" as GRP,cas."Number of condoms given" ,cas."Address Village",cas."Address Parish" ,cas."Distribution Point"
FROM condoms_as_ss as cas order by cas."Event date",GRP ASC;
"""

results_condoms_ss = conn.execute(query)

rows_results_condoms_ss = results_condoms_ss.fetchall()
col_names_results_condoms_ss = [col for col in results_condoms_ss.keys()]


numpy_data = np.array(rows_results_condoms_ss)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_condoms_ss)

df.to_excel("output/data_results_condoms_ss.xlsx",index=False)
