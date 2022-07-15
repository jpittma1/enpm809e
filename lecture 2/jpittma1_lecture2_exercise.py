'''ENPMN809E Summer 2022
Jerry Pittman (117707120)
jpittma1@umd.edu'''

puzzle_solved = False

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
        print("=" * 80)
    
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
            print("=" * 80)
            
        if object:
            if object[0] == table[0]: #First letters are the same
                print(f"OK: I can pick up the {object} from the {table} table")
                puzzle_solved == True
                break
            else:
                print(f"ERROR: I cannot pick up the {object} from the {table} table")
                print("=" * 80)