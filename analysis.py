from app import rows_results_stones, rows_results_ses,conn,np,col_names_results_ses,pd,col_names_results_stones

stones = []
ses = []

ses_asset = []

result_ses_asset = conn.execute('''
            SELECT s."DREAMS ID No",CAST(SUBSTRING(s."DREAMS ID No",14) AS INT) AS ID_NO,  
            s."Last Name" , s."First Name" ,
            s."Current Age" ,s."Asset financing training start date" ,s."Asset financing training end date" ,
            s."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
            s."Education Status" AS IN_SCHOOL,s."DREAMS_SES Service" AS SES_TYPE
            from ses s WHERE "DREAMS_SES Service" = "Asset Financing" order by IN_SCHOOL, SES_TYPE,  ID_NO;
            ''')
rows_all_asset_girls = result_ses_asset.fetchall()
rows_all_asset_girls_columnnames = [col for col in result_ses_asset.keys()]



for v in rows_all_asset_girls:
    ses_asset.append(v['ID_NO'])

for v in rows_results_stones:
    stones.append(v['ID_NO'])

for v in rows_results_ses:
    ses.append(v['ID_NO'])

no_stones_in_ses= []
for i in ses:
    if i not in stones:
        
        results_ses_id = conn.execute(f'''
                    SELECT s."DREAMS ID No",CAST(SUBSTRING(s."DREAMS ID No",14) AS INT) AS ID_NO,  
                    s."Last Name" , s."First Name" ,
                    s."Current Age" ,
                    s."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
                    s."Education Status" AS IN_SCHOOL,s."DREAMS_SES Service" AS SES_TYPE
                    from ses s WHERE "DREAMS_SES Service" = "Asset Financing" 
                    AND ID_NO = {i} order by IN_SCHOOL, SES_TYPE,  ID_NO;
                ''')

        for j in results_ses_id.all():
           no_stones_in_ses.append(j) 

numpy_data = np.array(no_stones_in_ses)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_ses)

df.to_excel("output/data_results_no_stones_in_asset_fin_ses.xlsx",index=False)


# print(no_stones_in_ses)

no_ses_in_stone= []
no_ses_in_stone_taken= []
for i in stones:
    if i not in ses_asset:
        
        results_stones_id = conn.execute(f'''
                    SELECT ss."DREAMS ID No", ss."DREAMS ID No",CAST(SUBSTRING(ss."DREAMS ID No",14) AS INT) AS ID_NO,  
                    ss."Last Name" , ss."First Name" ,ss."Sim Card Number" ,ss."Sim Card Number" ,
                    ss."Number of stepping stones sessions attended" AS NO_SS,
                    ss."Current Age" ,ss."Address Village" ,ss."Address Parish",ss."Number of stepping stones sessions attended",
                    ss."Age at entry (must be whole number e.g 10, 14, 17)" AS AGE_ENTRY,
                    ss."Education Status" AS IN_SCHOOL,ss."Name of school" AS SCH,
                    ss."Group Name" AS GROUP_NAME from stepping_stones ss WHERE ID_NO = {i}  order by GROUP_NAME,  ID_NO
                ''')
        no_ses_in_stone_taken.append(i)

        for j in results_stones_id.all():
           no_ses_in_stone.append(j) 




numpy_data = np.array(no_ses_in_stone)

df = pd.DataFrame(data= numpy_data, columns=col_names_results_stones)

df.to_excel("output/data_results_no_ses_in_stone.xlsx",index=False)



sql = """
with condoms_as_ss AS (SELECT *
FROM condoms c 
INNER JOIN stepping_stones ss ON c."DREAMS ID No" = ss."DREAMS ID No") 
SELECT cas."Event date",cas."Date of Birth" , cas."Group Name" as GRP,cas."Address Village",cas."Address Parish" ,cas."Distribution Point"
FROM condoms_as_ss as cas order by cas."Event date",GRP ASC;
"""



