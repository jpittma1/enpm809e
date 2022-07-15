"""
Jerry Pittman, Jr., 117707120, jpittma1@umd.edu
ENPM809E: Python applications to robotics
Summer 2022
RWA1: planner.py
"""
import pprint

"""
Creates Nested Dictionary for Planner

Possible states ("values") of each key
robot_floor: {"is_gripper_empty": True or False,
                        "is_holding_part": True or False},
        robot_ceiling: {"is_gripper_empty": True or False,
                        "is_holding_part": True or False
                        "is_holding_tray": Treu or False},
        red_part: {"bin": None, 1, 2, 3, 4,
                    "number": None, 0, 4, 9},
        green_part: {"bin": None, 1, 2, 3, 4,
                    "number": None, 0, 4, 9},
        blue_part: {"bin": None, 1, 2, 3, 4,
                    "number": None, 0, 4, 9},
        wood_tray: {"location": "wood_tray_table", "gripper", or "agv",
                    "status": "Complete" or "Incomplete",
                    "red_part": 0->2,
                    "blue_part": 0->2,
                    "green_part": 0->2},
        metal_tray: {"location": "metal_tray_table", "gripper", or "agv",
                    "status": "Complete" or "Incomplete",
                    "red_part": 0->2,
                    "blue_part": 0->2,
                    "green_part": 0->2},
        AGV: {"name": None, 1, 2, 3, or 4
                "station_to_be_used": None, 1, 2, 3, or 4,
                "tray_to_be_used": None, 'w', or 'm',
                "location": "staging" or "station"},
        kit: {'red_part': None, 0, 1, or 2,
                'blue_part': None, 0, 1, or 2,
                'green_part': None, 0, 1, or 2,
                'total_number_of_parts': 7, 0, 1, 2, 3, 4, 5, or 6} #Max of 6
"""
rwa1 = {
        'robot_floor': {"is_gripper_empty": True,
                        "is_holding_part": False},
        'robot_ceiling': {"is_gripper_empty": True,
                        "is_holding_part": False,
                        "is_holding_tray": False},
        'red_part': {"bin": None,
                    "number": None},
        'green_part': {"bin": None,
                    "number": None},
        'blue_part': {"bin": None,
                    "number": None},
        'wood_tray': {"location": "wood_tray_table",
                    "status": "Incomplete",
                    "red_part": 0,
                    "blue_part": 0,
                    "green_part": 0},
        'metal_tray': {"location": "metal_tray_table",
                    "status": "Incomplete",
                    "red_part": 0,
                    "blue_part": 0,
                    "green_part": 0},
        'AGV': {"name": None,
                "station_to_be_used": None,
                "tray_to_be_used": None,
                "location": "staging"},
        'kit': {"red_part": None,
                "blue_part": None,
                "green_part": None,
                "total_number_of_parts": 7}
}

# pprint.pprint(rwa1)

def pickup_tray(robot: str, tray: str, table: str):
    """
    `robot` picks up `tray` from `table`

    Note: This function can only be executed if `robot` is 'ceiling_robot'

    Preconditions:
        - `robot` is 'robot_ceiling'
        - `tray` is located on `table`
        - `robot`'s gripper is empty

    Effects:
        - `robot`'s gripper is not empty
        - `robot`'s gripper is holding the tray
        - location of `tray` is not on `table`
        - location of `tray` is in `robot`'s gripper

    Args:
        robot (str): The robot used to perform this action
        tray (str): The tray to pick up ('wood_tray' or 'metal_tray')
        table (str): Table where the tray is located
            ('wood_tray_table' or 'metal_tray_table')
    """
    print(f"pickup_tray({robot}, {tray}, {table})")
    
    ####---Effects: 
    rwa1[robot]["is_gripper_empty"] = False
    rwa1[robot]["is_holding_tray"] = True
    rwa1[tray]["location"] = "gripper"
    # pass


