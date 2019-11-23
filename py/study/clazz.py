"""
人类
"""


class Human:

    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        print(self)

    def __home(self):
        print(self.name + "回家了！")
        return

    def go(self):
        self.__home()
        return self.__class__


""" 定义变量"""
zSan = Human("张三", "男")
print(zSan.go())

""" 动态添加属性"""
zSan.age = 18
print(zSan.age)
"""动态删除属性"""
del zSan.age

"""
类的继承男人
"""


class Man(Human):
    def __init__(self, name):
        """方式一"""
        # super(Man, self).__init__(name, "男")
        """方式二"""
        Human.__init__(self, name, "男")

    def go(self):
        return self.name + " " + self.sex + " 回家了！"


ls = Man("李四")
print(ls.go())
