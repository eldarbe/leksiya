'''обработка исключений '''


'''''
ошибки это проблемы с синтаксисомисключение 
1 syntaxError   забыли двое точи или скобку

2 indentationerror: неправилный отступ 

3 tabError неправилное табуляция



'''

# 2f = 8


# исключение код написан правилно но работает не так 
# как ожидалос

# AritheticError 
# zerodivisioError
# valueError 
# NameError
# TypError
# KeyError
# IndexError
#AttributeError
#ImportError
#BaseExeption (прородител)

ZeroDivisionError# при делении на 0 
# 8 / 0 

# 4 // 0 
#3 % 0

ValueError# int('hello') вызывается при распоковке переводе одного типа данных на другой

# a = 'abc'
# k,b = a 

NameError# когда обращаемся  к несушествуещому переменной

# print (b )

TypeError#  когда передаем функцию метод менше или боьше арнументов чем требуется 
# for i in 12345677:
#     print(i)

# [] . append(1,2,3)
# '5' + 5 

KeyError# при обращении к не существуещому ключу

# dict_ = {'a': 1}
# #dict_['b']
# # dict_.pop('b')


# IndexError # при обращении к не сушествуешому индексу

# #list_ = ['a','b','c']
# #list_[4]
# # list_.pop(3)


# AttributeError# когда не существуещому методу или отрибуту

# #a = 12341
# # a.upper()
# b = [1,3,4]
# #b.discard()


# ImportError# когда не правилно написал импорт обекта


# # BaseXception прородител


# '''try except'''
#  #чтобы код не прекращал свою работу

# ''' синтаксис'''
# try:
#     тело try 
#     # код который может вызват ошибку

# except: 
#     тело except
#     # код который сработает если в try возник ошибка


# else:
#     тело else 
#     # код коотработаетесли в блоке try не возникла

# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')
# try:
#     dict_ = {key: key ** 2 for key in range (11)if key % a == 0}
#     print(dict_)
#     value = dict_[3]
#     print(value)
# except NameError:
#     print('переменная dict_ не обявлена')

# try: 
#     num = int(input(''))
#     num2 = int(input(''))
#     result = num + num2 
# except ValueError:
#     print('ввели не число')
#     num = int(input(''))
#     num2 = int(input(''))
#     result = num + num2
#     # print(result)
# else:
#     print('не возникла ошибки')
# finally: ()
# print(result)

'''''============ raise ==========='''''
# искучтвенно вызывает ошибки 
# try:
#     age = int(input('введите возраст: '))
#     if age > 18:
#         print('okey')
#     elif age > 18:
#         print('no')
#         raise ValueError('досьуп закрыт')
# except:
#     print('вам менше 18ти или ввыели не цифру')

# name_of_friends = ['hello','world','python','eldar','9']
# for name in name_of_friends:
#     print(name)
labels = ['Honda','Kawasaki']
for name in labels:
    print(f'I like brand {name}')