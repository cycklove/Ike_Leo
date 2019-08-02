from urllib import request
import chardet

if __name__ == '__main__':
    url = "http://www.renren.com/256297970/profile"

    headers = {
        "Cookie":"anonymid=jyr1wl52oae6wq; depovince=GW; _r01_=1; __utma=151146938.1257409968.1564652147.1564652147.1564652147.1; __utmz=151146938.1564652147.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/SysHome.do; _de=264F4ADEAF0A744244B0A57815E527E7696BF75400CE19CC; ln_uact=saiyuyu3@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20120706/1715/h_main_Hxjs_4591000002061376.jpg; jebe_key=b56156b9-1b69-4e3d-89cd-3cbf3118c942%7Ce87d70e49fc070044e774e03c766eff5%7C1564652804374%7C1%7C1564652830979; jebecookies=bceb81cf-0245-4d5f-800b-d53d4f6bac30|||||; ick_login=dab2d0d1-eedb-4d7d-9c5d-f33a2a687354; p=33daf41fed384ea987d3e029fa7e07350; first_login_flag=1; t=d3176ac7ac895cbf237799fc9be0f9f80; societyguester=d3176ac7ac895cbf237799fc9be0f9f80; id=256297970; xnsid=aff87079; ver=7.0; loginfrom=null; wp_fold=0"
    }

    req = request.Request(url,headers=headers)
    rsp = request.urlopen(req)

    html = rsp.read()
    cs = chardet.detect(html)
    html = html.decode(cs.get("encoding","utf-8"))

    with open("rsp2.html","w",encoding="utf-8") as f:
        f.write(html)
        f.close()