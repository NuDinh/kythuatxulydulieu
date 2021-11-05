
import json
import psycopg2

with psycopg2.connect(database = 'weatherdb', user = 'postgres', 
password = 'password', port = '5432') as conn:
    with conn.cursor() as cur:
        with open('config/vn_list_eng.json','r') as my_file: #config/vn_list.json
            data = json.load(my_file)
            cur.execute("""CREATE TABLE IF NOT EXISTS weather_city_dim
            (
            id	VARCHAR PRIMARY KEY ,
            name	VARCHAR(50) 	,	
            state	VARCHAR(50) 	,
            country VARCHAR(50) 	,	
            coord json		
                ) """)
            query_sql = """ insert into weather_city_dim
                select * from json_populate_recordset(NULL::weather_city_dim, %s) """
            # print(json.dumps(data))

            cur.execute(query_sql, (json.dumps(data),))

            

# import pandas as pd
# df = pd.read_json(r"D:\MASTER\HK3\Ky thuat xu ly du lieu\kythuatxulydulieu\weather\config\vn_list.json")
# print(df)
# df.to_excel (r"D:\MASTER\HK3\Ky thuat xu ly du lieu\kythuatxulydulieu\weather\config\vn_list_1.xls", index = None, encoding= 'UTF8')