##################
# # --- SLIDE 33
##################
# ur10_tup = ('base', 'shoulder', 'elbow')
# print(ur10_tup)  # ('base', 'shoulder', 'elbow')

# ur10_list = ['base', 'shoulder']
# ur10_tup = tuple(ur10_list)
# print(ur10_tup)  # ('base', 'shoulder')

# ur10_tup = 'base', 'shoulder', 'elbow'
# print(ur10_tup)  # ('base', 'shoulder', 'elbow')

# ur10 = ('base')
# print(type(ur10))  # <class 'str'>

# # add a comma
# ur10 = ('base',)
# print(type(ur10))  # <class 'tuple'>

# ur10 = 'base',
# print(type(ur10))  # <class 'tuple'>


##################
# # --- SLIDE 34
##################
# ur10 = ('base', 'shoulder', 'elbow')
# print(ur10[-1])
# print(ur10[1:])
# link1, link2, link3 = ur10
# print(link1, link2, link3)  # base shoulder elbow
# # link1, link2, link3, link4 = ur10  # ValueError: not enough values to unpack

# _,link2, _ = ur10
# print(link2) #shoulder
# print(_) #elbow

##################
# # --- SLIDE 36
##################

# ur10 = ('base', 'shoulder', 'elbow')
# ur10[0] = "Base"  # TypeError: 'tuple' object does not support item

# ur10 = (['base', 'shoulder'], 'elbow')
# ur10[0][0] = "BASE"  # OK
# print(ur10)  # (['BASE', 'shoulder'], 'elbow')

# ur10 = ('base', 'shoulder', 'elbow')
# del ur10[0]  # TypeError: 'tuple' object doesn't support item deletion
# del ur10[1:]  # TypeError: 'tuple' object doesn't support item deletion
# del ur10
# print(ur10)
