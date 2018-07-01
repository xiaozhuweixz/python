# li = [11,22,33,44]
# for item in li:
#     print (item)


# li = [11,22,33]
# for k,v in enumerate(li, 1):
#     print(k,v)
# list = [11,22,33,44,55,66,77,88,99,90]
# dict = {}
# list1 = [];
# list2= [];
# for item in list:
#     if item > 66:
#         list1.append(item)
#     else:
#         list2.append(item)
# dict['k1'] = list1
# dict['k2'] = list2
# print(dict)

# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
#
#
# for item in li:
#     if (item.strip().startswith('a') or item.strip().startswith('A')) and item.strip().endswith('c'):
#        print(item.strip())
#
# for item in tu:
#     if (item.strip().startswith('a') or item.strip().startswith('A')) and item.strip().endswith('c'):
#          print(item.strip())
#
# for item in dic:
#     if (dic[item].strip().startswith('a') or dic[item].strip().startswith('A')) and dic[item].strip().endswith('c'):
#         print(item.strip() + ':' + dic[item].strip())


# li = ["手机", "电脑", '鼠标垫', '游艇']
# dic = {}
# for key,val in enumerate(li, 1):
#     print(str(key) +':'+ val)
#     dic[key] = val
# print(dic)
#
# username = input('请输入相对应的序号:')
# dirStr = dic
# for item in dirStr:
#     if str(item) == username:
#         print(dirStr[item])
#     continue


# goods = [
# #     {"name": "电脑", "price": 2001},
# #     {"name": "鼠标", "price": 10},
# #     {"name": "游艇", "price": 20},
# #     {"name": "美女", "price": 998},
# # ]
# #
# # goodsDic = {}
# # mun  = 2000
# #
# # for key , val in enumerate(goods,1):
# #     goodsDic[str(key)] = val
# # print(goodsDic)
# #
# # index = input('请输入相对应的购买序号:')
# # for item in goodsDic:
# #     if str(item) == index:
# #         print(goodsDic[index]['name'])
# #         print(goodsDic[index]['price'])
# #         if str(mun) < str(goodsDic[index]['price']):
# #             print('所购买的金额大于余额，请进行充值.')
# #             break
# #         else:
# #             #print('购买成功，所剩余额为:' + str(mun) - str(goodsDic[index]['price']))
# #             del goodsDic[str(index)]
# #             break
# #     else:
# #         continue
# # print(goodsDic)


# dic = {
#     "河北": {
#         "石家庄": ["鹿泉", "藁城", "元氏"],
#         "邯郸": ["永年", "涉县", "磁县"],
#     }
# }
#
# city = input('请输入省份:')
# print(dic[city])
# privtion = input('请输入城市')
# print(dic[city][privtion])

# shopping_cart = []
# salary = 2000
# goods = [
#     {"name": "电脑", "price": 3000},
#     {"name": "鼠标", "price": 103},
#     {"name": "游艇", "price": 200000},
#     {"name": "美女", "price": 998},
# ]
# for i in enumerate(goods):
#     index = i[0]    #序号
#     p_list = i[1]   #商品清单
#     p_name_list = p_list.get('name')#商品名称列表
#     p_price_list = p_list.get('price')#商品价格列表
#     print(index,":",p_name_list,p_price_list)
#
# while True:
#     choice = input("please enter your choice:").strip()
#     if choice.isdigit():#如果选择为正整数
#         choice = int(choice)#输入为数字
#         if choice < len(goods) and choice >= 0:#选择小于列表长度大于0时
#             p_item = goods[choice]#加入购物车
#             p_name = p_item.get('name')
#             p_monery = p_item.get('price')
#             if p_monery <= salary:#如果商品价格小于等于余额
#                 shopping_cart.append(p_item)#加入购物车
#                 salary -= p_monery#结算
#                 print("购买的商品\033[32m:%s\033[0m已加入到购物车".center(40, '-') %p_name)
#                 for p_item in shopping_cart:
#                     print(p_name,p_monery)
#                     print("您的余额为\033[31m:%s\033[0m元" % salary)
#             else:
#                 print("您的余额不足，差%s元"%(abs(p_monery - salary)))
#         else:
#             print("没有此件商品!")
#     else:
#         print("参数错误")
#     if choice == "q" or choice == "quit":
#         cost = 0
#         print("您购买的商品清单如下:")
#         for p in shopping_cart:
#             print(p_name, p_monery)
#             cost += p_monery
#         print("\033[32m消费总金额:",cost,"元\033[0m")
#         print("\033[32m您的余额为:",salary,"元\033[0m")
#         break

