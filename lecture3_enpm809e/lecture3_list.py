import copy

##################
# # --- SLIDE 10
##################
# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2", "wrist3"]
# print(ur10)
# print(type(ur10))

##################
# # --- SLIDE 11
##################
# ur10 = list()  # []
# print(ur10)
# print(type(ur10))

# link = "base"
# ur10 = list(link)  # ['b', 'a', 's', 'e']
# print(ur10)

# link = "base"
# ur10 = list([link])  # ['base']
# print(ur10)

# link = ["base"]
# ur10 = list(link)  # ['base']
# print(ur10)

##################
# # --- SLIDE 12
##################

# # for loop
# square_list = []

# for number in range(1, 11):
#     square_list.append(number * number)
# print(square_list)

# # list comprehension
# square_list = [number * number for number in range(1, 11)]
# print(square_list)

##################
# # --- SLIDE 13
##################
# sentence = 'Have you got anything without spam?'
# vowel_list = [char for char in sentence if char in 'aeiouy']
# print(vowel_list)

##################
# # --- SLIDE 14
##################
# numbers = [3, 4, -5, 45, -55]
# numbers = [n if n > 0 else 0 for n in numbers]
# print(numbers)

##################
# # --- SLIDE 15
##################
# matrix = [
#     [0, 0, 0, 0],
#     [1, 1, 1, 1],
#     [2, 2, 2, 2],
#     [3, 3, 3, 3],
# ]

# # with list comprehension
# flattened = [num for row in matrix for num in row]
# print(flattened)

# # with a for loop
# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
# print(flat)

##################
# # --- SLIDE 16
##################
# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2", "wrist3"]
# print(ur10[2])    # elbow
# print(ur10[-2])   # wrist2
# print(ur10[2:4])  # ['elbow', 'wrist1']

# ########## exercise###########
# nested_list = ['a', 'b', ['c', 'd', ['e', 'f']]]

#long hand
# var1=nested_list[2]
# var2=var1[2]
# var3=var2[0]
# print(var3)

 #short hand
# print(nested_list[2][2][0])

##################
# # --- SLIDE 17
##################
# ur10 = ["base", "shoulder", "elbow", "wrist2"]

# # modify the last element
# ur10[-1] = "wrist_2"
# print(ur10)  # ['base', 'shoulder', 'elbow', 'wrist_2']

# # convert the last element to uppercase
# ur10[-1] = ur10[-1].upper()
# print(ur10)  # ['base', 'shoulder', 'elbow', 'WRIST_2']

# ur10[1:3] = ["wrist1"]  #replaces items 1-3 with "wrist_1"
# print(ur10)  # ['base', 'wrist1', 'WRIST_2']

# ur10[:] = range(3)
# print(ur10)  # [0, 1, 2]


##################
# # --- SLIDE 18
##################
# ur10 = ["shoulder"]

# ur10.append("wrist1")
# print(ur10)  # ['shoulder', 'wrist1']

# ur10 = ["shoulder"]
# ur10.insert(1, "elbow")
# print(ur10)
# ur10.insert(0, "base")
# print(ur10)  # ['base', 'shoulder', 'elbow']

# ur10 = ["shoulder"]
# ur10.extend(["wrist2", "wrist3"])
# print(ur10)  # ['shoulder', 'wrist2', 'wrist3']


##################
# # --- SLIDE 19
##################
# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2"]
# ur10.remove("base")
# print(ur10)  # ['shoulder', 'elbow', 'wrist1', 'wrist2']

# print(ur10.pop())  # wrist2
# print(ur10)  # ['shoulder', 'elbow', 'wrist1']

# del ur10[0]
# print(ur10)  # ['elbow', 'wrist1']

# ur10.clear()
# print(ur10)  # []


##################
# # --- SLIDE 20
##################
# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2"]
# ur10.remove("base")  # ['shoulder', 'elbow', 'wrist1', 'wrist2']
# ur10.remove("base")  # ValueError

# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2"]
# del ur10[0]  # ['shoulder', 'elbow', 'wrist1', 'wrist2']
# del ur10
# print(ur10)  # NameError: name 'ur10' is not defined


##################
# # --- SLIDE 21
##################
# ur10 = ["base", "shoulder"]
# ur10_copy = ur10

# ur10.append('elbow')
# print(ur10)       # ['base', 'shoulder', 'elbow']
# print(ur10_copy)  # ['base', 'shoulder', 'elbow']

# ur10_copy.append('wrist1')
# print(ur10)       # ['base', 'shoulder', 'elbow', 'wrist1']
# print(ur10_copy)  # ['base', 'shoulder', 'elbow', 'wrist1']


