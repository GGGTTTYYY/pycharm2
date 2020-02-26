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
yueyue.age = 16
yueyue.name = "xiaodana"

# 查看A内的所有属性

print(PythonStudent.__dict__)
print(yueyue.__dict__)

print(PythonStudent.age)
print(PythonStudent.name)
print("*" * 20)

print(id(PythonStudent.name))
print(id(PythonStudent.age))

print("*" * 20)

print(yueyue.name)
print(yueyue.age)

print("*" * 20)

print(id(yueyue.name))
print(id(yueyue.age))
yueyue.dohomework()
