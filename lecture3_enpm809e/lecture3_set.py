

##################
# # --- SLIDE 58
##################
# ur10={}
# print (ur10)
# x={(1,2,3)}
# print (x)

# ur10 = {"base", "shoulder"}
# x = {(1, 2, 3)}

# print(ur10, x)

# ur10 = set(["base", "shoulder"])
# print(ur10)

# my_list = [1 ,2, 3, 4, 3]
# my_set = set(my_list)
# print (my_set)

# empty = set()
# print(empty)

# even = set(range(0, 10, 2))
# print(even)

# square_tup = (1, 4, 9, 16, 4)
# square_set = set(square_tup)
# print(square_set)

# greeting = "Hello"
# characters = set(greeting)
# print(characters)

# mixed_set = {42, 'foo', (1, 2, 3), 3.14159}
# print(mixed_set)

# print({"Hello"})
# print(set("Hello"))

##################
# # --- SLIDE 59
##################
# ur10 = {"base", "shoulder", "elbow", "wrist1", "wrist2", "wrist3"}

# # # get elements of a set
# for link in ur10:
#     print(link)


##################
# # --- SLIDE 60
##################
# ur10 = {"base"}
# ur10.add("shoulder")
# print(ur10)


# ur10 = set()
# ur10.add("base")  # OK

# ur10 = {}
# ur10.add("base")  # AttributeError

##################
# # --- SLIDE 63
##################
# set1 = {0, 2, 4, 6, 8}
# set2 = {4, 6, 8, 10}
# list1 = [4, 6, 8, 10]
# print(set1.union(set2))  # {0, 2, 4, 6, 8, 10}
# print(set1 | set2)       # {0, 2, 4, 6, 8, 10}
# print(set1.union(list1))  # {0, 2, 4, 6, 8, 10}
# print(set1 | list1)      # TypeError

##################
# # --- SLIDE 64
##################
# set1 = {0, 2, 4, 6, 8}
# set2 = {4, 6, 8, 10}
# set1.update(set2)
# print(set1)       # {0, 2, 4, 6, 8, 10}

##################
# # --- SLIDE 65
##################
# set1 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
# set2 = {1, 4, 9, 16, 25, 36}
# set3 = {16, 17, 18, 19}
# print(set1.intersection(set2))        # {16, 4}
# print(set1 & set2)                    # {16, 4}

# print(set1.intersection(set2, set3))  # {16}
# print(set1 & set2 & set3)             # {16}


##################
# # --- SLIDE 66
##################
# set1 = {0, 16, 2, 4, 6, 8, 10, 12, 14, 18}
# set2 = {1, 4, 9, 16, 25, 36}
# set1.intersection_update(set2)
# print(set1)        # {16, 4}

##################
# # --- SLIDE 68 EXERCISES
##################
# x = ["a", "a", "b", "b", "c", "d", "d", "e"]

# # # write code here
# x=sorted(list(set(x)))

# print(x)  # ['a', 'b', 'c', 'd', 'e']

# x = {'a', 'b'}  #set
# lst = ['a', 'b', 'c', 'd']  #list

# # write code here
# x.update(lst)


# print(x)  # {'a', 'b', 'c', 'd'}
