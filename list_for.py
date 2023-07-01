'''тип данных Списки'''
# спиписок изменяемый тип данных упорядаченный индексируемый интерируемый тип данных

#[] - > литералы вырожение или констандыкоторые создают обект

# list_ = [1,2,3,4,5[True, 'hello'], 'hello',{1:'one'},(1,2,3),]


# print(list_[0])
# print(list_[2][0])
# print(list_[-1])

'''======создание списков========'''

# from typing import Iterable

# list(Iterable)
# list_1 = list('hello world')
# print(list_1)
# 2. []
# a = []
 # print(type(a))

 # 3 range() -> возвращает последователность
#list_1 = list(range(11))

# range (start,end,step)
# start -> с какого числа начат по умолчанию 0 
# end -> до какого элемента не включително end
# step -> шаг какие элементы пропустит


'''=========== методы списков==========='''
# list,append (element) -> добавляет в конец списка
# list_3 = [1,2,3, 'hello', 'world','test']
# list_3.append(4)
# print(list_3)
# list_3 = [1,2,3, 'hello', 'world','test']
# list_3.extend([1,2,3])
# print(list_3)
# list.insert(index,element) добовляет element по индексу
# list_3 = [1,2,3,'hello','world','test']
# list_3.insert(3,4)
# list_3.insert(0, 'makers')
# print(list_3)
# list_3 = [1,2,3, 'hello','world','test',1,2,3]
# print(list_3.index(1))
# print(list_3.index('hello'))
# list.clear() -> очищает список
# list_3 = [1,2,3 'hello', 'world', 'test']
# list_3.clear()
# print(list_3)
# list.count(element) -> количество вхождений элемента в список 

# list_3 = [1,2,3 'hello', 'world', 'test']
# print(list_3.cound(1))
# print(list_3('hello'))


# pop ввозвращает удаленные элементы по умолчанию удоляет последный элемент удоляет элемент по индексу
# print(list_3.pop())
#print(list_3.pop(0))

# list.remove(element) -> удоляет element
# list_3.remove(1)

#list_3.remove(1)
#print(list_3)

# list.revers() переворачивает список 
# print(list_3)
# list_3.reverse()
# print(list_3)



# list.sort() сортирует список состаящий из элементов

# list_3 = [5,3,2,1,45]
# list_3.sort(reverse=True)
# print(list_3)
# list_ = ['f','a','h']
# list_.sort()
# print(list_)

# list.copy() -> поверхносное копирование

# list_ = ['hello', 1,2,3,4]
# list_1 = list_copy(list_)
# list.clear() -> очищает список
# list_3 = [1, 2, 3, 'hello', 'world', 'test']
# list_3.clear()
# print(list_3)

# list.count(element) -> возвращает кол-во вхождений элемента в список

# list_3 = [1, 2, 3, 'hello', 'world', 'test', 1, 2, 3, 1, 1]
# print(list_3.count(1))
# print(list_3.count('hello'))

# list.pop([index]) -> удаляет элементы по индексно, возвращает удаленный элемент. По умолчанию удаляет последний элемент списка
# list_3 = [1, 2, 3, 'hello', 'world', 'test', 1]
# print(list_3.pop())
# print(list_3.pop(0))
# print(list_3.pop(100)) IndexError: pop index out of range
# print(list_3)

# list.remove(element) -> удаляет element
# list_3.remove(1)
# list_3.remove(1)
# print(list_3)

# list.reverse() -> переворачивает список
# print(list_3)
# list_3.reverse()
# print(list_3)

# list.sort() -> сортирует список, состоящий из элементов одного типа. Сортирует в порядке возрастания, если указать reverse=True (по умолчанию reverse=False) то сортирует в порядке убывания
# list_3 = [5, 2, 4, 6, 7]
# list_3.sort(reverse=True)
# print(list_3)
# list_ = ['f', 'a', 'h', 'o', 'p', '_', ' '] # 
# list_.sort()
# print(list_)

# list.copy() -> поверхносное копирование
# list_ = ['hello', 1, 2, 3, 4]
# list_1 = list_.copy()
# # list_1 = list_
# list_.pop()
# print(id(list_))
# print(id(list_1))

'''======== Цикл for ========'''
# повторяющийся блок кода

# list_ = [1, 2, 3, 4, 5]
 

# for i in list_:
#     print(i)

# for i in list_:
#     print(i ** 2)

# str_ = 'hello'
# for i in str_:
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(11):
#     if i % 2:
#         print(i,'нечетное')
#     else:
#         print(i, 'четное')

# for i in  range(1, 5):
#     print()
#     print(i)
#     for b in range(i):
#         print(b)





# list_ = [1, 'hello', 2, 3, 4, 5, 'test', 'world']
# list_index = []
# for i in list_:
#     if type(i) != int:
#         list_index.append(i)

# for i in list_index:
#     list_.remove(i)
# print(list_) 





# Tuple ====================
# кортеж неизменяемый индесируемымя
  # упорядоченным интерируемым типом данных 
  # литералы 


# a = 1,2,3,4
# a = (8,)
# print(type(a))



 #  методы тупле d
# num = 5 
# per = num * 4 
# s = num ** 2 
# print (per,s)

# numbers = [7] * 7
# print(numbers)

# number = list(range(9,21,2))
# print(number)

# for i in range(1,11):
#     i = i ** 2
#     print(i)

# number = [1,True,'hello',1,3,4,6,(1,2),['bootcamp']]
# print(number[2])
# print(number[-2])


# number = [1,True,'hello',1,3,4,6,(1,2),['bootcamp']]

# number[-2] = 'world'
# print(number)

# user = ['Alice','Sam','Carly']
# for user in user:
#     print(f'hello {user}')

# for letter in 'makers':
#     print(letter.upper())

# append(element)
# user = ['alise','sam','billy']
# print(user)
# user.append('tom')
# # user.append(users)
# print(user)


# guest = []
# list_length = int(input('enter number of guest  '))

# for i in range(list_length):
#     user = input('enter guest name  ')
#     guest.append(user)
# print(guest)

