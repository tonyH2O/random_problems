

# given a list of nums, find the num that is second largest ( the list can contain duplicate numbers )
# in: 2 3 6 6 5 ---> out: 5



n = int(input('how many nums you need?: '))
a = []

for x in range(0,n):
    n = int(input('num: '))
    a.append(n)

print('current list: ')
print(a)

b = set(a)
b.remove(max(b))
print('we will now remove the biggest nums in the list, so current list is: ')
print(b)

print('here is the second best that is now left as first in the list: ')
sorted(b)
print(max(b))


