import pymysql as bb
mysql=bb.connect(host="localhost",
                 user="root",
                 password="",
                 database="ml_users")
cursorobj=mysql.cursor()
id=input("enter the emp_id= ")
sql="delete from employee where emp_id=%s"
try:
    cursorobj.execute(sql,id)
    mysql.commit()
    print("student deleted.")
except:
    print("error..")
