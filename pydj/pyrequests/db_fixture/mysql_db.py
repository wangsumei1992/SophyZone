import pymysql.cursors
import os
<<<<<<< HEAD
import ConfigParser as cparser

#======== Reading db_config.ini setting ===========
'''
=======
import configparser as cparser

#======== Reading db_config.ini setting ===========
>>>>>>> a05751e3bc37e838995c10523bab43aabcfef2cd
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
#base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")
<<<<<<< HEAD
'''
# ======== MySql base operating ===================
class DB(object):
=======

# ======== MySql base operating ===================
class DB:
>>>>>>> a05751e3bc37e838995c10523bab43aabcfef2cd

    def __init__(self):
        try:
            #connect to the database
<<<<<<< HEAD
            self.connection = pymysql.connect(host='127.0.0.1',
                                              user='root',
                                              password='12345678',
                                              db='pyguest',
                                              port=3306,
=======
            self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=db,
>>>>>>> a05751e3bc37e838995c10523bab43aabcfef2cd
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
<<<<<<< HEAD
        real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value + ")"
        print(real_sql)
=======
        real_sql = "INSERT INTO" + table_name + "(" + key + ") VALUES (" + value + ")"

>>>>>>> a05751e3bc37e838995c10523bab43aabcfef2cd
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

        def close(self):
            self.connection.close()

<<<<<<< HEAD
if __name__ == '__main__':
=======
if __main__ == '__main__':
>>>>>>> a05751e3bc37e838995c10523bab43aabcfef2cd

    db = DB()
    table_name = "sign_event"
    data = {'id':1,'name':'xiaomi','limit':2000,'status':1,'address':'beijing','start_time':'2018-04-30 12:30:00'}
    table_name2 = "sign_guest"
    data2 = {'realname':'wangsumei','phone':12121212123,'email':'wangsumei@mail.com','sign':0,'event_id':1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()