def place_tray(robot: str, tray: str, agv: str):
    """
    `robot` places `tray` on `agv`.

    Note: This function can only be executed if `robot` is 'robot_ceiling'.

    Preconditions:
        - `robot` is 'robot_ceiling'
        - `robot`'s gripper is holding `tray`
        - `tray` is located in `robot`'s gripper
        - location of `tray` is in `robot`'s gripper

    Effects:
        - `robot`'s gripper is empty
        - `robot`'s gripper is not holding `tray`
        - location of `tray` is not in `robot`'s gripper
        - location of `tray` is `agv`

    Args:
        robot (str): The robot used to perform this action
        tray (str): The tray to place on `agv` ('yellow_tray' or 'gray_tray')
        agv (str): AGV where `tray` is placed
            ('agv1', 'agv2', 'agv3', or 'agv4')
    """
    print(f"place_tray({robot}, {tray}, agv{agv})")
    
    ####---Effects: 
    rwa1[robot]["is_gripper_empty"] = True
    rwa1[robot]["is_holding_tray"] = False
    rwa1[tray]["location"] = "agv"
    # pass


def pickup_part(robot: str, bin: str, part: str):
    """
    `robot` picks up `part` from `bin`.

    Preconditions:
        - `robot`'s gripper is empty
        - `bin` has parts of type `part`
        - The number of parts in `bin` is > 0

    Effects:
        - Decrease the number of parts in `bin` by 1
        - `robot`'s gripper is holding `part`
        - `robot`'s gripper is not empty

    Args:
        robot (str): Robot used to perform this action 
            ('robot_ceiling' or 'robot_floor')
        bin (str): Bin from which a part is removed ('bin1', ..., or 'bin4')
        part (str): The part to pick up
            ('red_part', 'green_part', or 'blue_part')
    """
    print(f"pickup_part({robot}, bin{bin}, {part})")
    
    ####---Effects: 
    rwa1[part]["number"] = rwa1.get(part,{}).get("number") - 1
    rwa1[robot]["is_holding_part"] = True
    rwa1[robot]["is_gripper_empty"] = False
    # pass


def place_part(robot: str, tray: str, part: str, agv: str):
    """
    `robot` places `part` in `tray`, which is located on `agv`

    Preconditions:
        - `robot`'s gripper is holding `part`
        -  location of `tray` is `agv`
        - `tray` is not complete

    Effects:
        - `tray` has `part`
        - `robot`'s gripper is not holding `part`
        - `robot`'s gripper is empty

    Args:
        robot (str): Robot used to perform this action
            ('robot_ceiling' or 'robot_floor')
        tray (str): Tray in which `part` is placed
            ('yellow_tray' or 'gray_tray')
        part (str): The part to place
            ('red_part', 'green_part', or 'blue_part')
        agv (str): AGV where `tray` is located.
            ('agv1', 'agv2', 'agv3', or 'agv4')
    """
    print(f"place_part({robot}, {tray}, {part}, agv{agv})")
    
    ####---Effects:
    rwa1[tray][part] = rwa1.get(tray,{}).get(part) + 1
    rwa1[robot]["is_gripper_empty"] = True
    rwa1[robot]["is_holding_part"] = False
    # pass


def ship_agv(agv: str, tray: str, station: str):
    """
    Ship `agv` to assembly station `station` if `tray` is complete

    Preconditions:
        - `tray` is complete (it has all the parts needed)
        - `tray` is on `agv`

    Effects:
        - `agv` location is `station`

    Args:
        agv (str): AGV to ship
            ('agv1', 'agv2', 'agv3', or 'agv4')
        tray (str): Tray located on `agv`
            ('yellow_tray' or 'gray_tray')
        station (str): Assembly station where to ship `agv`
            ('as1', 'as2', 'as3', or 'as4')
  
    """
    print(f"ship_agv(agv{agv}, as{station})")
    
    ####---Effects:
    rwa1["AGV"]["location"] = "station"
    # pass


