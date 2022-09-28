import itchat
import datetime,time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import xml.dom.minidom
import urllib
import json
import demjson
import jsonpath
import wxauto
import xmltodict

#获取金山词霸每日一句
def get_new():
    url="http://open.iciba.com/dsapi"
    r=requests.get(url)
    contents=r.json()['content']
    note=r.json()['note']
    print(r.json())
    return contents,note

def tshifleet(mmsi):
    ts = time.time()
    # url = "https://www.hifleet.com/hifleetapi/queryMyFleetsShips.do?timestamp=%s&dataType=json&mmsis=413835888"%ts
    # ua = UserAgent()
    # header = {'User-Agent': ua.chrome}
    # session = requests.Session()
    # aa = session.get(url, headers=header)
    # l = aa.json()['data']
    # ll = aa.json()['timestamp']
    # lastsj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
    # print(l,"\n",ll,ts,"\n",lastsj)

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

def tscdt():
    ts = time.time()
    # url = "http://www.shipdt.com/lvservice/ship/getUnFocusShipDataNew?shipmmsi=413765597&aisstatu=1&cookievalue=CdKXhDsB60MSOyGJAloL%2FQ%3D%3D"
    url = "http://www.shipdt.com/"
    ua = UserAgent()
    header = {'User-Agent': ua.chrome}
    session = requests.Session()
    aa = session.get(url, headers=header)
    cookiejar = aa.cookies
    print(cookiejar)
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    getckie = cookiedict['JSESSIONID']
    print(getckie)

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
        lastsj = soup.timestamp.string

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
        lat = dict_result['lat']
        if float(lat) > 0:
            lat = 'N {}'.format(round(float(lat) / 60, 6))
        else:
            lat = 'S {}'.format(round(abs(float(lat) / 60), 6))
        lon = dict_result['lon']
        if float(lon) > 0:
            lon = 'E {}'.format(round(float(lon) / 60, 6))
        else:
            lon = 'W {}'.format(round(abs(float(lon) / 60), 6))


        print("\n", "船舶ID:", shipid, "\n", "船名:", name, "\n", "中文船名:", dm, "\n","国籍:", dn, "\n",
              "船舶类型:", type, "\n", "船长:", cblength, "\n",
              "船宽:", cbwidth, "\n", "吃水:", cbdraught, "\n", "目的地:", destination, "\n", "预到时间:", eta_std, "\n",
              "纬度:", lat, "\n", "经度:", lon, "\n","纬度2:", latitude, "\n", "经度2:", longitude, "\n",
              "航速:", sog, "\n", "最新船位时间:", lastsj, "\n", )



def get_ship_cdt():
    k = 'a74f1881058a4a6c8d4bfda1e30f96fa'
    shipid = '413835888'
    url = "http://api.shipdt.com/DataApiServer/apicall/GetManyShip?k=%s&id=%s"%(k,shipid)
    r = requests.get(url)
    data = r.json()
    print(data)
    l = r.json()['data']
    kv = eval(str(l))

    dict_result = {}
    for _ in kv:
        for k, v in _.items():
            dict_result[k] = v

    ShipID = dict_result['ShipID']
    mmsi = dict_result['mmsi']
    imo = dict_result['imo']
    nationality = dict_result['nationality']
    name = dict_result['name']
    callsign = dict_result['callsign']
    shiptype = dict_result['shiptype']
    length = dict_result['length']
    length = '%s米'%int(length / 10)
    width = dict_result['width']
    width = '%s米'%int(width / 10)
    left = dict_result['left']
    trail = dict_result['trail']
    draught = dict_result['draught']
    draught = '%s米'%int(draught / 1000)
    dest = dict_result['dest']
    dest_std = dict_result['dest_std']
    destcode = dict_result['destcode']
    eta = dict_result['eta']
    eta_std = dict_result['eta_std']
    navistat = dict_result['navistat']
    lat = dict_result['lat']
    if lat > 0:
        lat = 'N {}'.format(int(lat) / 1000000)
    else:
        lat = 'S {}'.format(abs(int(lat) / 1000000))
    lon = dict_result['lon']
    if lon > 0:
        lon = 'E {}'.format(int(lon) / 1000000)
    else:
        lon = 'W {}'.format(abs(int(lon) / 1000000))
    hdg = dict_result['hdg']
    cog = dict_result['cog']
    sog = dict_result['sog']
    sog = round(sog / 1000 * 1.852,2)
    rot = dict_result['rot']
    lasttime = dict_result['lasttime']
    lastsj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(lasttime))
    print("\n","船舶ID:",shipid,"\n","船国籍:",nationality,"\n","船名:",name,"\n",
          "船舶类型:",shiptype,"\n","船长:",length,"\n",
          "船宽:", width, "\n", "吃水:", draught, "\n", "目的地:", dest, "\n", "预到时间:",eta_std,"\n",
          "纬度:", lat, "\n", "经度:", lon, "\n", "航速:", sog, "\n", "最新船位时间:", lastsj, "\n",)


