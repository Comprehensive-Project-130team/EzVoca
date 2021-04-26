import pymysql

conn = pymysql.connect(host="localhost", user="root", password="12345", db="testdb", charset="utf8")
curs = conn.cursor()
sql = "select * from members"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

conn.close()