def get_user_inputs():
    """
    Gets user inputs for Inital and Goal states and updates rwa1 dictionary values accordingly.
        Ensures user inputs are integers for number values and values entered are within allowed options.
        Ensures options displayed are only allowed values and re-prompts user if incorrect values are provided
    """
    print("=" * 80)
    print("\tINITIAL STATE")
    print("=" * 80)
    
    parts_test_list = [0, 4, 9]
    bin_test_list = [1, 2, 3, 4]
    
    #Prompt for # of Red parts until User provides correct value
    while rwa1['red_part']["number"] not in parts_test_list:
        rwa1['red_part']["number"] = int(input("How many red_parts in the workcell [0, 4, 9]? "))
        # print(rwa1['red_part']["number"], type(rwa1['red_part']["number"]))
        
    # Verify Red parts will be used
    if rwa1['red_part']["number"] != 0:
        #Prompt for Red parts bin until User provides correct value
        while rwa1['red_part']["bin"] not in bin_test_list:
            rwa1['red_part']["bin"] = int(input("In which bin are red_parts located [1, 2, 3, 4]? "))

    #Prompt for Green part until User provides correct value
    while rwa1['green_part']["number"] not in parts_test_list:
        rwa1['green_part']["number"] = int(input("How many green_parts in the workcell [0, 4, 9]? "))

    #Prompt for Green parts bin until User provides correct value
    if rwa1['green_part']["number"] != 0:
        '''
        Verify that green parts are !=0 then prompt for green bin
        By making red bin not available for picking
        '''
        while rwa1['green_part']["bin"] not in bin_test_list:
        
            if rwa1['red_part']["bin"] == 1:
                rwa1['green_part']["bin"] = int(input("In which bin are green_parts located [2, 3, 4]? "))
            elif rwa1['red_part']["bin"] == 2:
                rwa1['green_part']["bin"] = int(input("In which bin are green_parts located [1, 3, 4]? "))
            elif rwa1['red_part']["bin"] == 3:
                rwa1['green_part']["bin"] = int(input("In which bin are green_parts located [1, 2, 4]? "))
            else:
                rwa1['green_part']["bin"] = int(input("In which bin are green_parts located [1, 2, 3]? "))
    #END green part bin determination 
    
    #Prompt for Blue part until User provides correct value
    while rwa1['blue_part']["number"] not in parts_test_list:
        rwa1['blue_part']["number"] = int(input("How many blue_parts in the workcell [0, 4, 9]? "))
    
    if rwa1['blue_part']["number"] != 0:    
        '''
        Verify that blue parts are !=0 then prompt for blue bin
        By making red bin and green bin not available for picking
        '''
        while rwa1['blue_part']["bin"] not in bin_test_list:
            
            if rwa1['red_part']["bin"] == None:
                if rwa1['green_part']["bin"] == 1:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 3, 4]? "))
                elif rwa1['green_part']["bin"] == 2:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 3, 4]? "))
                elif rwa1['green_part']["bin"] == 3:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2, 4]? "))
                elif rwa1['green_part']["bin"] == 4:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2, 3]? "))
                else:   #green is None; Unexpected to have two empty bins...
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2, 3, 4]? "))
            
            elif rwa1['red_part']["bin"] == 1:
                if rwa1['green_part']["bin"] == None:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 3, 4]? "))
                elif rwa1['green_part']["bin"] == 2:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [3, 4]? "))
                elif rwa1['green_part']["bin"] == 3:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 4]? "))
                else:   #green is bin4
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 3]? "))
            
            elif rwa1['red_part']["bin"] == 2:
                if rwa1['green_part']["bin"] == 1:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [3, 4]? "))
                elif rwa1['green_part']["bin"] == 3:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 4]? "))
                elif rwa1['green_part']["bin"] == 4:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 3]? "))
                else:   #green is None
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 3, 4]? "))
            
            elif rwa1['red_part']["bin"] == 3:
                if rwa1['green_part']["bin"] == 1:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 4]? "))
                elif rwa1['green_part']["bin"] == 2:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 4]? "))
                elif rwa1['green_part']["bin"] == 4:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2]? "))
                else:   #green is None
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2, 4]? "))
            
            elif rwa1['red_part']["bin"] == 4:
                if rwa1['green_part']["bin"] == 1:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [2, 3]? "))
                elif rwa1['green_part']["bin"] == 2:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 3]? "))
                elif rwa1['green_part']["bin"] == 3:
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2]? "))
                else:   #green is None
                    rwa1['blue_part']["bin"] = int(input("In which bin are blue_parts located [1, 2, 3]? "))
    #END blue part bin determination
       
    print("=" * 80)
    print("\tGOAL STATE")
    print("=" * 80)
    
    tray_test_list = ["w", "m"]
    agv_test_list = [1, 2, 3]
    
    while rwa1['AGV']["tray_to_be_used"] not in tray_test_list:
        rwa1['AGV']["tray_to_be_used"] = input("Which tray to use [(w)ood, (m)etal]? ")
    
    while rwa1['AGV']["name"] not in agv_test_list:
        rwa1['AGV']["name"] = int(input("Which AGV to use [1, 2, 3, 4]? "))
    
    ###---Determine Assembly Station based on AGV to be used--_###
    as_test_list_1_2 = [1, 2]   #AGV1 and 2 can only reach Assembly station 1 and 2
    as_test_list_3_4 = [3, 4]   #AGV3 and 4 can only reach Assembly station 3 and 4
    
    if rwa1['AGV']["name"] == 1:
        while rwa1['AGV']["station_to_be_used"] not in as_test_list_1_2:
            rwa1['AGV']["station_to_be_used"] = int(input("Which assembly station to ship agv1 [1, 2]? "))
    elif rwa1['AGV']["name"] == 2:
        while rwa1['AGV']["station_to_be_used"] not in as_test_list_1_2:
            rwa1['AGV']["station_to_be_used"] = int(input("Which assembly station to ship agv2 [1, 2]? "))
    elif rwa1['AGV']["name"] == 3:
        while rwa1['AGV']["station_to_be_used"] not in as_test_list_3_4:
            rwa1['AGV']["station_to_be_used"] = int(input("Which assembly station to ship agv3 [3, 4]? "))
    else: #AGV is agv4
        while rwa1['AGV']["station_to_be_used"] not in as_test_list_3_4:
            rwa1['AGV']["station_to_be_used"] = int(input("Which assembly station to ship agv4 [3, 4]? "))
    
    ###---Determine number of parts required for Kitting on tray---###
    kit_test_list = [0, 1, 2]

    while rwa1['kit']["total_number_of_parts"] > 6:
        '''Ensures maximum parts <= 6 (maximum parts on a tray)'''
        if rwa1['red_part']["number"] != 0:
            while rwa1['kit']["red_part"] not in kit_test_list:
                rwa1['kit']["red_part"] = int(input("How many red_parts in tray [0, 1, 2]? "))
        else:
            rwa1['kit']["red_part"] = 0
        
        if rwa1['green_part']["number"] != 0:
            while rwa1['kit']["green_part"] not in kit_test_list:
                rwa1['kit']["green_part"] = int(input("How many green_parts in tray [0, 1, 2]? "))
        else:
            rwa1['kit']["green_part"] = 0
        
        if rwa1['blue_part']["number"] != 0:
            while rwa1['kit']["blue_part"] not in kit_test_list:
                rwa1['kit']["blue_part"] = int(input("How many blue_parts in tray [0, 1, 2]? "))
        else:
            rwa1['kit']["blue_part"] = 0
        
        rwa1['kit']["total_number_of_parts"] = rwa1['kit']["red_part"] + rwa1['kit']["green_part"] + rwa1['kit']["blue_part"]
        print ("Total parts in a kit are: ", rwa1['kit']["total_number_of_parts"])
    #END parts for each kit
    
    print("=" * 80)

