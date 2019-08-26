'''
中文Unicode
'''
import re

hello = u'你好 世界'

pat = re.compile(r'[\u4e00-\u9fa5]+')

m = pat.findall(hello)
print(m)