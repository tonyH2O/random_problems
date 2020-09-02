

# given a Binary Search Tree with values left and right, find the closest value from the BST Node to an outside given Target value



# BST starting num: 10
# left: 5,2,5
#right: 15,13,22
#target: 12

a = int(input('give me a number of how many inputs you need: '))
b = []

for x in range(0,a):
    nums = int(input('num: '))
    b.append(nums)

c = 10
target = 12
left = []
right = []
for x in b:
    if x < c:
        left.append(x)
        
    elif x == c:
        pass

    else:
        right.append(x)

if target > c:
    right.append(target)
elif target == c:
    pass
else:
    left.append(target)

print('The main node of the BST is: {}'.format(c))
print('The left tree is: {}'.format(left))
print('The right tree is: {}'.format(right))

def find(listt,target):
    if target in listt:
        listt.remove(target)
    closest = listt[0]
    for x in range(1,len(listt)):
        if abs(listt[x] - target) < (abs(closest - target)):
            closest = listt[x]
    return closest

f = find(left,target)
f2 = find(right,target)

if target in left:
    print('The target number {} is in the Left node'.format(target))
    left.sort()
    print('The closest number to our target number {} is ---> {}'.format(target,f))
    
    
else:
    print('The target number {} is in the Right node'.format(target))
    right.sort()
    print('The closest number to our target number {} is ---> {}'.format(target,f2))











