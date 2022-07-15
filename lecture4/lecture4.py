# install pylint
from typing import List
from functools import reduce

# num = (3)
# print(type(num))

# num = (3,)
# print(type(num))

# list1 = [1, 3, 2, 9, 1]
# print(list1.sort()) #None
# print(sorted(list1)) #1, 1, 2, 3, 9

##############
#  SLIDE 6
##############
# def remove_duplicate(var_list):
#     return list(set(var_list))

# def capitalize_list(var_list):
#     final_list = []
#     for item in remove_duplicate(var_list):
#         final_list.append(item.upper())
#     return final_list

# my_list = ['cow', 'cow', 'how']
# my_list = capitalize_list(my_list)
# print(my_list)

##############
#  SLIDE 7
##############
# def print_even_odd(x):
#     if x % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# # main program
# result = print_even_odd(3)
# print(result)  # None


##############
#  SLIDE 8
##############
# def return_multiple_values():
#     return "Hello", 123, ['a', 'b', 'c']


# result = return_multiple_values()
# print(type(result))  # <class 'tuple'>
# print(result)  # ('Hello', 123, ['a', 'b', 'c'])
# var_1, var_2, var_3 = result  # tuple unpacking
# print(var_1, var_2, var_3)  # Hello 123 ['a', 'b', 'c']


##############
#  SLIDE 10
##############
# def f(a, b, c):
#     print(id(a), id(b), id(c))
#     print(a, b, c)

# x = 1
# y = "hello"
# z = [1, 2, 3]

# print(id(x), id(y), id(z))

# f(x, y, z)


##############
#  SLIDE 11
##############
# def print_person(age, name):
#     print(f'Age: {age}, Name: {name}')

# # function calls
# print_person(30, "John")
# print_person("John", 30)  # probably not what you wanted


##############
#  SLIDE 12
##############
# def print_person(age: int, name: str) -> None:
#     print(f'Age: {age}, Name: {name}')

# print(print_person.__annotations__)


# #############

# def capitalize_list(var_list: List[str]) -> List[str]:
#     tmp_list = []
#     for item in var_list:
#         tmp_list.append(item.upper())
#     return tmp_list


# print(capitalize_list.__annotations__)


# #############
#  SLIDE 12
# #############
# def f(a, b, c):
#     print(a, b, c)

# f(c=[1, 2, 3], a=1, b="hello")      # OK: Any order
# # f(a=1, b="hello", c=[1, 2, 3], d=4) # TypeError
# # f(c=[1, 2, 3], a=1)                 # Wrong number of arguments
# f(1, c=[1, 2, 3], b="hello")        # OK: a=1
# # f(1, b=[1, 2, 3], "hello")          # SyntaxError


##############
#  SLIDE 14
##############
# def print_greeting(name, greeting="Hello"):
#     print(greeting, name)


# print_greeting("John")           # Hello John
# print_greeting("John", "HELLO")  # HELLO John

##############
#  SLIDE 15
##############
# def f(my_list=[]):
#     my_list.append('a')
#     return my_list

# print(f([1, 2])) # OK: [1, 2, 'a']
# print(f())       # OK: ['a']

# print(f())  # ['a']
# print(f())  # ['a', 'a']
# print(f())  # ['a', 'a', 'a']

##############
#  SLIDE 16
##############
# def f(my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append('a')
#     return my_list

# print(f()) # ['a']
# print(f()) # ['a']
# print(f()) # ['a']
# print(f([1, 2])) # OK: [1, 2, 'a']

### Slide 17 Exercise #######
# def multiply(*args):
#     total = 1
#     for x in args:
#         total *= x
#     print(f"Multiply total is {total}")
#     return total

# def add(*args):
#     total = 0
#     for x in args:
#         total += x
#     print(f"Add total is {total}")
#     return total

# multiply (2, 2)
# multiply(1, 2, 3, 6, 8)

# add(2, 2, 3, 4, 2, 2, 2, 5)

##############
#  SLIDE 19
##############
# def f(*args):
#     print(args)
#     print(type(args), len(args))
#     for x in args:
#         print(x)

# f(1, 2, 3)
# f('a', [1, 2], 10)


##############
#  SLIDE 21
##############
# def f(x, y, z):
#     print(f'x = {x}')
#     print(f'y = {y}')
#     print(f'z = {z}')

# my_tup = (1, 'a', [1, 'a'])
# f(*my_tup) # equivalent to f(1, 'a', [1, 'a'])

