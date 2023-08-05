'''
Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
'''
#answer 1516

with open('input.txt') as f:
    measurement = f.readlines()

increase = []
all_measurements = []
calculations = []

for measure in measurement:
    all_measurements.append(int(measure.rstrip()))

while len(all_measurements) != 2:
    #take out 3 numbers
    first = all_measurements.pop(0)
    second = all_measurements.pop(0)
    third = all_measurements.pop(0)

    #add them together and add into a list of sums
    calculate = first+second+third
    calculations.append(calculate)
    print(f"{first} + {second} + {third} = {calculate}")

    if len(calculations) < 2:
        #adds the first sum to increase (no sums before it to compare with)
        print(f"adding: {calculations[-1]} to increase\n")
        increase.append(calculations[-1])
    else:
        print(f"{calculations[-1]} - {calculations[-2]} = {calculations[-1] - calculations[-2]}\n")
    
        #checks if last sum in list of sums is bigger than the sum before it
        if calculations[-1] > calculations[-2]:
            print(f"adding: {calculations[-1]} to increase\n")
            increase.append(calculations[-1])    

    #puts the second and third number back into measurement list for further calculations
    if len(all_measurements) != 2:
        all_measurements.insert(0, third)
        all_measurements.insert(0, second)
        

print(all_measurements)
print(f"lenght of original list: {len(all_measurements)}")
print(f"increase: {len(increase)}")