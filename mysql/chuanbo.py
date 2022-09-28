import random  # 导入requests库
import time,datetime
import csv  # 导出为csv文档
import requests
from fake_useragent import UserAgent  # 导入随机获取UA的库


class ShipxySpider(object):
    def __init__(self):
        # 船讯网系统主页，用来获得cookie
        self.main_url = 'https://www.shipxy.com/'
        # 获取船舶MMSI的url
        self.mmsi_url = 'https://www.shipxy.com/Advert/JinGangJingShips'
        # 获取船舶数据的url
        self.data_url = 'https://www.shipxy.com/ship/GetShip'
        # 随机生成一个谷歌浏览器的UA
        self.ua = UserAgent()
        # 定义header
        self.header = {'User-Agent': self.ua.chrome}

    # 获取船舶数据
    def getData(self):
        session = requests.Session()
        session.get(self.main_url, headers=self.header)
        # 获取船舶的MMSI
        mmsi_res = session.post(self.mmsi_url, headers=self.header)
        #MMSI = mmsi_res.json()['data']
        MMSI = ['413835888','413765597']
        # 根据MMSI获取船舶的数据
        alldata = []
        for mmsi in MMSI:
            data = {"mmsi": mmsi}
            data_res = session.post(self.data_url, headers=self.header, data=data)
            #print(data_res.json())
            l = data_res.json()['data']
            kv = eval(str(l))
            dict_result = {}
            for _ in kv:
                for k, v in _.items():
                    dict_result[k] = v
                print(dict_result)
                mmsi = dict_result['mmsi']
                imo = dict_result['imo']
                type = dict_result['type']
                if type == 50:
                    cblx = '引航船'
                elif type == 51:
                    cblx = '搜救船'
                elif type == 52:
                    cblx = '拖轮'
                elif type == 53:
                    cblx = '港口供应船'
                elif type == 54:
                    cblx = '载有防污染装置和设备的船舶'
                elif type == 55:
                    cblx = '执法艇'
                elif type == 56:
                    cblx = '备用-用于当地船舶的任务分配'
                elif type == 57:
                    cblx = '备用-用于当地船舶的任务分配'
                elif type == 58:
                    cblx = '医疗船'
                elif type == 59:
                    cblx = '符合18号决议Mob-83的船舶 '
                elif type == 30:
                    cblx = '捕捞'
                elif type == 31:
                    cblx = '拖引'
                elif type == 32:
                    cblx = '拖引并且船长>200m或船宽>25m'
                elif type == 33:
                    cblx = '疏浚或水下作业'
                elif type == 34:
                    cblx = '潜水作业'
                elif type == 35:
                    cblx = '参与军事行动'
                elif type == 36:
                    cblx = '帆船航行'
                elif type == 37:
                    cblx = '娱乐船'
                elif type >=20 and type <=29:
                    cblx = '地效应船'
                elif type >=40 and type <=49:
                    cblx = '高速船'
                elif type >=60 and type <=69:
                    cblx = '客船'
                elif type >=70 and type <=79:
                    cblx = '货船'
                elif type >=80 and type <=89:
                    cblx = '油轮'
                elif type >=90 and type <=99:
                    cblx = '其他类型的船舶'
                elif type == 100:
                    cblx = '集装箱'
                else:
                    cblx = '其它'

                tradetype = dict_result['tradetype']
                if tradetype == 1:
                    tradetype = '内贸'
                elif tradetype == 2:
                    tradetype = '外贸'
                else:
                    tradetype = '其它'
                name = dict_result['name']
                cnname = dict_result['cnname']
                callsign = dict_result['callsign']
                length = dict_result['length']
                length = '%s米' % int(length / 10)
                width = dict_result['width']
                width = '%s米' % int(width / 10)
                left = dict_result['left']
                trail = dict_result['trail']
                draught = dict_result['draught']
                draught = '%s米' % float(draught / 1000)
                dest = dict_result['dest']
                eta = dict_result['eta']
                nf = datetime.datetime.today().year
                eta = str(nf)+"-"+eta+":00"
                navistatus = dict_result['navistatus']
                lat = dict_result['lat']
                if lat > 0:
                    lat = '{} N'.format(int(lat) / 1000000)
                else:
                    lat = '{} S'.format(abs(int(lat) / 1000000))
                lon = dict_result['lon']
                if lon > 0:
                    lon = '{} E'.format(int(lon) / 1000000)
                else:
                    lon = '{} W'.format(abs(int(lon) / 1000000))
                hdg = dict_result['hdg']
                cog = dict_result['cog']
                sog = dict_result['sog']
                sog = round(sog / 1000 * 1.852, 2)
                rot = dict_result['rot']
                navistatus = dict_result['navistatus']
                if navistatus == 0:
                    navistatus="在航(主机推动)"
                elif navistatus == 1:
                    navistatus = "锚泊"
                elif navistatus == 2:
                    navistatus = "失控"
                elif navistatus == 3:
                    navistatus = "操纵受限"
                elif navistatus == 4:
                    navistatus = "吃水受限"
                elif navistatus == 5:
                    navistatus = "靠泊"
                elif navistatus == 6:
                    navistatus = "搁浅"
                elif navistatus == 7:
                    navistatus = "捕捞作业"
                elif navistatus == 8:
                    navistatus = "靠帆船提供动力"
                else:
                    navistatus = "未知"

                lastdyn = dict_result['lastdyn']
                lastsj = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(lastdyn))
                print("\n", "船舶ID:", mmsi, "\n","船名:", name, "\n","贸易类型:", tradetype,"\n", "中文船名:", cnname,"\n",
                      "船舶类型:",cblx,"\n","航行状态:",navistatus,"\n", "预到时间:",eta,"\n",
                      "船长:", length, "\n", "船宽:", width, "\n", "吃水:", draught, "\n", "目的地:", dest, "\n",
                      "纬度:", lat, "\n", "经度:", lon, "\n", "航速:", sog, "\n", "最新船位时间:", lastsj, "\n", )

            alldata.append(data_res.json()['data'])
        session.close()
        return alldata

    # 把爬取的数据保存到本地
    # def saveData(self, filename):
    #     with open(filename, mode='w', newline='') as csv_file:
    #         # 构建字段名称，也就是key
    #         fieldnames = ['mmsi', 'lat', 'lon', 'tradetype', 'callsign', 'hdg', 'trail', 'laststa', 'lastdyn', 'imo',
    #                       'satelliteutc', 'type', 'left', 'length', 'matchtype', 'draught', 'dest', 'width', 'name',
    #                       'cog', 'rot', 'navistatus', 'cnname', 'source', 'sog', 'eta', 'shipid']
    #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #         # 写入字段名，当做表头
    #         writer.writeheader()
    #         for item in self.getData():
    #             # 多行写入
    #             writer.writerows(item)

    # 入口函数
    def run(self):
        # self.saveData('data.csv')
        self.getData()
        # 每爬取一个页面随机休眠1-2秒钟的时间
        time.sleep(random.randint(1, 2))


# 主函数，用来控制整体逻辑
if __name__ == '__main__':
    # 程序开始运行时间
    start = time.time()
    # 实例化一个对象spider
    spider = ShipxySpider()
    # 调用入口函数
    spider.run()
    end = time.time()
    # 爬虫执行时间
    print('执行时间:%.2f' % (end - start))