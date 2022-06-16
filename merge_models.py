import pandas as pd, numpy as np
from sqlalchemy import create_engine

def connect_to_db():
    engine = create_engine("sqlite:///db/dreams_services.db")
    return engine


conn = connect_to_db()

query = """
with ses_as_ss AS (SELECT *
FROM ses s
INNER JOIN stepping_stones ss ON s."DREAMS ID No" = ss."DREAMS ID No") SELECT * FROM ses_as_ss;
"""

results_ses_ss = conn.execute(query)

rows_results_ses_ss = results_ses_ss.fetchall()
col_names_results_ses_ss = [col for col in results_ses_ss.keys()]


numpy_data = np.array(rows_results_ses_ss)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_ses_ss)

df.to_excel("output/data_col_names_results_ses_ss.xlsx",index=False)
