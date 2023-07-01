"""Области видимости и пространство имен"""
# def func():
#     a = 0 
#print('функциа func')

# print(func)

'''byuktubs (встроиные что все что встроено в стандартную библетеку питона)'''
# print, input , len ....
# a = 'sam'
'''
2 Global глобалное   все перемменные внутри файла которые мы создали
без табуляции 
'''
'''enclpsed     локалное )))       
или замкнутая находится между двух пространствами
'''
# print(globals()) возвращает все глобал переменные
# 
#  
# print(dir(__builtins__))  возврашает все встроенные имена

# x = 100 
# y = 0 
# z = 99
# print(globals())
# globals()['x'] = 45
# print(globals())

# print(z is globals()['z'])
# print(globals())

'''local   локалное  ''' 
# locls () возвршает все локалные имена 
# def func(test):
#     a = 10
#     b = 0 
#     print(locals()) возвращает словар {'test': 6, 'a': 10, 'b': 0}
# func(6)

# print(locals()) когда применяем на глабалном уровне возвращает все все глобалные имена


# def func1():
#     a = 0 
#     b = 9

#     print(a, b)


# func1()


# Enclosed возникает 


# def outer_func():
#     outer = ' не локалная пременная (enclosed)'
#     print(outer)
#     def inner_func():
#         inner = "локална переменная "

#         # print(inner)
#     inner_func()
#     # print(locals)
# outer_func()

# iner_func() будет ошибка так как она не в локалной области
#  порядок поиска переменных 
'''local enclosed clobal builtins'''

# import this  #краткий гайд по дзен питону
'''global позволяет значение глобалной переменной находяс в локалном области
видимости'''

# x = 10
# def func():
#     # global x
#     # x += 20

#     print(x + 99)
# func()
# print(x)



# count = 0 

# def couter():
#     global count
#     count += 1
#     return count
# print(couter())
# a = 0
# def outer():
#     global a
#     a = 8
#     def inner():
#         global a
#         a = 10
#         print('inner a = .', a)
#     inner()
#     print('outer a = ', a)
# outer()
# print('global a =', a)
'''nonlocal позволяет изменит значение enclosed не локалное переменной в локалной области видимости'''

# a = 0
# def outer():
#     a = 8
#     def inner():
#         nonlocal a
#         a = 10
#         print('inner a = .', a)
#     inner()
#     print('outer a = ', a)
# outer()
# print('global a =', a)


