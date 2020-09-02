
# in1: number
# in2: ASCII symbols as many as in1 number
# "E" - the person / '..' - free path / '#' - obstacle
# depending on "E" position, find the easiest path to freedom
# out: number of how many obstacle you encounter on the shortest path to freedom

# example:
# 8
# ....E..#
# out: 0 obstacles, chosing left path



a = int(input('how many characters you need?: '))
b = input('chars: ')

while len(b) > a or len(b) < a:
    b = input('the chars needs to be {}, enter such amount: '.format(a))

print('\nhere is your escape situation: ')
print(b)

c = list(b)
left = []
right = []

for x,y in enumerate(c):
    if y == 'E':
        left.append(c[:x])
        right.append(c[x+1::])
        print('\n{} is here on position: {}'.format(y,x))

print('\nLeft of E, we have: ')
print(left)
print('\nRight of E, we have: ')
print(right)

counter = 0
counter2 = 0


# because left and right are nested lists now, we dig deeper
for x in left:
    for y in x:
        if y == '#':
            counter +=1
for x in right:
    for y in x:
        if y == '#':
            counter2+=1
print('\nLeft has this much obstacles: ')
print(counter)
print('\nRight has this much obstacles: ')
print(counter2)


if counter > counter2:
    print('E will be free in {} obstacles to the Right side.'.format(counter2))
elif counter == counter2:
    print('E can choose Left or Right side, because there is equal number of obstacles {}'.format(counter))
else:
    print('E will be free in {} obatacles to the Left side'.format(counter))



    



