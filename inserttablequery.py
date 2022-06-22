import pymysql as mq
# Server Name-> localhost
# username-> root
# password-> ''
myobj=mq.connect("localhost","root","")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("database created")

except:
    print("database error..")




