import pymysql as mq
# Server Name-> localhost
#Username-> root
#Password-> ""
myobj=mq.connect(host='localhost',
                user='root',
                password='',
                )
cursorobj=myobj.cursor()
try:
    db="create database ml_users"
    cursorobj.execute(db)
    print("database created")

except:
    print("database error..")






