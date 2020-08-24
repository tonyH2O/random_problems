


# we have 1 number N
# find all 3 number sums combinations that are equal to N
# input: 3
# out: 90

# explain: (1*1*1) + (1*1*2) +(1*1*3) + ... = 1+2+3+4+6+9+8+12+18+27 = 90

import itertools

n = int(input('give me num: '))


c = []
for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            b = x*y*z
            c.append(b)
            print('{} * {} * {} = {}'.format(x,y,z,b))
            
print(c)

'''
a = []
for x in range(1,n):
    a.appen(x)
    print(a)

print('all combinations from 1 to N: ')

for x in itertools.permutations(a,n):
    print(x)

print('start the cycle to gather all numbers: ')
c = []
for x in a:
    for y in a:
        for z in a:
            b = x*y*z
            c.append(b)
            #print(b)
'''

print('now create Dict to remove duplicate nums: ')

c = list(dict.fromkeys(c))
print(c)

print('All final sums: ')
print(sum(c))
