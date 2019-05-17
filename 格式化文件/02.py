import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("exam.xml")
print("利用getiterator访问：")
nodes = root.getiterator()
for node in nodes:
    print("{0}------{1}".format(node.tag,node.text))

print("利用find和findall方法：")
ele_student = root.find("Student")
print("{0}------{1}".format(ele_student.tag,ele_student.text))

ele_stus = root.findall("Student")
for ele in ele_stus:
    print("{0}------{1}".format(ele.tag,ele.text))
    for sub in ele.getiterator():
        if sub.tag == "name":
            if "Other" in sub.attrib.keys():
                print(sub.attrib["Other"])