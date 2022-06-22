import pymysql as mq
conn=mq.connect(host='localhost',
                user='root',
                password='',
                database="mailani"
                )
mysqlc=conn.cursor()
#(Table student (st_id,st_name,st_class,st_email)
tc="create table employee(emp_id INT primary key auto_increment,emp_name varchar(50),emp_post varchar(20),emp_email varchar(50))"

mysqlc.execute(tc)



