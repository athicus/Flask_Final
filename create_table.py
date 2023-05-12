import mysql.connector as sql
conn = sql.connect(host="localhost",	user="flask",	password="ubuntu",	database="flask_db")
cur = conn.cursor()
cmd = "CREATE TABLE appointments (\
  LicPlate INT NOT NULL PRIMARY KEY,\
	CusName	VARCHAR(30) NOT	NULL, \
	CarType VARCHAR(15), \
	CusPhone VARCHAR(15), \
	AppDate DATE)"
cur.execute(cmd)
conn.close()
