# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 22:14
# @Author  : Feng Xiaoqing
# @FileName: jicheng-school.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print("for student %s do regit " % stu_obj.name)
    def hire(self,):
class SchoolMember(object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)

        def tell(self):
            print('''
            ------------info teacher-----------
            
            Name :%s
            Age: %s
            Sex :%s
            Salary: %s
            Course: %s
                      
            
            ''' % (self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is a  %s teacher" % (self.name,self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

        def tell(self):
            print('''
            ------------info student-----------

            Name :%s
            Age: %s
            Sex :%s
            Salary: %s
            Course: %s


            ''' % (self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print("%s has paid   %%s " % (self.name, self.amount)


school = School("Oldboy IT","北京")

t1 = Teacher('fxq'，22，'M',22222,'Linux')
t1 = Teacher('Alex'，32，'M',2000,'Python')

s1 = Student("Chenronghua",33,'MF',1101,'python')
s2 = Student("xiao wang",12,'MF',1103,'linux')

t1.tell()
s1.tell()

