# RE使用大致步骤
- 使用compile将表示正则的字符串编译为一个pattern对象
- 通过pattern对象提供一系列方法对文本进行查找匹配 获得匹配结果 一个match对象
- 最后使用match对象提供的属性和方法获得信息 根据需要进行操作

# RE常用函数
- group() 获得一个或者多个分组匹配的字符串 当要获得整个匹配的子串时 直接使用group或者group(0)
- start 获取分组匹配的子串再整个字符串中的起始位置 参数默认为0
- end 获取分组匹配的子串再整个字符串中的结束位置 默认为0
- span 返回的结构技术(start(group), end(group))

# 查找
- search(str,[,pos[,endpos]]): 在字符串中查找匹配 pos和endpos表示起始位置
- findall 查找所有
- finditer 查找 返回一个iter结果

# sub替换
- sub(rep1,str[,count])

# 匹配中文
- 大部分中文内容表示范围是[u4e00-u9fa5] 不包括全角标点

# 贪婪和非贪婪
- 贪婪：尽可能多的匹配    *表示贪婪
- 非贪婪: 找到符合条件的最小内容即可  ?表示非贪婪
- 正则默认使用贪婪匹配