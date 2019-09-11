# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 7:13
# @Author  : Feng Xiaoqing
# @FileName: Jicheng.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# class People:(经典类)
class People(object):#新式类 主要是继承有变化

    def __init__(self,name,age):
        self.name = name
        self.age = age



    def eat(self):
        print("%s is eating.." %(self.name))

    def talk(self):
        print("%s is talking.." %(self.name))

    def sleep(self):
        print("%s is sleeping.." %(self.name))

# a = People('fxq',22)
# a.eat()
class Relation(object):

    def make_friend(self,obj):
        print('%s is making friend with %s' % (self.name,self.obj.name))


class Man(People,Relation):

    # def __init__(self,name,age,money):
    #     People.__init__(self,name,age)
    #     self.money = money
    #     print("%s is born ,have lots of movey,is %s" % (self.name,self.money))
    def __init__(self,name,age,money):
        super(Man,self).__init__(name,age) #不用写多个Poeple
        self.money = money
        print("%s is born ,have lots of movey,is %s" % (self.name,self.money))

    def piao(self):
        print("%s is piaoing.." % (self.name))

    def sleep(self):
        People.sleep(self)
        print("man is sleeping...")

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)

man=Man('aaa',33,'10')
man.eat()
man.piao()
man.sleep()
man.money()


women = Woman('haha',55)
women.get_birth()
women.sleep()

man.make_friend(w1)