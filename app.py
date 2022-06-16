import pandas as pd, numpy as np
from sqlalchemy import create_engine

def connect_to_db():
    engine = create_engine("sqlite:///db/dreams_services.db")
    return engine


conn = connect_to_db()


results_all_girls = conn.execute('''SELECT DISTINCT ag."DREAMS ID No", CAST(SUBSTRING(ag."DREAMS ID No",14) AS INT) AS ID_NO,
    ag."Last Name" , ag."First Name" ,ag."Sim Card Number" ,ag."Sim Card Number" ,
    ag."Date of Birth" as dob,
    CAST((strftime('%Y', 'now') - strftime('%Y', ag."Date of Birth")) 
        - (strftime('%m-%d', 'now') < strftime('%m-%d', ag."Date of Birth") ) AS INT) AS AGE,
    ag."Address Village" ,ag."Address Parish" ,ag."Mother's Maiden Name" AS CAREGIVER ,ag."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
    ag."Current Age",ag."Name of school" AS SCH
    from all_girls ag order by  ID_NO''')





rows_all_girls = results_all_girls.fetchall()
col_names_all_girls = [col for col in results_all_girls.keys()]

# print(col_names_all_girls)

# print(rows_all_girls)

numpy_data = np.array(rows_all_girls)

df = pd.DataFrame(data= numpy_data, columns=col_names_all_girls)

df.to_excel("output/data_allgirls.xlsx",index=False)


results_stones = conn.execute('''
                SELECT ss."DREAMS ID No", ss."DREAMS ID No",CAST(SUBSTRING(ss."DREAMS ID No",14) AS INT) AS ID_NO,  
                ss."Last Name" , ss."First Name" ,ss."Sim Card Number" ,ss."Sim Card Number" ,
                ss."Number of stepping stones sessions attended" AS NO_SS,
                ss."Current Age" ,ss."Address Village" ,ss."Address Parish",ss."Number of stepping stones sessions attended",
                ss."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
                ss."Education Status" AS IN_SCHOOL,ss."Name of school" AS SCH,                                          
                ss."Group Name" AS GROUP_NAME from stepping_stones ss order by GROUP_NAME,  ID_NO;
                ''')


rows_results_stones = results_stones.fetchall()
col_names_results_stones = [col for col in results_stones.keys()]

# print(col_names_results_stones)

# print(rows_results_stones)

numpy_data = np.array(rows_results_stones)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_stones)

df.to_excel("output/data_results_stones.xlsx",index=False)




results_ses = conn.execute('''
                    SELECT s."DREAMS ID No",CAST(SUBSTRING(s."DREAMS ID No",14) AS INT) AS ID_NO,  
                    s."Last Name" , s."First Name" ,
                    s."Current Age" ,
                    s."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
                    s."Education Status" AS IN_SCHOOL,s."DREAMS_SES Service" AS SES_TYPE
                    from ses s order by IN_SCHOOL, SES_TYPE,  ID_NO;
                ''')




rows_results_ses = results_ses.fetchall()
col_names_results_ses = [col for col in results_ses.keys()]

# print(col_names_results_ses)

# print(rows_results_ses)

numpy_data = np.array(rows_results_ses)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_ses)

df.to_excel("output/data_results_ses.xlsx",index=False)

















