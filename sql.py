import pymysql
import csv
import pandas as pd

hostname = 'localhost'
portnum = 3306
pswd = '48615+'

###petraschu
conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into hospital_info (HospitalID, name, contract, is24, isBeautyParlor, isHotel, isStore, hasParkingLot, businessHours, latitude, longitude, address, subject, species) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
f = open('./dataset/petraschu.csv','r',encoding='cp949')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13]))
conn.commit()
conn.close()
f.close()

###disease_info
conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into disease_info (Disease_name, Species, Definition, Main_Symptom) values (%s,%s,%s,%s)"
f = open('./dataset/질병정보v3.csv','r',encoding='cp949')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2],line[3]))
conn.commit()
conn.close()
f.close()

###symptom
conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into symptom (Symptom_code, Sorted_Symptom_kor, Sorted_Symptom_eng, Symptom_code_list, Symptom_name) values (%s,%s,%s,%s,%s)"
f = open('./dataset/동물질병 증상분류.csv','r',encoding='cp949')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2],line[3],line[4]))
conn.commit()
conn.close()
f.close()

###gu_info
conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into gu_info (gu, Hospital, Is24) values (%s,%s,%s)"
f = open('./dataset/gu_counts.csv','r',encoding='cp949')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2]))
conn.commit()
conn.close()
f.close()

###start_end
conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
curs = conn.cursor()
sql = "insert into gu_info (name, mon_start, tue_start, wed_start, thu_start, fri_start, sat_start, sun_start, hol_start, mon_end, tue_end, wed_end, thu_end, fri_end, sat_end, sun_end, hol_end, businessHours) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
f = open('./dataset/start_end.csv','r',encoding='cp949')
rd = csv.reader(f)
next(rd)
for line in rd:
    curs.execute(sql, (line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9],line[10],line[11],line[12],line[13],line[14],line[15],line[16],line[17],line[18]))
conn.commit()
conn.close()
f.close()