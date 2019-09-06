from lxml import etree

html =etree.parse("./29.xml")

rst = html.xpath("//from")
print(type(rst))
print(rst)

#XPATH的意思是查找带有nm属性值为ike的元素
rst2 = html.xpath('//from[@nm="ike"]')
print(type(rst2))
print(rst2)

rst3 = html.xpath('//from[@nm="ike"]/age')
rst3 = rst3[0]
print(type(rst3))
print(rst3)
print(rst3.tag)
print(rst3.text)