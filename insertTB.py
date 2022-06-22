import pymysql as mq
mysql=mq.connect(host="localhost",
                user="root",
                password="",
                database="ml_users"
                )
mycursor=mysql.cursor()
try:
    #emp_id,emp_name,emp_post,emp_email
    ins="INSERT INTO employee(emp_name,emp_post,emp_email) values(%s,%s,%s)"
    t=[("sachin",'engineer1','sachin@gmail.com'),("vaibhav","senior engineer","vaibhav@gmail.com"),("mahesh","team lead","mahesh@gmail.com"),("rahul","engineer","rahul@gmail.com")]
    mycursor.executemany(ins,t)
    mysql.commit();
    print("insert data")
except:
    print("error..")
