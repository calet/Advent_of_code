'''
Using this new interpretation of the commands, calculate the horizontal position and depth 
you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
#answer: 1727785422

def open_file(all_directions):
    with open('input.txt') as f:
        position = f.readlines()
        for direction in position:
            all_directions.append(direction.rstrip())

'''replace spaces to split between direction and amount'''
def replace_space(directions):
    for direction in all_directions:  
        space = direction.find(" ") 
        direct = direction.replace(direction[space:], '')
        direct_amount = int(direction.replace(direction[:space], ''))
        if direct == 'forward':
           calculate(directions, direct, direct_amount)
        if direct == 'up':
            calculate(directions, direct, direct_amount)
        if direct == 'down':
            calculate(directions, direct, direct_amount)

def calculate(directions, direction, direct_amount):
    '''calculates the directions for: forward, up and down'''
    if direction == 'forward':
        directions['horizontal position'] += direct_amount
        calculate_aim = (directions['aim'] * direct_amount)
        calculate_depth = (directions['aim'] * direct_amount + directions['depth'])
        directions['depth'] += (directions['aim'] * direct_amount)
        prints_forward(directions, calculate_aim, calculate_depth, direct_amount)

    if direction == 'up':
        directions['aim'] -= direct_amount
        calculate_aim = (directions['aim'] - direct_amount)
        calculate_depth = (directions['depth'] - direct_amount)
        prints_up(directions, calculate_aim, calculate_depth, direct_amount)
    
    if direction == 'down':
        directions['aim'] += direct_amount
        calculate_aim = (directions['aim'] + direct_amount)
        calculate_depth = (directions['depth'] + direct_amount)
        prints_down(directions, calculate_aim, calculate_depth, direct_amount)
   

'''prints the directions for: forward, up and down'''
def prints_forward(directions, calculate_aim, calculate_depth, direct_amount):
    print(f"going forward: {direct_amount}")
    print(f"aim increase on depth: {directions['aim']} * {direct_amount} =  {calculate_aim}")
    print(f"depth: {(directions['aim'] * direct_amount)} + {directions['depth']} = {calculate_depth}")
    prints_new_position(directions)

def prints_up(directions, calculate_aim, calculate_depth, direct_amount):
    print(f"going up: {direct_amount}")
    print(f"aim: {directions['aim']} - {direct_amount} =  {calculate_aim}")
    print(f"depth: {directions['depth']} - {direct_amount} =  {calculate_depth}")
    prints_new_position(directions)

def prints_down(directions, calculate_aim, calculate_depth, direct_amount):
    print(f"going down: {direct_amount}")
    print(f"aim: {directions['aim']} + {direct_amount} =  {calculate_aim}")
    print(f"depth: {directions['depth']} + {direct_amount} =  {calculate_depth}")
    prints_new_position(directions)

def prints_new_position(directions):
    print(f"my new position: {directions}\n")

all_directions = []
directions = {'horizontal position': 0, 'aim': 0, 'depth': 0}

open_file(all_directions)
replace_space(directions)

horizontalTimesDepth = directions['horizontal position'] * directions['depth']

print(f"horizontal amount times depth: ", horizontalTimesDepth)