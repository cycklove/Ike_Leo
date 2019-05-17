import  xml.etree.ElementTree as et

stu2 = et.Element("Student1")

name = et.SubElement(stu2,"Name")
name.attrib = {"lang","en"}
name.text = "maozedong"

age = et.SubElement(stu2,"Age")
age.text = 18

et.dump(stu2)