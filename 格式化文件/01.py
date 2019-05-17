import xml.dom.minidom
# 负责解析xml文件
from xml.dom.minidom import parse

# 使用minidom打开xml文件
DOMTree = xml.dom.minidom.parse("exam.xml")
# 得到文档对象
doc = DOMTree.documentElement

# 显示子元素
for ele in doc.childNodes:
    if ele.nodeName == "Student":
        print("----------Node:{0}------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "name":
                print("Name:{0}".format(child.childNodes[0].data))