##############
#  SLIDE 22
##############
# def f(*args): #argument unpacking
#     for arg in args:
#         print(arg)

# my_tup = (1, 'a', [1, 'a'])
# f(*my_tup) #tuple packing


##############
#  SLIDE 23
##############
# def f(**kwargs):
#     print(kwargs) #{'a': 1, 'b': 2, 'c': 3}
#     print(type(kwargs)) #<class 'dict'>
#     for key, val in kwargs.items():
#             print(key, ':', val)
#                 # a : 1
#                  # b : 2
#                 # c : 3
# f(a=1, b=2, c=3)


##############
#  SLIDE 24
##############
# def f(a, b, c):
#     print(F'a = {a}')
#     print(F'b = {b}')
#     print(F'c = {c}')


# d = {'a': 1, 'b': 2, 'c': 3}
# f(**d) # equivalent to f(a=1, b=2, c=3)

##############
#  SLIDE 25
##############
# def f(**kwargs):
#     for key, val in kwargs.items():
#             print(key, '->', val)

# d = {'a': 1, 'b': 2, 'c': 3}
# f(**d) # equivalent to f(a=1, b=2, c=3)


##############
#  SLIDE 26
##############
# def f(a, b, *args, **kwargs):
#     print(F'a = {a}')
#     print(F'b = {b}')
#     print(F'args = {args}')
#     print(F'kwargs = {kwargs}')

# f(1, 2, 'a', 'b', 'c', 'd', x=10, y=20, z=30)

##############
#  SLIDE 28
##############
# def f(fx):
#     print(id(fx))
#     fx = 10
#     print(id(fx))

# x = 5
# print(id(x))
# f(x)
# print(x)  # 5


# #############
#  SLIDE 29
# #############
# def f(flist1, flist2, fx):
#     flist1.append(3)  # in-place modification
#     flist1[0] = 4     # in-place modification
#     flist2 = []       # rebinding
#     fx = 0            # rebinding
#     return flist2, fx

# list1 = [1, 2]
# list2 = [3, 4]
# x = 5

# print(list1, list2, x)  #[1, 2] [3, 4] 5
# f(list1, list2, x)
# list2, x = f(list1, list2, x) #4, 2, 3] [] 0
# print(list1, list2, x)  #[4, 2, 3] [3, 4] 5

##############
#  SLIDE 31
##############
# def f(flist1, flist2, fx):
#     flist1.append(3)  # in-place modification
#     flist1[0] = 4     # in-place modification
#     flist2 = []       # rebinding
#     fx = 0            # rebinding

# list1 = [1, 2]
# list2 = [3, 4]
# x = 5

# print(list1, list2, x)  #[1, 2] [3, 4] 5
# f(list1, list2, x)
# print(list1, list2, x)  #[4, 2, 3] [] 0

##############
#  SLIDE 32
##############
# def outer_function():
#     print("outer")

#     def inner_function():
#         print("inner")

#     # function call
#     inner_function()


# # function call
# outer_function()  # outer
#                   # inner
# inner_function()  # NameError: name 'inner_function' is not defined


##############
#  SLIDE 36
##############
# def outer():
#     var = 100

#     def inner():
#         nonlocal var
#         var = var + 1
#         print(var)
#         # return var2

#     inner()
#     print(var)

# outer() # UnboundLocalError: local variable 'var' referenced before assignment

##############
#  SLIDE 37
##############
# print(dir()) # dir() is called in the global scope
# var = 10
# print(dir())

##############
#  SLIDE 38
##############
# var = 10

# def double_value():
#     return var * 2  # OK

# def increment_value():
#     global var
#     var = var + 1  # UnboundLocalError

# # main program
# print(double_value())  # 20
# print(var)             # 10
# increment_value()
# print(var)

##############
#  SLIDE 39
##############
# var = [1, 2, 3]

# def modify_list():
#     var.append(4)

# # main program
# modify_list()
# print(var) # [1, 2, 3, 4]


##############
#  SLIDE 43
##############
# triangle = {"Sides": {"A": None, "B": None, "C": None},
#             "Type": None}

# def build_triangle():
#     a, b, c = input("Enter the length of each side of a triangle: ").split()
#     a = float(a)
#     b = float(b)
#     c = float(c)

#     triangle["Sides"]["A"] = a
#     triangle["Sides"]["B"] = b
#     triangle["Sides"]["C"] = c

#     if a == b == c:
#         triangle["Type"] = "Equilateral"
#     elif a != b and a != c and b != c:
#         triangle["Type"] = "Scalene"
#     else:
#         triangle["Type"] = "Isosceles"

