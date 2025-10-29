class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, college, class_):
        super().__init__(name, age, gender)
        self.college = college
        self.class_ = class_

    def personInfo(self):
        super().personInfo()
        print(f"学院: {self.college}, 班级: {self.class_}")
#python的独特用法如下
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 学院: {self.college}, 班级: {self.class_}"


if __name__ == "__main__":
    stu = Student("napuc", 17, "男", "钱学森书院", "人工智能2501")
    stu.personInfo()
    print() 
    
    print(stu)