def oxygen_generator_rating(data, ones, zeros, increment):
    temp_oxygen_list = data[:]
    for bit in data:
        if len(temp_oxygen_list) == 1:
            print(f"(binary) last oxygen bit: {''.join(temp_oxygen_list)}")
            return int(temp_oxygen_list[0], 2)
        if ones > zeros:
            if bit[increment] != '1':
                temp_oxygen_list.remove(bit)
        elif zeros > ones:
            if bit[increment] != '0':
                temp_oxygen_list.remove(bit)
        else:
            if bit[increment] != '1':
                temp_oxygen_list.remove(bit)
    return temp_oxygen_list
#when you remove from list the index amount gets lower,
#meaning it jumps over numbers and dont delete everything it should.
def CO2_scrubber_rating(data, ones, zeros, increment):
    temp_CO2_list = data[:]
    for bit in data:
        if len(temp_CO2_list) == 1:
            print(f"(binary) last CO2 bit: {''.join(temp_CO2_list)}")
            return int(temp_CO2_list[0], 2)
        if ones < zeros:
            if bit[increment] != '1':
                temp_CO2_list.remove(bit)
        elif zeros < ones:
            if bit[increment] != '0':
                temp_CO2_list.remove(bit)
        else:
            if bit[increment] != '0':
                temp_CO2_list.remove(bit)
    return temp_CO2_list

with open('input.txt', 'r') as f:
    data = f.readlines()

oxygen = data[:]
increment = 0
co2 = data[:]
#-2 because while loops always do one final loop when it
#gets to a target unless you break it.
while increment < (len(data[0])-1):
    ones = 0
    zeros = 0
    for bit in co2:
        if bit[increment] == '0':
            zeros+=1
        else:
            ones+=1

    #message = f"time {increment}:\nzeros: {zeros}\nones: {ones}"
    #print(message)
    #print("-"*len(message), '\n')
    last_CO2_bit = CO2_scrubber_rating(co2, ones, zeros, increment)
    increment+=1
    co2 = last_CO2_bit
    try:
        if int(co2):
            break
    except:
        continue
increment = 0
#-2 because while loops always do one final loop when it
#gets to a target unless you break it.
while increment < (len(data[0])-1):
    ones = 0
    zeros = 0
    for bit in oxygen:
        #print(f"bit increment: {increment}, bit: {bit}, bit index: {bit[increment]}")
        if bit[increment] == '0':
            zeros+=1
        else:
            ones+=1

    #message = f"time {increment}:\nzeros: {zeros}\nones: {ones}"
    #print(message)
    #print("-"*len(message), '\n')
    last_oxygen_bit = oxygen_generator_rating(oxygen, ones, zeros, increment)
    #print(f"lenght: {len(last_oxygen_bit)}, last oxygen bit: {last_oxygen_bit}")
    increment+=1
    oxygen = last_oxygen_bit
    try:
        if int(oxygen):
            break
    except:
        continue

life_support_rating = oxygen * co2
print(f"(decimal) last CO2 bit: {co2}")
print("")
print(f"(decimal) last oxygen bit: {oxygen}")
print("")
print(f"life support rating: {life_support_rating}")
print("----finished----")
