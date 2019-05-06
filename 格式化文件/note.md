# 结构化文件存储
- xml,json
- 为了解决不同设备之间信息交换
# xml文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285
    
- XML(eXtensibleMarkupLanguage) 可扩展标记语言
    - 标记语言 语言中使用尖括号括起来的文本字符串标记
    - 可扩展 用户可以自己定义需要的标记
    - 例如：
        `<Teacher>
            自定义标记Teacher
            在两个标记之间任何内容都应该跟Teacher相关
        </Teacher>`
    - 是w3c组织制定的一个标准
    - XML描述的是数据本身 即数据的结构和语义
    - HTML侧重于如何显示web页面中的数据
    
- XML文档的构成
    - 处理指令（可以认为一个文件内只有一个处理指令）
        - 最多只有一行
        - 且必须在第一行
        - 以XML关键字开头
        - 一般用于声明XML的版本和采用的编码
            - version属性是必须的
            - encoding属性用来支出xml解释器使用的编码
    - 根元素（一个文件内只有一个根元素）
        - 在整个XML文件中 可以把他看作一个树形结构
        - 根元素有且只能有一个
    - 子元素
    - 属性
    - 内容
        - 表明标签所存储的信息
    - 注释
        - 起说明作用的信息
        - 注释不能嵌套在标签里
        - 只有在注释的开始和结尾使用双短横线
        - 三短横线只能出现在注释的开头而不能在结尾
    -保留字符的处理
        - XML中使用的符号可能跟实际符号想冲突 典型的就是左右尖括号
        - 使用实体引用（EntityReference）来表示保留字符
            - &:&amp;
            - <:&lt;
            - >:&gt;
            - ':&apos;
            - ":&quot;
            - 一共五个 每个实体引用都以&开头并且以分号结尾            
            
        - 把含有保留字符的部分放在CDATA块内部  CDATA块内部信息视为不需要转义  
        
              <![CDATA[select name,age from st where sc>80]]> 
    - XML标签的命名规则
        - Pascal命名法
        - 用单词表示 第一个字母大写
        - 大小写严格区分
        - 配对的标签必须一致                            
    - 案例exam
    
    
        
        