'''
How many measurements are larger than the previous measurement?
'''
#answer 1475
all_measurements = []
with open('input.txt') as f:
    measurement = f.readlines()
    for measure in measurement:
        all_measurements.append(int(measure.rstrip()))

increase = []

all_measurements = []
for measure in measurement:
    all_measurements.append(int(measure.rstrip()))

while all_measurements:
    first = all_measurements.pop(0)
    second = all_measurements.pop(0)
    print(f"{second} - {first} = {second-first}")
    if second > first:
        increase.append(second)
        
    if len(all_measurements) != 0:
        all_measurements.insert(0, second)

print(all_measurements)
print(f"lenght of original list: {len(all_measurements)}")
print(f"increase: {len(increase)}")
