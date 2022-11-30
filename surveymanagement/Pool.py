import pymysql as Mysql

def ConnectionPool():
    DB=Mysql.connect(host='localhost',port=3306,user='root',password='1234',database="surveymanagement",cursorclass=Mysql.cursors.DictCursor)
    CMD=DB.cursor()
    return DB,CMD