# import copy
#
# # ######### 数字、字符串 #########
# n1 = 123
# # n1 = "i am alex age 10"
# print(id(n1))
# # ## 赋值 ##
# n2 = n1
# print(id(n2))
# # ## 浅拷贝 ##
# n2 = copy.copy(n1)
# print(id(n2))
#
# # ## 深拷贝 ##
# n3 = copy.deepcopy(n1)
# print(id(n3))

# ######### 定义函数 #########

# name 叫做函数func的形式参数，简称：形参
# def func(name):
#     print (name)
#
# # ######### 执行函数 #########
# #  'wupeiqi' 叫做函数func的实际参数，简称：实参
# func('wupeiqi')


# def func(name, age=18):
#     print("%s:%s" % (name, age))
#
#
# # 指定参数
# func('wupeiqi', 19)
# # 使用默认参数
# func('alex')

#
#
# def func(*args):
#
#     print (args)
#
#
# # 执行方式一
# func(11,33,4,4454,5)
#
# # 执行方式二
# li = [11,2,2,3,3,4,54]
# func(*li)


# def func(arg1, arg2):
#     if arg1 == 0:
#         print(arg1, arg2)
#     arg3 = arg1 + arg2
#     print(arg3)
#     func(arg2, arg3)
#
# func(0, 1)

# def func(ages):
#     print(ages)
# func('caixiaowei')

# def func (name, age = 18):
#     print(name +':'+ str(age))
# func('caixiaowei',19)

# def func (*ages):
#     print(ages)
#
# func(['111','2222','3333'],1111)
#
# li = ['111','2222','3333']
# mun = 2222
# func(li,mun)
# def func (**ages):
#     print(ages)
#
# func({'k1':'11111','k2':'22222'},1111)

# def function(str):
#     strIndex = 0
#     munIndex = 0
#     tiramIndex = 0
#     for item in str:
#         print(item)
#         if item.isnumeric():
#             munIndex+=1
#         elif item.isalpha():
#             strIndex+=1
#         else:
#             tiramIndex+=1
#     print(strIndex)
#     print(munIndex)
#     print(tiramIndex)
#
#
#
# function('AAaa11 ')
# # print(strIndex)
# # print(munIndex)
# # print(tiramIndex)

# def func(*age):
#     if len(*age) > 5:
#         print('传入的长度过长')
#     else:
#         print('传入的长度正好')
#
# li = [1,2,3,4,5,6,7]
# tuples = (1,2,3,4,5,6,7)
# strs = '213333'
# func(strs)
#
# def func(age):
#     if len(age) > 2:
#         return age[0:2]
#     else:
#         return age
# li = func([11,22,33])
# print(li)
# li = []
# def fun(ages):
#     for key,val in enumerate(ages,1):
#         if key%2 != 0:
#            li.append(val)
#     return li
#
# li = fun([11,22,33,44,55,66,77,88])
# print(li)

# tup1 = []
# def fun(ages):
#     for key,val in enumerate(ages,1):
#         if key%2 != 0:
#             print(ages[key])
#             tup1.append(ages[key])
#     return tup1
# li = fun((11,22,33,44,55,66,77,88))
#
# print(li)

# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# dicStr = {}
# def func (age):
#     for item in age:
#         if len(dic[item]) > 2:
#             valItem = dic[item]
#             dicStr[item] = valItem[0:2]
#         else:
#             print('恭喜你中奖了')
#     print(dicStr)
# func(dic)

# def nrange(num):
#     temp = -1
#     while True:
#         temp = temp + 1
#         if temp >= num:
#             return
#         else:
#             yield temp
# print(nrange(10))

# import sys
# # print (sys.path)

# import sys
# import time
#
#
# def view_bar(num, total):
#     rate = float(num) / float(total)
#     rate_num = int(rate * 100)
#     r = '\r%d%%' % (rate_num, )
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
#
# if __name__ == '__main__':
#     for i in range(0, 100):
#         time.sleep(0.1)
#         view_bar(i, 100)

# import hmac
#
# h = hmac.new(bytes('898oaFs09f', encoding="utf-8"))
# h.update(bytes('admin', encoding="utf-8"))
# print(h.hexdigest())

# import random
#
# print(random.random())
# print(random.randint(1, 2))
# print(random.randrange(1, 10))

# import random
# checkcode = ''
# for i in range(4):
#     current = random.randrange(0,4)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
# print (checkcode)

# 无分组
# import re
# r = re.match("h\w+", 'origin')
# print(r.group())  # 获取匹配到的所有结果
# print(r.groups())  # 获取模型中匹配到的分组结果
# print(r.groupdict())  # 获取模型中匹配到的分组结果
import re

origin = "hello alex bcd abcd lge acd 19"
#r = re.findall("a\w+",origin)
r = re.findall("a((\w*)c)(d)", origin)
print(r)