def generate_plan():
    """
    Generates a plan based on initial and goal states.
        Tests for Pre-conditions prior to each function call.
        Prints completion of each action when applicable function is called.
        Each function updates the applicable dictionary value as the state changes of the 'part', 'gripper'
            of 'robot', 'tray' location, and amount of 'part' on applicable 'tray'.
    STEP 1) Gets User inputs to update Dictionary while testing they are valid
    
    STEP 2) moves tray to table
    
    STEP 3) picks up applicable parts with applicable robot to applicable table located on applicable AGV
    
    STEP 4) moves applicable AGV to applicable assembly station
    """
    get_user_inputs()
    
    ###---Test for Solution possible based on required versus available parts of given color---####
    red_kit_required = rwa1.get('kit',{}).get("red_part")
    red_parts_available = rwa1.get('red_part', {}).get("number")
    green_kit_required = rwa1.get('kit',{}).get("green_part")
    green_parts_available = rwa1.get('green_part', {}).get("number")
    blue_kit_required = rwa1.get('kit',{}).get("blue_part")
    blue_parts_available = rwa1.get('blue_part', {}).get("number")
    
    if red_kit_required > red_parts_available:
        print("=" * 80)
        print("\tNO SOLUTION FOUND - Not enough red_parts")
        print("=" * 80)
    elif green_kit_required > green_parts_available:
        print("=" * 80)
        print("\tNO SOLUTION FOUND - Not enough green_parts")
        print("=" * 80)
    elif blue_kit_required > blue_parts_available:
        print("=" * 80)
        print("\tNO SOLUTION FOUND - Not enough blue_parts")
        print("=" * 80)
    else:
        print("=" * 80)
        print("\tSOLUTION FOUND!")
        print("=" * 80)
        
        current_robot = "robot_ceiling"
        
        ####---Pickup Tray---###
        '''Set "initial_table" variable to be the location of the correct tray'''
        if rwa1['AGV']['tray_to_be_used'] == "w":
            initial_table = rwa1['wood_tray']["location"]
            tray_used = "wood_tray"
        elif rwa1['AGV']['tray_to_be_used'] == "m":
            initial_table = rwa1['metal_tray']["location"]
            tray_used = "metal_tray"
        
        if (rwa1['wood_tray']["location"] == "wood_tray_table" or rwa1['metal_tray']["location"] == "metal_tray_table") \
            and rwa1['robot_ceiling']["is_gripper_empty"] == True and current_robot == "robot_ceiling":
            
            pickup_tray(current_robot, tray_used, initial_table)
        
        ####---Place tray on AGV---###
        active_AGV = rwa1['AGV']["name"]
        
        if rwa1[tray_used]["location"] == "gripper"  and rwa1['robot_ceiling']["is_holding_tray"] == True and current_robot == "robot_ceiling":        
            place_tray(current_robot, tray_used, active_AGV)
        
        current_red = 0
        current_green = 0
        current_blue = 0
        current_kit = 0
        robot_floor_test_list = [1, 2]  #robot_floor can only access bins 1 and 2
        robot_ceiling_test_list = [3, 4]    #robot_ceiling can only access bins 3 and 4
        
        while current_kit < rwa1['kit']["total_number_of_parts"]:
            
            ####---Pick up red part(s)---###
            red_bin = rwa1.get('red_part', {}).get("bin")
            red_parts_in_bin = rwa1.get('red_part', {}).get("number")
            part_to_place = "red_part"
            red_in_kit = rwa1[tray_used][part_to_place]
            # print(f" Red bin is bin{red_bin}, red_parts_in_bin{red_bin} is {red_parts_in_bin}, red needed in_kit is {red_in_kit}")
            
            #Test that parts in workcell is not 0 (i.e. not required for kit)
            if red_parts_in_bin != 0:
                if red_bin in robot_floor_test_list:
                    current_robot = "robot_floor"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and red_parts_in_bin > 0:
                        pickup_part(current_robot, red_bin, part_to_place)
                    
                    ####---Place red part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        current_red = red_in_kit
                elif red_bin in robot_ceiling_test_list:
                    current_robot = "robot_ceiling"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and red_parts_in_bin > 0:
                        pickup_part(current_robot, red_bin, part_to_place)
                    
                    ####---Place red part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        current_red = red_in_kit
                else:
                    continue
            
            ####---Pick up green part(s)---###
            green_bin = rwa1.get('green_part', {}).get("bin")
            green_parts_in_bin = rwa1.get('green_part', {}).get("number")
            part_to_place = "green_part"
            green_in_kit = rwa1[tray_used][part_to_place]
            # print(f" Green bin is {green_bin}, green_parts_in_bin is {green_parts_in_bin}, green_in_kit is {green_in_kit}")

            #Test that parts in workcell is not 0 (i.e. not required for kit)
            if green_parts_in_bin != 0:
                if green_bin in robot_floor_test_list:
                    current_robot = "robot_floor"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and green_parts_in_bin > 0:
                        pickup_part(current_robot, green_bin, part_to_place)
                    
                    ####---Place green part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        current_green = green_in_kit
                elif green_bin in robot_ceiling_test_list:
                    current_robot = "robot_ceiling"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and green_parts_in_bin > 0:
                        pickup_part(current_robot, green_bin, part_to_place)
                    
                    ####---Place green part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        current_green = green_in_kit
                else:
                    continue
            
            ####---Pick up blue part(s)---###
            blue_bin = rwa1.get('blue_part', {}).get("bin")
            blue_parts_in_bin = rwa1.get('blue_part', {}).get("number")
            part_to_place = "blue_part"
            blue_in_kit = rwa1[tray_used][part_to_place]
            # print(f" blue bin is {blue_bin}, blue_parts_in_bin is {blue_parts_in_bin}, blue_in_kit is {blue_in_kit}")
            
            #Test that parts in workcell is not 0 (i.e. not required for kit)
            if blue_parts_in_bin != 0:  
                if blue_bin in robot_floor_test_list:
                    current_robot = "robot_floor"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and blue_parts_in_bin > 0:
                        pickup_part(current_robot, blue_bin, part_to_place)
                    
                    ####---Place blue part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        # current_blue +=1
                        current_blue = blue_in_kit
                elif blue_bin in robot_ceiling_test_list:
                    current_robot = "robot_ceiling"
                    
                    if rwa1.get(current_robot, {}).get("is_gripper_empty") == True and blue_parts_in_bin > 0:
                        pickup_part(current_robot, blue_bin, part_to_place)
                    
                    ####---Place blue part(s)---###
                    if rwa1.get(current_robot, {}).get("is_holding_part") == True and rwa1.get(tray_used, {}).get("location") == "agv" \
                        and rwa1.get(tray_used, {}).get("status") == "Incomplete":
                        
                        place_part(current_robot, tray_used, part_to_place, active_AGV)
                        # current_blue +=1
                        current_blue = blue_in_kit
                else:
                    continue
            
            current_kit = current_red + current_green + current_blue
            # print(f"Current Kit is: {current_kit} containing {current_red} red, {current_green} green, and {current_blue} blue")
            
        ####---Mark appropriate Tray Complete---###
        if current_kit == rwa1['kit']["total_number_of_parts"] and rwa1['kit']["total_number_of_parts"] <= 6:
            rwa1[tray_used]["status"] = "Complete"
        
        ####---Ship AGV to AS---###
        assembly_station = rwa1['AGV']["station_to_be_used"]
        
        if rwa1[tray_used]["status"] == "Complete" and rwa1[tray_used]["location"] == "agv":
            ship_agv(active_AGV, tray_used, assembly_station)
        
        print("=" * 80)