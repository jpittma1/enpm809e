# #  --- SLIDE 7
# def add_numbers(a, b):
#     return a + b


# print(type(add_numbers))  # <class 'function'>

# my_var = add_numbers
# print(my_var(1, 2))  # 3

# #  --- SLIDE 8


# def increment(number):
#     return number + 1


# def operate(func, x):
#     result = func(x)  # call func and store its returned value
#     return result


# print(operate(increment, 3))  #4

# #  --- SLIDE 9


# def outer_function():
#     def inner_function():
#         print("Hello World")
#     return inner_function


# my_var = outer_function()  # similar to my_var = inner_function

# my_var()  # inner_function()
#             # Hello World


# #  --- SLIDE 11

# def decorate(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner


# def print_hello():
#     print("Hello")


# # Let's decorate print_hello()
# decorated_function = decorate(print_hello)
# decorated_function()

# # I got decorated
# # Hello

# #  --- SLIDE 12

# def decorate(func):
#     def wrapper():
#         print("I got decorated")
#         func()
#     return wrapper


# def print_hello():
#     print("Hello")


# # Let's decorate print_hello()
# decorated_function = decorate(print_hello)
# decorated_function()

# # I got decorated
# # Hello

# #  --- SLIDE 13

# def decorate(func):
#     def wrapper():
#         print("I got decorated")
#         func()
#     return wrapper


# @decorate #syntatic sugar version so is always decorated
# def print_hello():
#     print("Hello")


# print_hello()

# #  --- SLIDE 14


# def divide_smartly(func):
#     def wrapper(a, b):
#         print(f"Dividing {a} and {b}")
#         if b == 0:
#             print("Cannot divide")
#             return
#         return func(a, b)
#     return wrapper


# @divide_smartly
# def divide(x, y):
#     print (x/y)
#     return x/y


# # var = divide_smartly(divide)  # this returns wrapper
# # var(10, 2)  # calls wrapper(10, 2) which returns 5

# divide(1,3)
# divide(1,0)
# divide(10,2)
# #  --- SLIDE 15

# def call_twice(func):
#     def wrapper(a):
#         func(a)
#         func(a)
#     return wrapper


# @call_twice
# def print_string(s):
#     print(s)


# @call_twice
# def print_hello():
#     print('Hello')


# print_string('Hi')
# print_hello()  # TypeError: wrapper() missing 1 required positional argument: 'a'


# #  --- SLIDE 17

# def create_stars(func):
#     def wrapper(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return wrapper


# def create_dashes(func):
#     def wrapper(*args, **kwargs):
#         print("-" * 30)
#         func(*args, **kwargs)
#         print("-" * 30)
#     return wrapper


# @create_stars
# @create_dashes
# def print_hello():
#     print('Hello')


# print_hello()

# printer_hello = create_stars(create_dashes(print_hello))
# create_dashes_wrapper = create_dashes(print_hello)
# # create_dashes_wrapper()
# create_stars_wrapper = create_stars(create_dashes_wrapper)
# create_stars_wrapper()

# print("*"*60)
# print("\n\nPrinter Hello")
# printer_hello()
# print("*"*60)