def get_ship_hifleet():
    usertoken = 'RKAMoBc/J+dwj4UU1yPYZQUQCGID/iStnch6q/1e6VkWg2kYalxMGc5EP0sNG54T'
    mmsi = '413765597'
    url = "https://api.hifleet.com/position/position/get/token?mmsi=%s&usertoken=%s"%(mmsi,usertoken)
    r = requests.get(url)
    data = r.json()
    #print(data)
    l = r.json()['list']
    kv = eval(str(l))
    print(kv)
    m = kv['m']
    n = kv['n']
    sp = kv['sp']
    co = kv['co']
    ti = kv['ti']
    la = kv['la']
    if float(la) > 0:
        la = 'N {}'.format(round(float(la) / 60,6))
    else:
        la = 'S {}'.format(round(abs(float(la) / 60),6))
    lo = kv['lo']
    if float(lo) > 0:
        lo = 'E {}'.format(round(float(lo) / 60,6))
    else:
        lo = 'W {}'.format(round(abs(float(lo) / 60),6))
    h = kv['h']
    draught = kv['draught']
    eta = kv['eta']
    destination = kv['destination']
    callsign = kv['callsign']
    type = kv['type']
    buildyear = kv['buildyear']
    dwt = kv['dwt']
    fn = kv['fn']
    dn = kv['dn']
    an = kv['an']
    l = kv['l']
    w = kv['w']
    rot = kv['rot']
    status = kv['status']

    print("\n", "船舶ID:", m, "\n", "船国籍:", dn, "\n", "船名:", n, "\n",
          "船舶类型:", type, "\n", "船长:", l, "\n",
          "船宽:", w, "\n", "吃水:", draught, "\n", "目的地:", destination, "\n", "预到时间:", eta, "\n",
          "纬度:", la, "\n", "经度:", lo, "\n", "航速:", sp, "\n", "最新船位时间:", ti, "\n",
          "状态:", status)

def send_news():
    try:
        itchat.auto_login(hotReload=True)
        my_friend = itchat.search_friends(name=u'Leo')
        FriendName = my_friend[0]["UserName"]
        message1 = get_new()[0]
        # 因为会出现进程报错，所以我加上了 pass
        pass
        message2 = get_new[1]
        pass
        message3 = u"来自你的朋友"
        pass
        itchat.send(message1, toUserName=FriendName)
        itchat.send(message2, toUserName=FriendName)
        itchat.send(message3, toUserName=FriendName)
        # 每个1天发送消息
        t = time(86400, send_news())
        t.start()

    except:
        # 如果上面其中一条消息没有发送成功，就会发送本条消息
        message4 = u"你的朋友出bug了"
        itchat.send(message4,toUserName=FriendName)

def ttwx():
    itchat.auto_login()
    itchat.send('Hello, filehelper', toUserName='filehelper')

if __name__=="__main__":
    #a = get_new()
    #print(a)
    #get_ship_cdt()
    #get_ship_hifleet()
    #tshifleet()
    #tscdt()
    start = time.time()
    tszggkw()
    end = time.time()
    print('执行时间:%.2f' % (end - start))
