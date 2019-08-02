from urllib import  request
import chardet

if __name__ == '__main__':
    url = "http://www.renren.com/256297970/profile"

    rsp = request.urlopen(url)
    html =  rsp.read()
    cs = chardet.detect(html)
    html = html.decode(cs.get("encoding","utf-8"))

    with open("rsp.html","w",encoding="utf-8") as f:
        f.write(html)
        f.close()