import datetime,time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import json
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler


def connect_DBS(content,ip,zh,mm,dbase):
    db = pymysql.connect(host=ip, user=zh, password=mm, database=dbase)
    cursor = db.cursor()
    cursor.execute(content)
    db.commit()
    cursor.close()
    db.close()

def getjwd(lat,lng):
    ak = "Kige1SOvcLoH5rSBzysWAt5z4AtHarR1"  # 百度地图个人开发应用所属的ak
    baiduUrl = "https://api.map.baidu.com/reverse_geocoding/v3/?ak=%s&output=json&coordtype=wgs84ll&location=%s,%s" % (ak, lat, lng)
    req = requests.get(baiduUrl)
    content = req.text
    # 将content读取到的内容存入名为baiduAddr的字典中
    baiduAddr = json.loads(content)
    # 调用字典的相应内容，存到内存的变量中
    province = baiduAddr["result"]["addressComponent"]["province"]
    city = baiduAddr["result"]["addressComponent"]["city"]
    district = baiduAddr["result"]["addressComponent"]["district"]

    fulladdr = {'province':province,'city':city,'district':district}

    return fulladdr

def tshifleet(mmsi):
    ts = time.time()
    url = "https://www.hifleet.com/"
    ua = UserAgent()
    header = {'User-Agent': ua.chrome}
    session = requests.Session()
    aa = session.get(url, headers=header)
    data_url = "https://www.hifleet.com/hifleetapi/queryMyFleetsShips.do?timestamp=%s&dataType=json"%ts
    mmsi = mmsi
    data = {"mmsis": mmsi
            }
    data_res = session.post(data_url, headers=header, data=data)
    ll = data_res.json()
    return ll

