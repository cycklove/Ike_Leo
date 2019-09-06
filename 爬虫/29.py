from lxml import etree

html =etree.parse("./29.xml")

rst = etree.tostring(html,pretty_print=True)
print(rst)

