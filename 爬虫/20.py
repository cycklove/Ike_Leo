'''
破解有道词典
'''
from urllib import request,parse
from chardet import detect
import time,random,hashlib,json

def getsalt():
    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getmd5(v):
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))

    sign = md5.hexdigest()

    return  sign

# 浏览器找到fanyi.min.js 查找sign里的公式
# 第一 四个参数是固定的字符串 第三个是salt 第二个是要输入查找的单词
def getsign(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getmd5(sign)
    return sign

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    salt = getsalt()

    data = {
        "i":key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult":"dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getsign(key,salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
        "typoResult": "false"
    }

    # print(data)

    # 参数data需要bytes格式
    data = parse.urlencode(data).encode()

    headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            #"Accept-Encoding": "gzip,deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": len(data),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=2115555114@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=2066718543.1368227; _ntes_nnid =74d0702d0e964b864c1f93d7fbc1c6a1,1552033992955; JSESSIONID=aaaQlM-Tb1gxn41rfDdYw; ___rl__test__cookies=1565573746957",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            #"X-Requested-With": "XMLHttpRequest"
    }

    req = request.Request(url = url,data = data,headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read()

    cs = detect(html)

    html = html.decode(cs.get("encoding","utf-8"))

    json_data = json.loads(html)

    test2 = {}

    # for item in json_data:
    #     test2[item["k"]] = item["v"]
    # # ensure_ascii=False来指定出中文
    # # indent对json进行数据格式化输出
    # aa = json.dumps(json_data, ensure_ascii=False, indent=4)


    print(json_data)

if __name__ == '__main__':
    a = input("input:")
    youdao(a)