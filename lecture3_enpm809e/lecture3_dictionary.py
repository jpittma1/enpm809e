import pprint

##################
# # --- SLIDE 38
##################
# robot = {
#     "TurtleBot3": "mobile",
#     "UR10": "industrial",
#     "Gapter": "aerial"
# }

# print(type(robot))
# print(robot)

##################
# # --- SLIDE 40
##################

# def test():
#     # return 2
#     return "hello", "hi"

# robot = {
#     "TurtleBot3": "mobile",
#     "UR10": "industrial",
#     "Gapter": "aerial",
#     "TurtleBot3": "aerial",
#     "greeting": "hello",
#     1: "integer",
#     2.5: "float",
#     int: "type",
#     test(): "type",
#     True: True,
#     (1, 2, 3): (1, 2, 3),
#     # [1, 2, 3]: "mutable objects can't be keys",  # TypeError
# }

# print(robot)

##################
# # --- SLIDE 41
##################
# robot = {  # top level dictionary
#     "TurtleBot3": {  # another dictionary
#         "Max Trans Velocity": "0.22 m/s",
#         "Max Rot Velocity": "2.84 rad/s",
#         "Max payload": "15 Kg",
#         "Size": {  # another dictionary
#             "L": 138,
#             "W": 178,
#             "H": 192,
#         }
#     },
#     "Kobuki": {  # another dictionary
#         "Max Trans Velocity": "70 cm/s",
#         "Max Rot Velocity": "180 deg/s",
#         "Max payload": {  # another dictionary
#             "Hard Floor": "5 Kg",
#             "Carpet": "4 Kg"
#         }
#     }
# }

# pprint.pprint(robot)


##################
# # --- SLIDE 44
##################

# # -------------------------
# # dict(**kwargs)
# # -------------------------
# empty = dict()
# numbers = dict(x=5, y=0)

# print(empty)
# print(numbers)

# # -------------------------
# # dict(mapping, **kwargs)
# # -------------------------
# numbers1 = dict({'a': 4, 'b': 5})  # this version is overkill
# numbers2 = dict({'a': 4, 'b': 5}, c=3, d=4)

# print(numbers1)
# print(numbers2)

# # -------------------------
# # dict(iterable, **kwargs)
# # -------------------------
# # without keyword argument
# numbers1 = dict([('x', 5), ('y', -5)])  # list of tuples
# # keyword argument is also passed
# numbers2 = dict([('x', 5), ('y', -5)], z=8)  # list of tuples + keyword argument

# print(numbers1)
# print(numbers2)


##################
# # --- SLIDE 45
##################
# bot = {"TurtleBot3": "aerial", "UR10": "industrial"}
# bot["Gapter"] = "aerial"
# bot["TurtleBot3"] = "mobile"  # update the value for the key "TurtlBot3"

# print(bot)

# # -------------------------
# # update()
# # -------------------------
# bot1 = {"TurtleBot3": "aerial", "UR10": "industrial"}
# bot2 = {"TurtleBot3": "mobile", "Kobuki": "mobile"}
# bot1.update(bot2)
# print(bot1)

# bot1 = {"TurtleBot3": "aerial", "UR10": "industrial"}
# bot2 = [('TurtleBot3', "mobile"), ("Kobuki", "mobile")]
# bot1.update(bot2)
# print(bot1)

##################
# # --- SLIDE 46
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}
# print(robot["TurtleBot3"])  # mobile
# print(robot["UR10"])        # industrial

# print(robot.get("TurtleBot3"))    # mobile
# print(robot.get("UR10"))          # industrial
# print(robot.get("UR5"))           # None
# print(robot.get("Banana", "N/A"))  # N/A

# if x is not None:
#     pass

##################
# # --- SLIDE 47
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# keys = robot.keys()  
# # print(keys) ## dict_keys(['TurtleBot3', 'UR10'])

# for key in keys:
#     print(key)  #TurtleBot3
#                 #UR10

# # -----------

# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# for key in robot:
#     print(key)

##################
# # --- SLIDE 48
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# values = robot.values()  # dict_values(['mobile', 'industrial'])

# for value in values:
#     print(value)

# # -----------
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# for key in robot:
#     print(robot[key])

##################
# # --- SLIDE 49
# ##################
# robot = {"Crazyflie": "aerial", "Gapter": "aerial"}

# items = robot.items()
# print(items)  # dict_items([('Crazyflie', 'aerial'), ('Gapter', 'aerial')])
    
# for key, value in items:  # unpack each tuple in the list
#     print(f'{key}: {value}')


##################
# # --- SLIDE 51
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# keys = robot.keys()
# print(keys)  # dict_keys(['TurtleBot3', 'UR10'])

# # Add a new item
# robot["Gapter"] = "aerial"

# # view object is updated
# print(keys)  # dict_keys(['TurtleBot3', 'UR10', 'Gapter'])

# print(id(keys), id(robot.keys()), id(robot))

##################
# # --- SLIDE 53
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# # remove element based on the key and return its value
# value = robot.pop("TurtleBot3")
# print(value)  # 'mobile'
# print(robot)  # {'UR10': 'industrial'}
# print(robot.pop("TurtleBot3", "Key does not exist"))  # Key does not exist
# print(robot.pop("TurtleBot3", None))  # None
# print(robot.pop("TurtleBot3"))  # KeyError: 'TurtleBot3'

##################
# # --- SLIDE 54
##################
# robot = {"TurtleBot3": "mobile", "UR10": "industrial"}

# # remove the last key-value pair added
# removed_item = robot.popitem()
# print(removed_item)  # ('UR10', 'industrial')

# robot["Gapter"] = "aerial"
# # remove the last key-value pair added
# removed_item = robot.popitem()
# print(removed_item)  # ('Gapter', 'aerial')

##################
# # --- SLIDE 55
##################
# robot = {
#     "TurtleBot3": "mobile",
#     "UR10": "industrial",
#     "Gapter": "industrial"
# }

# robot["Gapter"]= "aerial"

# robot["Crazyfile"] = robot.pop("Gapter")    #update "Gapter" to "Crazyfile"

# print(robot)
