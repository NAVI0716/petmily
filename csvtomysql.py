import pymysql
import csv
import pandas as pd


conn = pymysql.connect(host = 'localhost', user='root',password='48615+',db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into hospital_info (name, contract, is24, isBeautyParlor, isHotel, isStore, hasParkingLot, businessHours, latitude, longitude, address, subject, species) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
f = open('datalib/exampledata/petraschu.csv','r',encoding='utf-8')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12]))
conn.commit()
conn.close()
f.close()

# data = pd.read_csv('datalib/exampledata/petraschu.csv',encoding='utf-8')
# data = data.where(pd.notnull(data), None)
# engine = create_engine('mysql+mysqldb://root:48615+@host:3306/study_db',encoding='utf-8')
# conn = engine.connect()
# data.to_sql(name='petraschu_tb',con=engine,if_exists='append',index=False)

# db_connection_str = 'mysql+pymysql://[root]:[48615+]@[3306]/[study_db]'
# db_connection = create_engine(db_connection_str)
# conn = db_connection.connect()
# data.to_sql(name='petraschu_tb', con=db_connection, if_exists='append',index=False)  
