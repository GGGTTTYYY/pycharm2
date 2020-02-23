"""
定义一个学生类，用来形容学生
"""


# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个对象
mingyue = Student()


class PythonStudent():
    name = None
    age = 18
    course = 'python'

    def dohomework(self):
        print("我在做作业")
        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.dohomework()