##################
# # --- SLIDE 22
##################
# old_list = [[1, 2], [3, 4]]
# new_list = copy.copy(old_list)  # shallow copy

# print(old_list)  # [[1, 2], [3, 4]]
# print(new_list)  # [[1, 2], [3, 4]]

# old_list.append([5, 6])

# print(old_list)  # [[1, 2], [3, 4], [5, 6]]
# print(new_list)  # [[1, 2], [3, 4]]

##################
# # --- SLIDE 23
##################
# old_list = [[1, 2], [3, 4]]
# new_list = copy.copy(old_list)  # shallow copy

# print(old_list)  # [[1, 2], [3, 4]]
# print(new_list)  # [[1, 2], [3, 4]]
# old_list.append([5, 6])
# old_list[0][0] = 0

# print(old_list)  # [[0, 2], [3, 4], [5,6]]
# print(new_list)  # [[0, 2], [3, 4]]


##################
# # --- SLIDE 24
##################

# old_list = [[1, 2], [3, 4]]
# new_list = list(old_list)  # shallow copy

# print(old_list)  # [[1, 2], [3, 4]]
# print(new_list)  # [[1, 2], [3, 4]]

# old_list.append([5, 6])
# old_list[0][0] = 0

# print(old_list)  # [[0, 2], [3, 4], [5, 6]]
# print(new_list)  # [[0, 2], [3, 4]]


##################
# # --- SLIDE 25
##################
# old_list = [[1, 2], [3, 4]]


# new_list = copy.deepcopy(old_list)  # deep copy

# print(old_list)  # [[1, 2], [3, 4]]
# print(new_list)  # [[1, 2], [3, 4]]

# old_list.append([5, 6])
# old_list[0][0] = 0

# print(old_list)  # [[0, 2], [3, 4], [5, 6]]
# print(new_list)  # [[1, 2], [3, 4]]

##################
# # --- SLIDE 28
##################
# # + operator
# links1 = ["base", "elbow", "wrist1"]
# links2 = ["shoulder", "wrist3"]
# ur10 = links1 + links2
# # print(ur10) # ['base', 'elbow', 'wrist1', 'shoulder', 'wrist3']

# # append()
# links1 = ["base", "elbow", "wrist1"]
# links2 = ["shoulder", "wrist3"]

# for item in links2:
#     links1.append(item)
# print(links1)   # ['base', 'elbow', 'wrist1', 'shoulder', 'wrist3']

# # extend()
# links1 = ["base", "elbow"]
# links2 = ["wrist1", "wrist2"]
# links1.extend(links2)
# print(links1)


##################
# # --- SLIDE 29
##################

#.sort does not return anything and does not store in a variable
# ur10 = ["elbow", "wrist1", "base"]
# ur10.sort()   #does not return anything and does not store in a variable
# print(ur10)  # ['base', 'elbow', 'wrist1']
# ur10.sort(reverse=True)
# print(ur10)  # ['wrist1', 'elbow', 'base']

# ur10 = ["elbow", "wrist1", "base"]
# sorted_list = sorted(ur10)
# print(ur10)        # ["elbow", "wrist1", "base"]
# print(sorted_list)  # ['base', 'elbow', 'wrist1']

##################
# # --- SLIDE 30
##################
# lst = [0, 1, [2, 3]]
# print(lst.pop().pop())  #3

# lst = ['1', '2', '3']
# print(lst[1:])  #['2', '3']

# ur10 = ["base", "elbow"]
# greeting = "hello"
# ur10.extend(greeting)   #['base', 'elbow', 'h', 'e', 'l', 'l', 'o']
# print(ur10)
# ur10.pop()
# ur10.pop()
# ur10.pop()
# ur10.pop()
# ur10.pop()
# ur10.append(greeting)
# print(ur10) #['base', 'elbow', 'hello']

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)  #['apple', 'banana', 'mango']

# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2"]
# del ur10[1:4]
# print(ur10) #['base', 'wrist2']


##  In-class Quiz
# lst=[0,1,[2,3]]
# print(lst.pop().pop()) #3

# lst=['1','2','3']
# print(lst[1:])  #['2', '3']

# ur10 = ["base", "elbow"]
# greeting = "hello"
# ur10.extend(greeting)
# print(len(ur10))    #7

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)  #['apple', 'banana', 'mango']


# ur10 = ["base", "shoulder", "elbow", "wrist1", "wrist2"]
# # new_ur10=ur10[1:3]
# ur10[1:3]=[]    
# print(ur10) #['base', 'wrist1', 'wrist2']

