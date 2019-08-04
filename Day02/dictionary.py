# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 20:49
# @Author  : Feng Xiaoqing
# @FileName: dictionary.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

info = {
    'stu101' : 'fengxiaoqing1',
    'stu102' : 'fengxiaoqing2',
    'stu103' : 'fengxiaoqing3'


}

print(info)
print(info['stu101'])
info["stu101"]= "xiaoqing"
print(info)

#del
del info['stu101']
print(info)


info.pop('stu102')

print(info)


print(info.get('stu102'))

#查找
print('stu101' in info)

info.keys()
info.setdefault('stu107','fengxiaoqing7')
print(info)

b = {
    'stu101':'xushen1',
    'stu102':'xushen2',
    'stu103':'xushen3'


}
info.update(b)
print(info)


c = dict.fromkeys([6,7,8],[1,{'name':'alex'},444])#坑，改1为333所有的就都被改了。

c[7][0]='333'
print(c)
c.pop(6)
print(c)

print('#'*50)
#字典循环
print(info)
for i in info:
    print(i,info[i])
# for k,v in info.items(): 效率没有上面的方法高。
#        print(k,v)


