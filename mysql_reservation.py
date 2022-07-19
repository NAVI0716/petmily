import pymysql
import pandas as pd
from datalib import readhospital
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='48615+', db='petmily_db', charset='utf8')

###---- mysql table=>csv, dataframe으로 불러오기
query = "SELECT * FROM hospital_info"
result = pd.read_sql(query,db)

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