# build_triangle()
# print(triangle)

##############
#  SLIDE 45
##############
# triangle = {"Sides": {"A": None, "B": None, "C": None},
#             "Type": None
#             }

# def prompt_triangle_sides():
#     a, b, c = input("Please enter the three sides of a triangle: ").split()
#     a = float(a)
#     b = float(b)
#     c = float(c)

#     return a, b, c

# def set_triangle_data(a, b, c):
#     triangle["Sides"]["A"] = a
#     triangle["Sides"]["B"] = b
#     triangle["Sides"]["C"] = c

#     if a == b == c:
#         triangle["Type"] = "Equilateral"
#     elif a != b and a != c and b != c:
#         triangle["Type"] = "Scalene"
#     else:
#         triangle["Type"] = "Isosceles"

# def update_triangle():
#     a, b, c = prompt_triangle_sides()
#     set_triangle_data(a, b, c)

# update_triangle()
# print(triangle)


##############
#  SLIDE 48 " First-Class Functions"
##############
# def f():
#     print("executing my_function")


# print("Hello", f, 1)

# my_list = ["Hello", f, 1]
# print(my_list[1])
# my_list[1]()

# my_dict = dict([('Hello', 1), (f, 2), (1, 3)])
# print(my_dict[f])

##############
#  SLIDE 49 "Outer is higher-oder function"
##############
# def inner():
#     print("inner function called")


# def outer(function): #higher-oder function
#     print("outer function called")
#     function()


# outer(inner)


##############
#  SLIDE 50
##############
# nato_phonetics = ["alfa", "zulu", "uniform", "india"]
# # print(sorted(nato_phonetics))  # ['alfa', 'india', 'uniform', 'zulu']

# # print(sorted(nato_phonetics, key=len)  # ['alfa', 'zulu', 'india', 'uniform']

# # print(sorted(nato_phonetics, reverse=True)) # ['zulu', 'uniform', 'india', 'alfa']

# def reverse_len(input_list): return -len(input_list)
# print(sorted(nato_phonetics, key=reverse_len))  #['uniform', 'india', 'alfa', 'zulu']
    
# # print (reverse_len(nato_phonetics))
# for item in new_list

##############
#  SLIDE 51
##############


# def outer():
#     print("outer() executed")

#     def inner():
#         print("inner() executed")
#     return inner


# f = outer()  # outer() executed and returns inner, which is stored in f
# f()          # inner() executed

# # without intermediate assignment
# outer()()

##############
#  SLIDE 55
##############
# def double(a):
#     return 2 * a


# lambda x: x * 2

##############
#  SLIDE 56
#############
# print((lambda x: x * 2)(3)) # 6

# double = lambda x: x * 2
# print(double(3)) # 6

##############
#  SLIDE 57
##############
# person = lambda first, last: f'{first.capitalize()}, {last.capitalize()}'
# print(person('guido', 'van rossum'))


##############
#  SLIDE 58
##############
# import dis

# # lambda expression
# add_numbers = lambda x, y: x + y
# dis.dis(add_numbers)

# print()
# # standard function
# def add(x, y):
#     return x + y

# dis.dis(add)

##############
#  SLIDE 60
##############

# print((lambda x, y, z: x + y + z)(1, 2, 3)) #6

# print((lambda x, y, z=3: x + y + z)(1, 2))  #6

# print((lambda *args: sum(args))(1,2,3)) #6

# print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2))    #3

##############
#  SLIDE 62
##############
'''Filters an iterable based on condition.'''
# sequence = [1, 24, 8, 7, 5, 4, 3, 11, 0, 7]


# # def my_filter(a):
# #     if a > 4:
# #         return a


# filtered_answer = filter(lambda x: x > 4, sequence)
# print(type(filtered_answer))    #<class 'filter'>
# print(list(filtered_answer))  # [24, 8, 7, 5, 11, 7]

##############
#  SLIDE 63
##############
'''Map goes through each item in a an iterable.'''

# sequence = [2, 2, 3, 4, 24]
# squared_result = map(lambda x: x*x, sequence)
# print(type(squared_result)) #<class 'map'>
# print(list(squared_result)) # [4, 4, 9, 16, 576]

##############
#  SLIDE 64
##############
# sequence = [1, 2, 3, 4]
# sum_result = reduce(lambda x, y: x+y, sequence)
# #(((1+2)+3)+4) = 10
# print(type(sum_result)) #<class 'int'>
# print(sum_result) # 10