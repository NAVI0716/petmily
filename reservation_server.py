from flask import Flask, make_response, jsonify, request
import requests
import os
import pymysql
app = Flask(__name__, static_url_path='/', static_folder='build')

@app.route('/reserve', methods=['GET','POST'])
def insert_data():
    if requset.method == 'GET':
        args_dict = request.args.to_dict()
    else:
        HospitalID = 33
        Customer_name = request.form["User_name"]
        Customer_number = request.form["User_PH"]
        AnimalType = request.form["dog"]
        Symptom = request.form["Symp"]
        Time = request.form["use_time"]
        # req_data = {
        #     HospitalID:33,
        #     Customer_name:request.form["User_name"],
        #     Customer_number:request.form["User_PH"],
        #     AnimalType:request.form["dog"],
        #     Symptom: request.form["Symp"],
        #     Time: request.form["use_time"]
        # }
    return 
    

    ###--- db에 저장
    # db = pymysql.connect(host='localhost', port=3306, user='root', passwd='48615+', db='petmily_db', charset='utf8')
    # c1=db.cursor()
    # query = "insert into reservation (HospitalID, Customer_name, Customer_number, AnimalType, Symptom, Time) values (%s,%s,%s,%s,%s,%s)"    
    # c1.execute(query)
    # db.commit()
    # db.close()
