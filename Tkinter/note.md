#GUI介绍
- Graphicaluserinterface
- GUI for Python: Tkinter wxpython pyqt
- Tkinter
    - 绑定的TK GUI工具集 用Python包装的TCL代码
- PyGTK
    - Tkinter的替代品
- wxPython
    - 跨平台的Python GUI
- PyQT
    - 跨平台的
    - 商业授权可能有问题      
    
- 推荐资料
    - 辛星GUI     辛星Python
    - Python GUI programming cookbook
    
# 常用的组件
- 按钮
    - button      按键
    - radiobutton  单选
    - checkbutton  多选按钮
    - listbox      列表框
    
- 文本输入组件
    - entry      单行文本
    - text       多行文本
    
- 标签组件
    - label      可以显示图片和文字
    - message    可以根据内容将文字换行
    
- 菜单
    - menu       菜单
    - menu       菜单按钮组件
    
- 滚动条
    - scale      滑块
    - scrollbar  滚动条
    
- 其他组件
    - canvas   画布
    - frame    框架 将多个组件编组
    - toplevel 子窗口容器组件    
                                                          
- button属性
    - text 显示文本内容
    - command 指定Button的事件处理函数
    - compound 指定文本与图像的位置关系
    - bitmap 指定位图
    - focus_set 设置当前组件得到的焦点
    - master 代表了父窗口
    - bg 设置背景颜色
    - fg 设置前景颜色
    - font 设置字体大小
    - height 设置显示高度、如果未设置此项，其大小以适应内容标签
    - relief  指定外观装饰边界附近的标签,默认是平的,可以设置参数;flat、groove、raised、ridge、solid、sunken
    - width  设置显示宽度，如果未设置此项，其大小以适应内容标签
    - wraplength  将此选项设置为所需的数量限制每行的字符,数默认为0
    - state  设置组件状态;正常(normal),激活(active),禁用(disabled)
    - anchor 设置Button文本在控件上的显示位置 可用值:n(north),s(south),w(west),e(east),和ne,nw,se,sw
    - bd     设置Button的边框大小;bd(bordwidth)缺省为1或2个像素
    - textvariable  设置Button与textvariable属性
    
# 组件布局
- 三种布局
    - pack   按照方位布局
    - place  按照坐标布局
    - grid   网格布局
    
- pack布局
    - 最简单 代码量最少 挨个摆放
    - 通用方式   组件对象.pack()
    - side   停靠方位  可选值LEFT TOP RIGHT BOTTON
    - fill   填充方式  X Y BOTH NONE
    - expande YES NO
    - anchor  N E S W CENTER
    - ipadx  x方向的内边距
    - ipady  y方向的内边距
    - padx  x方向的外边界
    - pady  y方向的外边界
    
- grid布局
    - 通用方式   组件对象.grid()
- place布局

## 消息机制
- 消息的传递机制
    - 自动发出事件/消息
    - 消息由系统负责发送到队列
    - 由相关组价进行绑定/设置
    - 后端自动选择感兴趣的事件并作出相应反应
- 消息格式
    - <modifier-]---type-[-detail]>
    - <Button-1> Button表示一个按钮时间 1代表的是鼠标左键 2代表中键
    - <KeyPress-A>  键盘A
    - <Control-Shift-KeyPress-A> 同时按下Control,Shift,A
    - [键位对应名称](https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html)       
    
## Tkinter的绑定
- bind_all 全局范围的绑定 默认的是全局快捷键 比如F1是帮助文档
- bind_class 接受三个参数 第一个是类名 第二个是事件 第三个是操作
- bind 单独对某一个实例绑定
- unbind 解绑

# Entry
- 输入框 功能单一
- entry["show"]="*"  设置遮挡字符

# 菜单
# 普通菜单
- 第一个menu类定义的是parent
- add_command 添加菜单项 如果菜单是顶层菜单 则从左向右添加 否则就是下拉菜单
    - label 制定菜单项的名称
    - command 点击后相应的调用函数
    - acceletor 快捷键
    - underline 指定是否菜单下是否有横线
    - menu 指定使用哪一个作为顶级菜单
    - 05
# 级联菜单
- add_cascade 级联菜单 作用是引出后面的菜单
- add_cascade的menu属性 指明把菜单级联到哪个菜单上
- label  名称
- 过程
    - 建立menu实例
    - add_command
    - add_cascade
    - 06   
    
# 弹出式菜单
- 也叫上下文菜单
- 实现的大致思路
    - 建立菜单并向菜单添加各种功能
    - 监听鼠标右键
    - 如果右键点击 则根据位置判断弹出
    - 调用Menu的pop方法
    - 07
- add_separator分隔符 

# canvas画布
- 画布 可以自由的在上面绘制图形
- 再画布上绘制对象 通常create_xxx  xxx=对象类型  例如 line,rectangle
- 08 09
- 画布的作用是把一定组件画到画布上显示出来
- 画布所支持的组件
    - arc
    - bitmap
    - image(bitmapimage photoimage)
    - line
    - oval
    - polygon
    - rectangle
    - text
    - window(组件)
- 每次调用create_xxx都会返回一个创建的组件的ID 同时也可以用tag属性指定其标签
- 通过调用canvas.move实现一个一次性动作
    - 10
         