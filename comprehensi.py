'''Comprehension'''
# 


# for переменная in диапазон :
# тело
#  ===синтаксис=== 
# резултат for элемент in иттериуемый обект
# резултат for элемент in иттериуемый обект if филтр 
 

'''list comprehension '''
# упрощение процесса создание списков

# list_ = []
# for i in 'hello':
#   list_.append(i)

# list_0 = list((i for i in 'hello'))
# list_1 = [] 










#import time 
# start_time = time.time()
# list_ = []
# for i in range(1, 1000001):
#     list.append(i)
# print(time.time() - start_time)
# #print(list_)

# #start_time = time.time()
# list_num = [number for number in range(1,1000001)]




# ''''''''создайте список 1 до 10  ''''


# list_ = [i for i in  range(1,11 if i % 2 == 0]
    
# print(i)

    
# list_str = []

# for i in range(1,11):
#     if i % 2 == 0 :
#         list_str.append('четное ')
#         print(list_str)
#     else:
#         list_str.append('не четное ')
#         print('не четное')


# list_ = [1,2,3,1,'test', 'python',
#          'makers', 1,2,3,4,5,6, 'hello']
# set_l = {i + 'world' for i in list_ if type
#          (i) == str}
# set_ = set()
# for i in list_:
#     set_.add(i)
# print(set_)

# ========Dict comprhension=========

# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# dict_1 = {}

# for k, v in dict_.items():
#     dict_1.update({v: k})
# print(dict_1)


# dict_ = {}
# for i in range(1,11):
#     dict_.update({i: i** 2})
# print(dict_)


# dict_ = {i: i ** 2  for i in range(1,11)}
# print(dict_)

# list_ = [1,1,1,3,4,2,3,7,8,4,4,]
# dic_1 = {i: list_.count(i) for i in list_}
# print(dic_1)


# dict_ = {'a': 1, 'b': 2, 'c': 3, 'b': 4, 'e': 5}
# {'a': 'не четное', 'b': }

# list_1 = [1,2,3,4,5]
# list_2 = ['a','b','c', 'd', 'e','g']
# dict_list = {
#     list_1[index]:list_2[index] for index in range(len(list_1))
#     }

# print(dict_list)


# обеденител join(list_)  переводитсписок в тип данных строки 
# ''.join(['a','b', 'c'])  'abc'


# +=========вложенные comprehensions===========


# dct = {
#     i:
#     [j for j in range(1, i+1)]
#     for i in range(1,6)
#     }
# print(dct)

# list_ = [['hello world' for i in range(2)]]

# employees = {
#     'id1': {
#         'first name': 'Александр',
#         'last name' : 'Иванов',
#         'age': 30,
#         'job':'программист'
#             },
#     'id2': {
#         'first name': 'Ольга',
#         'last name' : 'Петрова',
#         'age': 35,
#         'job':'ML-engineer'
#         }}
# dct = {
#     key: 
#     {k: float(v) 
#     if k == 'age' else v 
#     for k, v in value.items()
#     }
#     for key, value in 
#     employees.items()
#     }

# print(dct)
# # dct = {
#     key: 
#     {k: float(v) 
#     if k == 'age' else v 
#     for k, v in value.items()
#     }
#     for key, value in 
#     employees.items()
#     }

# print(dct)

# dct = {
#     key: 
#     {k:float(v)
#     if k == 'age' else v 
#     for k, v in info.items()
#     }

# }








# a = int(input(' '))
# b = int(input(' '))
# c = int(input(' '))
# if a + b <= c or a + c <= b or b + c <= a:
#     print('impossabile')
# elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or a**2 + b**2 == c**2:
#     print('rectangular') 
# elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or a**2 + b**2 < c**2:
#     print('"acute"')
# else:
#     print("obtuse")

# n = int(input('введите число:  '))
# if n % 10 == 1 and n % 100 != 11:
#     print(f'На лугу пасется {n} корова')Сумма: 8
# Разность: 2
# Произведение: 15
# Частное: 
# elif 2 <= n % 10  <= 4 and (n % 100 < 10 or n % 100 >= 20):
#     print(f'На лугу пасется {n} коровы')
# else: 
#     print(f'На лугу пасется {n} коров')

# a = int(input('первое число:  '))
# b = int(input('второе число:  '))
# oper1 = a + b 
# oper2 = a - b
# oper3 = a * b
# oper4 = a % b 
# print('сумма',oper1)
# print('разность',oper2)
# print('Произведение:',oper3)
# print('Частное',oper4)

# n = int(input('Введите количество пар чисел: '))

# for result in range(n):
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))

#     oper1 = a + b
#     oper2 = a - b
#     oper3 = a * b
#     oper4 = a / b

#     print('Сумма:', oper1)
#     print('Разность:', oper2)
#     print('Произведение:', oper3)
#     print('Частное:', oper4)
#     print()