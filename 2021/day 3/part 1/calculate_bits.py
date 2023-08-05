'''
power consumption = gamma rate * epsilon rate
gamma rate:
-most common bit in all numbers
epsilon rate
-least common bit in all numbers
'''
#answer: 3882564
store_bits = []
with open('input.txt') as f:
    all_bits = f.readlines()
    for bit in all_bits:
        store_bits.append(bit.rstrip())

gamma = ''
epsilon = ''

#rotates bits in store bits
rotated_bits = []
my_bit = ''
place = 0
while place != len(store_bits[0]):
    for item in store_bits:
        bit = item[place]
        my_bit+=bit
    
    rotated_bits.append(''.join(my_bit))
    my_bit=''
    place+=1

#counts 0s and 1s in bits   
for bit in rotated_bits:
    zeros = bit.count('0')
    ones = bit.count('1')

    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    elif ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        count_0 = 0
        count_1 = 0
        for n in bit:
            if n == '0':
                count_0 += 1
                if count_0 == 3:
                    gamma += '0'
                    epsilon += '1'
                    break
            if n == '1':
                count_1 += 1
                if count_1 == 3:
                    gamma += '1'
                    epsilon += '0'
                    break
                
#translates the binary gamma and epsilon to decimal numbers
count_gamma = int(gamma, 2)
count_epsilon = int(epsilon, 2)
power_consumption = count_gamma*count_epsilon
print("gamma:", count_gamma)
print()
print("epsilon:", count_epsilon)
print()
print("power consumption:", power_consumption)