import pymysql
import pandas as pd


###--- 받은 데이터 mysql에 저장

def reservation_save(HospitalID, Customer_name, Customer_number, AnimalType, Symptom, Time):
    hostname = 'localhost'
    portnum = 3306
    pswd = '48615+'
    conn = pymysql.connect(host = hostname, port = portnum, user='root',password=pswd,db='petmily_db',charset='utf8')
    curs = conn.cursor()
    sql = "insert into reservation (Hospital_ID, Customer_name, Customer_number, AnimalType, Symptom, Time) values (%s,%s,%s,%s,%s,%s)"
    curs.execute(sql, (HospitalID, Customer_name, Customer_number, AnimalType, Symptom, Time))
    conn.commit()
    conn.close()



###---- mysql table=>csv, dataframe으로 불러오기
# query = "SELECT * FROM hospital_info"
# result = pd.read_sql(query,db)

# result.to_csv("test.csv",encoding="cp949")

###---- mysql table 리스트튜플로 불러오기
# cur = db.cursor()
# query = "SELECT * FROM hospital_info"
# cur.execute(query)
# datas = cur.fetchone()
# print(dict(datas))
# db.commit()
# test=[dict(datas)]
# print(test[:5])
