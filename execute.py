from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap

import mysql.connector as sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
   return render_template('home.htm')

@app.route('/makeapp')
def new_student():
   return render_template('makeapp.htm')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   msg = "test"
   if request.method == 'POST':
      try:
         lc = request.form['lc']
         cn = request.form['cn']
         ct = request.form['ct']
         cp = request.form['cp']
         ad = request.form['ad']
         
         with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO appointments (LicPlate, CusName, CarType, CusPhone, AppDate) VALUES ('{0}','{1}','{2}','{3}','{4}')".format(lc,cn,ct,cp,ad)
            cur.execute(cmd)
            
            con.commit()
            msg = "Appointment made successfully"
      except:
         con.rollback()
         msg = "Apointment failed"
         
      finally:
         return render_template("result.htm",msg = msg)
         con.close()

@app.route('/listapps')
def info():
   with sql.connect(host="localhost", user="flask", password="ubuntu", database="flask_db") as conn:  
      cur = conn.cursor()
      cur.execute("select * from appointments")
      rows = cur.fetchall()

   return render_template("listapps.htm",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
