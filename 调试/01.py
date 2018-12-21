def sayhello(name):
    print("I want to say hello with you,{0}".format(name))
    print("hello {0}".format(name))
    print("Done......")

# if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
if __name__ == "__main__":
    print("***" * 10)
    name = input("Please input your name: ")
    print(sayhello(name=name))
    print("@@@" * 10)

