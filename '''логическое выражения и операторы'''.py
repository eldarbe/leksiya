'''логическое выражения и операторы'''
'''booleav'''
#true/False
# print(bool(0)) #False
# print(bool(2)) #True
# print(bool(False)) #False
# print(bool(' ')) #true
# print(bool('')) #false
# print (bool(234)) 

''''Логические  выражения -> выражения которые возвращают boolean type'''
 #== -> сравнение 
#5 == 5 #true
#4 == 6 #fals 
#'5' == 5 # false
# != - > не равно 
# false 
# 6 != 4  #true

# < менше 
3 < 4 # true
3 < 1 # false
3 < 3 # false

# >= -< болше или равно 
6 >= 5 #true 
6 >= 6 # true
6 >= 9 #false

# <= -> меншешого или рано
4 <= 3 #false 
4 <= 5 # true 
4 <= 4 # true


# or -> логические или 
# and -> логическое и 
# not -> логическое отритцание 


# true          true 
# a == 5 and b == 6 # true 
# a == 4 and b == 6 # false 
# a == 3 and b == 9 # false

# если все чати вырожения 







# a == 'g' and b == 'h'
# a == 5 or b == 6 # true
# a == 4 or b == 6 # true 
# a == 4 or b == 9 # false

#если хотябы одна часть вырожения возврашает true то все все вырожение вернет true

# not 

#print (not true)   

'''операторы идентификации'''
 # 1. in -n -> проверяет наличие элемента 
 # 2. sravnenie 
# #   == -> по значению 
# #   is -> по ячейке памяти 
 

# '''====none type====='''''
# # не изменяемые тип данных значение None исползует для обозначение пустых значений
# bool(None) #false
# bool('None') # true
# # a = none


'''=====условные операторы ====='''
# нужны для того чтобы при разных входных данных код выполнялся по разному


# if_ условие 
#      тело 
# # тело будет работать если условие true
#  if условие 
#      тело 
#         #условие тело один будет работат если условие 1 верно

# number = int(input('введите число:'))
# if number 




#'''''Маржовые операторы ''''''
# :=
# print(hello :="hello") 







# age = int(input())

# if age % 2 == 0:
#     print('четное')
# else: 
#     print("нечетное")
# if age % 2 : 
#     print('не четное')

# else: 
#      print ('четное')



'''Fizzbuzz'''

# a = int(input())

# if a % 15 == 0:
#     print('fizzbuz')
# elif a % 3 == 0:
#     print ('faizz')
# elif a % 5 == 0: 
#     print('buzz')
# else:
#     print(a)