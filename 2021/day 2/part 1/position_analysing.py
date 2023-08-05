'''
Calculate the horizontal position and depth you would have after following the planned course. 
What do you get if you multiply your final horizontal position by your final depth?
'''
#answer: 1840243


with open('input.txt') as f:
    position = f.readlines()

directions = {'forward': 0, 'up': 0, 'down': 0}

all_directions = []

for direction in position:
    all_directions.append(direction.rstrip())
for direction in all_directions:  
    space = direction.find(" ") 
    direct = direction.replace(direction[space:], '')
    direct_amount = int(direction.replace(direction[:space], ''))
    
    if direct == 'forward':
        print(f"going forward: {direct_amount} amount!!!")
        directions['forward'] += direct_amount
    if direct == 'up':
        print(f"going up: {direct_amount} amount!!!")
        if directions['down'] == 0:
            directions['up'] += direct_amount 
        else:
            directions['down'] += -direct_amount
    if direct == 'down':
        print(f"going down: {direct_amount} amount!!!")
        if directions['up'] == 0:
            directions['down'] += direct_amount 
        else:
            directions['up'] += -direct_amount
    print(f"my new position: {directions}\n")

horizontalTimesDepth = directions['forward'] * directions['down']

print(f"horizontal amount times depth: ", horizontalTimesDepth)