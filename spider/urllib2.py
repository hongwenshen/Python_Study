import requests
import os
try:
    url = "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%9B%BE%E7%89%87&hs=0&pn=0&spn=0&di=21166381280&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=2735633715%2C2749454924&os=1423882261%2C1566996236&simid=4041337662%2C948052319&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fwww.pptbz.com%2Fpptpic%2FUploadFiles_6909%2F201203%2F2012031220134655.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Brrpkz_z%26e3Bv54AzdH3FrrprtvAzdH3Frrprtv_80ln_z%26e3Bip4s&gsm=0&islist=&querylist="
    root = "F:/Git\PythonStudy/Python_Study/resources"
    path = root + url.split('/')[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        res = requests.get('url', timeout=5)
        files = open(path, 'wb')
        files.write(res.content)
        files.close()
        print('文件已经下载成功')
    else:
        print("文件已经存在")
except:
    print("获取失败")