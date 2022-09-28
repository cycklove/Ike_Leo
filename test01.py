import pymssql
import pymysql
import pymongo
import time
import bson
import json


def get_version():
    conn = pymssql.connect("192.168.1.12", "sa", "chinaY999", "a8v5", "utf8")
    #conn = pymssql.connect("192.168.10.84", "sa", "AAAaaa123", "cb", "utf8")

    curs = conn.cursor()
    data = curs.execute("SELECT @@VERSION");
    data = curs.fetchone()

    jg = data[0]
    jg1 = jg[26:28]

    if jg1 == 'R2':
        result = jg[21:28]
    else:
        result = data[0].split(' ')[3]

    print(result)

def check_mongodb():
        host = '192.168.1.234'
        port = '27017'
        user = 'jk'
        passwd = 'AAAaaa123'
        server_id ='1'
        tags = 'mongo-scrm'

        # mysqldb = pymysql.connect("192.168.1.165", "ddqdbjk", "AAAaaa123", "ddqdbjk")
        # c = mysqldb.cursor()
        # c.execute("insert into mongodb_status_history SELECT *,LEFT(REPLACE(REPLACE(REPLACE(create_time,'-',''),' ',''),':',''),12) from mongodb_status where server_id=1")
        # c.execute("delete from mongodb_status where server_id=1")
        # mysqldb.commit()
        # c.close()
        # mysqldb.close()

         #connect = pymongo.Connection(host,int(port))
        client = pymongo.MongoClient(host, int(port))
        db = client['admin']
        db.authenticate(user,passwd)
        serverStatus=client.admin.command(bson.son.SON([('serverStatus', 1), ('repl', 2)]))
        time.sleep(1)
        serverStatus_2=client.admin.command(bson.son.SON([('serverStatus', 1), ('repl', 2)]))
        connect = 1
        ok = int(serverStatus['ok'])
        version = serverStatus['version']
        uptime = int(serverStatus['uptime'])
        connections_current = serverStatus['connections']['current']
        connections_available = serverStatus['connections']['available']
        globalLock_activeClients = serverStatus['globalLock']['activeClients']['total']
        globalLock_currentQueue = serverStatus['globalLock']['currentQueue']['total']
        mem_bits = serverStatus['mem']['bits']
        mem_resident = serverStatus['mem']['resident']
        mem_virtual = serverStatus['mem']['virtual']
        mem_supported = serverStatus['mem']['supported']
        #mem_mapped = serverStatus['mem']['mapped']
        #mem_mappedWithJournal = serverStatus['mem']['mappedWithJournal']
        network_bytesIn_persecond = int(serverStatus_2['network']['bytesIn']) - int(serverStatus['network']['bytesIn'])
        network_bytesOut_persecond = int(serverStatus_2['network']['bytesOut']) - int(serverStatus['network']['bytesOut'])
        network_numRequests_persecond = int(serverStatus_2['network']['numRequests']) - int(serverStatus['network']['numRequests'])
        opcounters_insert_persecond = int(serverStatus_2['opcounters']['insert']) - int(serverStatus['opcounters']['insert'])
        opcounters_query_persecond = int(serverStatus_2['opcounters']['query']) - int(serverStatus['opcounters']['query'])
        opcounters_update_persecond = int(serverStatus_2['opcounters']['update']) - int(serverStatus['opcounters']['update'])
        opcounters_delete_persecond = int(serverStatus_2['opcounters']['delete']) - int(serverStatus['opcounters']['delete'])
        opcounters_command_persecond = int(serverStatus_2['opcounters']['command']) - int(serverStatus['opcounters']['command'])

        try:
            repl = serverStatus['repl']
            setName = repl['setName']
            replset = 1
            if repl['secondary'] == True:
                repl_role = 'secondary'
                repl_role_new = 's'
            else:
                repl_role = 'master'
                repl_role_new = 'm'
        except:
            replset = 0
            repl_role = 'master'
            repl_role_new = 'm'
            pass

        print(server_id,host,port,tags,connect,replset,repl_role,ok,uptime,version,connections_current,connections_available,globalLock_currentQueue,
              globalLock_activeClients,mem_bits,mem_resident,mem_virtual,mem_supported,network_bytesIn_persecond,network_bytesOut_persecond,
              network_numRequests_persecond,opcounters_insert_persecond,opcounters_query_persecond,opcounters_update_persecond,
              opcounters_delete_persecond,opcounters_command_persecond)

        print(serverStatus)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def zj(self):#当前zj方法中的self，就是外部的那个对象p，如果我再定义了一个对象p2，那么p2调用zj时，zj中的self就表示p2这个对象。正所谓：谁调用，就表示谁
        print("我叫%s，今年%s岁" % (self.name, self.age))

if __name__ == '__main__':
    # get_version()
    #     # check_mongodb()
    p = Person('ike','100')
    p.zj()

    # list_a = ['龚海明', '营销中心', '菜子王事业部', 'asfaf', '凉山州', '07', '区域经理', '中级', 'safasf', '菜子王区域经理', '2021', '菜子王', '1', '1', None, None, None, None]
    # while None in list_a:
    #     list_a.remove(None)
    # print(list_a)
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,'*',j, '=',i*j,end=" ")
        print()