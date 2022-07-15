# def main():
#     print("hello")
    
# print("outside main")


if __name__ == "__main__":
    # main()
    
    # print ('*' * 10)
    
    # text = "My age is "
    # age = 25
    # print(text)
    # print (age)
    # print(text * age) # prints text 25 times
    
    # l1=[1,2,3]
    # print(id(l1))
    # # print(id([1,2,3]))
    
    # l1=[1,2,3, 6, 7, 8]
    # print(id(l1))
    
    # print(5 % 3)  #32: returns remainder
    
    # print(-5 //2) #2: returns division rounded to next number towards negative infinity
    
    # greeting= 'hello '
    
    # name = input("Please enter your name: ")
    
    # print(greeting + name + '!!', type(name))
    
    # age= int(input('Please enter your age: ')   #casting
    
    # print(age, type(age))
    
    # my_string =  "This\nis\nmy\nstring"
    
    # print(my_string)
    
    # my_string2 =  "This\tis\tmy\tstring"
    
    # print(my_string2)
    
    # print("C:\Users\tony\notes.txt")  #error
    
    # print("C:\\Users\\tony\\notes.txt")   #Fix #1: exit backslash
    
    # print(r'C:\Users\tony\notes.txt') #Fix #2: verbatim
    
    # a= r'C:\Users\tony\notes.txt'
    # print(a, id(a))
    
    # print("C:\\\\Users\\tony") #double slashees
    
    # greeting = "Hello!"
    
    # print("Hello"[0])
    
    # print(greeting[2])  #grab the e
    
    # print(greeting[-1])  #grab the !
    
    #######Slicing (slide 36 of lecture 2)##########
    
    # greeting = "Welcome BACK!"
    
    # print(greeting[0:3])  #Wel
    # print(greeting[:7])  #Welcome
    # print(greeting[8:])  #BACK!
    # print(greeting[-5:])  #BACK!
    # print(greeting[-5:-1])  #BACK
    # print(greeting[-5:12])  #BACK
    
    # txt = "Python is fun"
    # print(txt[0:5:2]) #from index 0 up to but not including index 5 at step of 2
    
    #why up to but not included??
    #A: since will use len based on inputs that are dynamic so don't know size of string
    # a= "Welcome"
    # print(a[0:4])
    
    # name = input("Please enter your name: ")
    # #add code to check is a certain size
    
    # print(name[2:len(name)])
    
    # name = "Guido"
    # age= 65
    
    # print("Name is {0} and age is {1} and kid\'s age is {1} ".format(name, age))
    # #OR
    # my_string="Name is {0} and age is {1} and kid\'s age is {1} ".format(name, age)
    
    # print(my_string)
    
    #OR
    # print(f"{name} is {age} years old.")
    
    # name1= "John"
    # name2= "John"
    # # name3 = input("Please enter your name: ")
    # name3 =name2.upper()
    # print(name3)
    
    # # print(id(name1))
    # # print(id(name2))
    # # print(name3)
    # # print(id(name3))   #different ID# since is dynamically created/entered
    
    # name4=name1.title()
    # print(name4)
    
    
    ##########################
    #Exercise
    # letter = ""
    # letter = None
    # score = int(input("Please enter your score: "))
    
    # if score >= 90:
    #     letter = 'A'
    # elif score >= 80:
    #     letter = 'B'
    # elif score >= 70:
    #     letter ='C'
    # elif score >= 60:
    #     letter ='D'
    # else:
    #     letter ='F'
        
    # print(f"Your letter score is: {letter}")
    ##########################
    
    # for c in "hello":
    # print(c)    
    # print(c, end=' ')
    
    # for a in range(25):
    #     print(a, end=', ')
        
    # greeting = "Welcome back, Jerry!"
    
    # for b in range(len(greeting)):
    #     # print(b, end=' ')
    #     print(greeting[b], end='')
        
    # line = "123, 45, abc"
    # line2=
    # for a in range(len(line)):
    #     # print(type(line[a]))
    #     if line[a].ascii_letters is int:
    #         print(line[a], end='')
    
    ######Exercise#########
    # number= '0123456789'
    # line = "123, 45, abc"
    
    # #Student answer
    # for c in line:
    #     if c in number:
    #         print(c, end='')
    
    # print('\n')
    
    # #professor solution
    # number_str = ''
    # for i in range(len(line)):
    #     if line[i] in '0123456789':
    #         number_str = number_str + line[i]
    
    # print(number_str)
    
    # name = 'Jerry'
    # while  name:
    #     name = name.rstrip(name[-1])
    #     print(name)
        
    # name = 'Guido'
    # c='u'
    # i = 0
    
    # while i < len(name):
    #     if name[i]==c:
    #         print(f'{c} was found in {name}')
    #         break
    #     i += 1
    # else:
    #     print(f'{c} not found in {name}')
    
    ###--------Long Exercise---------------#####
    
    #green glass
    #blue book
    #purple pan
    
    puzzle_solved = False
    count=2
    while puzzle_solved == False:
        table=''
        table=input("Which table [g/b/p] should I go to? ")
        
        if table == 'g':
            table ='green'
        elif table == 'b':
            table = 'blue'
        elif table == 'p':
            table = 'purple'
        else:
            print("ERROR: I cannot recognize this table...exit")
            table = False  #reset object
            # print("=" * 20, f"Attempt #{count}", "=" * 20)
            # count+=1
        
        if table:
            object = ''
            object=input(f"Which object [g/b/p] is on the {table} table? ")

            if object == 'g':
                object ='glass'
            elif object == 'b':
                object = 'book'
            elif object == 'p':
                object = 'pan'
            else:
                print("ERROR: I cannot recognize this object...exit")
                object = False #reset object
                # print("=" * 20, f"Attempt #{count}", "=" * 20)
                # count+=1
                
            if object:
                if object[0] == table[0]: #First letters are the same
                    print(f"OK: I can pick up the {object} from the {table} table")
                    # print(f"Congrats, that only took you {count} attempts!")
                    puzzle_solved == True
                    break
                else:
                    print(f"ERROR: I cannot pick up the {object} from the {table} table")
                    # print("=" * 20, f"Attempt #{count}", "=" * 20)
                    # # print("Try again...")
                    # count+=1