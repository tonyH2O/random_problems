

# you have a binary tree as an array [3,6,2,9,-1,10] index[0] is the top Node, all negative integers, should be removed
# size of the branch is the sum of all node values
# return Right is its larger or Left if thats larger
# if they are equal return empty
# append all even nums to right and the rest goes to the left

n = int(input('how many nums you will need?: '))
a = []
for x in range(0,n):
    x1 = int(input('nums: '))
    a.append(x1)

print('the main node is: {}'.format(a[0]))

for x in a:
    if x <=0:
        a.remove(x)
    else:
        pass

left = []
right = []

for x in range(1,len(a),1):
    if x%2 != 0:
        left.append(a[x])
    else:
        right.append(a[x])

print('The left tree: ')
print(left)
print('The Right tree: ')
print(right)

l = sum(left)
r = sum(right)

if l > r:
    print('The sum of the left is: {} and it is bigger than the Right tree --> {}'.format(l,r))
elif r > l:
    print('The sum of the right is: {} and it is larger than the Left tree --> {}'.format(r,l))
else:
    e = []
    print('Left and Right trees are equal, here is an empty list: {}'.format(e))