def tszggkw():
    ts = int(round(time.time() * 1000))
    url = "http://ship.chinaports.com/"
    ua = UserAgent()
    header = {'User-Agent': ua.chrome}
    session = requests.Session()
    aa = session.get(url, headers=header)
    data_url ="http://ship.chinaports.com/ShipInit/shipInfo"
    mmsi = [413765597,413860442,413835888,413866432,413832267,413794396]
    for i in mmsi:
        data = {"userid": i,
                "source": 0,
               "num": ts,
                "encode": 'false',
                "lang": 'ZH',
                "zone": -480}
        data_res = session.post(data_url, headers=header, data=data)
        soup = BeautifulSoup(data_res.content, "html.parser")
        #print(soup)
        shipid = soup.mmsi.string
        shiptype = soup.shiptype.string
        if shiptype != None:
            shiptype = int(shiptype)
            if shiptype == 50:
                cblx = '引航船'
            elif shiptype == 51:
                cblx = '搜救船'
            elif shiptype == 52:
                cblx = '拖轮'
            elif shiptype == 53:
                cblx = '港口供应船'
            elif shiptype == 54:
                cblx = '载有防污染装置和设备的船舶'
            elif shiptype == 55:
                cblx = '执法艇'
            elif shiptype == 56:
                cblx = '备用-用于当地船舶的任务分配'
            elif shiptype == 57:
                cblx = '备用-用于当地船舶的任务分配'
            elif shiptype == 58:
                cblx = '医疗船'
            elif shiptype == 59:
                cblx = '符合18号决议Mob-83的船舶 '
            elif shiptype == 30:
                cblx = '捕捞'
            elif shiptype == 31:
                cblx = '拖引'
            elif shiptype == 32:
                cblx = '拖引并且船长>200m或船宽>25m'
            elif shiptype == 33:
                cblx = '疏浚或水下作业'
            elif shiptype == 34:
                cblx = '潜水作业'
            elif shiptype == 35:
                cblx = '参与军事行动'
            elif shiptype == 36:
                cblx = '帆船航行'
            elif shiptype == 37:
                cblx = '娱乐船'
            elif shiptype >= 20 and shiptype <= 29:
                cblx = '地效应船'
            elif shiptype >= 40 and shiptype <= 49:
                cblx = '高速船'
            elif shiptype >= 60 and shiptype <= 69:
                cblx = '客船'
            elif shiptype >= 70 and shiptype <= 79:
                cblx = '货船'
            elif shiptype >= 80 and shiptype <= 89:
                cblx = '油轮'
            elif shiptype >= 90 and shiptype <= 99:
                cblx = '其他类型的船舶'
            elif shiptype == 100:
                cblx = '集装箱'
        else:
            cblx = '其它'
        length = soup.length.string
        width = soup.width.string
        name = soup.shipname.string
        eta_std = soup.eta.string
        nf = datetime.datetime.today().year
        eta_std = str(nf) + "-" + eta_std + ":00"
        draught = soup.draught.string
        latitude = soup.latitude.string
        longitude = soup.longitude.string
        destination = soup.destination.string
        sog = soup.sog.string
        sog = round(float(sog),2)
        lastsj = soup.timestamp.string
        lastsj = lastsj.replace('(UTC+8)','')

        jgfleet = tshifleet(i)['data']
        kv = eval(str(jgfleet))
        dict_result = {}
        for _ in kv:
            for k, v in _.items():
                dict_result[k] = v
        print(dict_result)
        dn = dict_result['dn']
        dm = dict_result['dm']
        type = dict_result['type']
        cblength = dict_result['length']
        cblength = int(cblength)
        cbwidth = dict_result['width']
        cbwidth = int(cbwidth)
        cbdraught = dict_result['draught']
        cbdest = dict_result['destination']
        lat = dict_result['lat']
        if float(lat) > 0:
            latgsh = 'N {}'.format(round(float(lat) / 60, 6))
        else:
            latgsh = 'S {}'.format(round(abs(float(lat) / 60), 6))
        lon = dict_result['lon']
        if float(lon) > 0:
            longsh = 'E {}'.format(round(float(lon) / 60, 6))
        else:
            longsh = 'W {}'.format(round(abs(float(lon) / 60), 6))

        lat = round(float(lat) / 60, 6)
        lon = round(float(lon) / 60, 6)
        jwd = getjwd(lat,lon)
        province = jwd['province']
        city = jwd['city']
        district = jwd['district']
        fulladdr = province+city+district
        print(province,city,district)


        print("\n", "船舶ID:", shipid, "\n", "船名:", name, "\n", "中文船名:", dm, "\n","国籍:", dn, "\n",
              "船舶类型:", type, "\n", "船长:", cblength, "\n",
              "船宽:", cbwidth, "\n", "吃水:", cbdraught, "\n", "目的地:", destination, "\n", "目的地2:", cbdest, "\n","预到时间:", eta_std, "\n",
              "纬度:", latgsh, "\n", "经度:", longsh, "\n","纬度2:", latitude, "\n", "经度2:", longitude, "\n","当前位置:",fulladdr,"\n",
              "航速:", sog, "\n", "最新船位时间:", lastsj, "\n", )

        getsj = datetime.datetime.now()
        ip = "192.168.1.94"
        user = "root"
        psword = "AAAaaa123"
        dbase = "getdata"
        istsql = "insert into get_shipstatus(shipid,shipname,shipdm,shipdn,shiptype,shiplength,shipwidth,draught,destination,eta_std,lat,lon,province,city,district,fulladdr,sog,lastsj,synctime) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (shipid,name,dm,dn,type,cblength,cbwidth,cbdraught,destination,eta_std,latgsh,longsh,province,city,district,fulladdr,sog,lastsj,getsj)
        connect_DBS(content=istsql,ip=ip,zh=user,mm=psword,dbase=dbase)

if __name__=="__main__":
    # sched = BlockingScheduler()
    # # 每5分钟触发
    # sched.add_job(tszggkw, 'interval', minutes=5)
    # sched.start()
    start = time.time()
    tszggkw()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
