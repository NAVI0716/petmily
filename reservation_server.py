from flask import Flask, request, make_response, jsonify
import requests
import os
import pymysql
app = Flask(__name__, static_url_path='/', static_folder='build')

@app.route('/reserve', methods=['GET','POST'])
def insert_data():
    params = request.json
    

    ###--- db에 저장
    # db = pymysql.connect(host='localhost', port=3306, user='root', passwd='48615+', db='petmily_db', charset='utf8')
    # c1=db.cursor()
    # query = "insert into reservation (HospitalID, Customer_name, Customer_number, AnimalType, Symptom, Time) values (%s,%s,%s,%s,%s,%s)"    
    # c1.execute(query)
    # db.commit()
    # db.close()
