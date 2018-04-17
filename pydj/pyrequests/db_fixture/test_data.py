import sys
sys.path.append('./db_fixture')
from mysql_db import DB

#create data
datas = {
    'sign_event':[
        {'id':1,'name':'fullhouse','limit':2000,'status':1,'address':'shanghai101','start_time':'2017-10-10 14:00:00'},
        {'id':2,'name':'filling','limit':500,'status':1,'address':'beijing102','start_time':'2017-10-10 14:00:00'},
        {'id':3,'name':'nini','limit':400,'status':0,'address':'bjstation','start_time':'2018-10-10 14:00:00'},
        {'id':4,'name':'dibai','limit':100,'status':1,'address':'xixiyuan','start_time':'2017-10-10 14:00:00'},
        {'id':5,'name':'exhibition','limit':300,'status':1,'address':'habayuan','start_time':'2017-10-10 14:00:00'},
    ],
    'sign_guest':[
        {'id':1,'realname':'sgirl','phone':15811507610,'email':'silygirl@mail.com','sign':0,'event_id':1},
        {'id':2,'realname':'tom','phone':15811507611,'email':'tom@mail.com','sign':1,'event_id':1},
        {'id':3,'realname':'jim','phone':15811507612,'email':'jim@mail.com','sign':0,'event_id':5},
    ],
}
#Inster table datas
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()