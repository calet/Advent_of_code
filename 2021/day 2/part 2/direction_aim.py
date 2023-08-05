'''
Using this new interpretation of the commands, calculate the horizontal position and depth 
you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
#answer: 1727785422
with open('input.txt') as f:
    position = f.readlines()

directions = {'horizontal position': 0, 'aim': 0, 'depth': 0}

all_directions = []

for direction in position:
    all_directions.append(direction.rstrip())

for direction in all_directions:  
    space = direction.find(" ") 
    direct = direction.replace(direction[space:], '')
    direct_amount = int(direction.replace(direction[:space], ''))
    
    if direct == 'forward':
        print(f"going forward: {direct_amount}")
        directions['horizontal position'] += direct_amount
        print(f"aim increase on depth: {directions['aim']} * {direct_amount} =  {(directions['aim'] * direct_amount)}")
        print(f"depth: {(directions['aim'] * direct_amount)} + {directions['depth']} = {(directions['aim'] * direct_amount + directions['depth'])}")
        directions['depth'] += (directions['aim'] * direct_amount)

    if direct == 'up':
        print(f"going up: {direct_amount}")
        print(f"aim: {directions['aim']} - {direct_amount} =  {(directions['aim'] - direct_amount)}")
        directions['aim'] += -direct_amount
        print(f"depth: {directions['depth']} - {direct_amount} =  {(directions['depth'] - direct_amount)}")
        #directions['depth'] += -direct_amount 

    if direct == 'down':
        print(f"going down: {direct_amount}")
        print(f"aim: {directions['aim']} + {direct_amount} =  {(directions['aim'] + direct_amount)}")
        directions['aim'] += direct_amount
        print(f"depth: {directions['depth']} + {direct_amount} =  {(directions['depth'] + direct_amount)}")
        #directions['depth'] += direct_amount 
      
    print(f"my new position: {directions}\n")

horizontalTimesDepth = directions['horizontal position'] * directions['depth']

print(f"horizontal amount times depth: ", horizontalTimesDepth)