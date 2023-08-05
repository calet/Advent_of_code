'''
Calculate the horizontal position and depth you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
#answer: 1840243

def open_file():
    with open('input.txt') as f:
        position = f.readlines()
        for direction in position:
            all_directions.append(direction.rstrip())

'''replace spaces to split between direction and amount'''
def replace_space(all_directions, directions):
    for direction in all_directions:  
        space = direction.find(" ") 
        direct = direction.replace(direction[space:], '')
        direct_amount = int(direction.replace(direction[:space], ''))
        calculate(directions, direct, direct_amount)

'''calculates direction'''
def calculate(directions, direction, direct_amount):
    if direction == 'forward':
        directions['forward'] += direct_amount
        print_forward(directions, direct_amount)

    elif direction == 'up':
        if directions['depth'] > 0:
            directions['depth'] -= direct_amount
        else:
            print("you are at sea level!!")
        print_up(directions, direct_amount)

    elif direction == 'down':
        directions['depth'] += direct_amount
        print_down(directions, direct_amount)

'''prints directions'''
def print_forward(directions, direct_amount):
    print(f"going forward: {direct_amount}")
    print_position(directions)

def print_up(directions, direct_amount):
    print(f"going up: {direct_amount}")
    print_position(directions)

def print_down(directions, direct_amount):
    print(f"going down: {direct_amount}")
    print_position(directions)

'''prints position'''
def print_position(directions):
    print(f"my new position: {directions}\n")

directions = {'forward': 0, 'depth': 0}
all_directions = []

open_file()
replace_space(all_directions, directions)

horizontalTimesDepth = directions['forward'] * directions['depth']
print(f"horizontal amount times depth: ", horizontalTimesDepth)