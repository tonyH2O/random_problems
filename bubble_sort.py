

# if 1st element of a list > from the 2nd --> place 1st on the position of 2nd, and ... until list is sorted


a = [5,7,11,2]

print('unsorted: ')
print(a)

for x in range(len(a)-1):
    for y in range(0,len(a)-x -1):
        if a[y] > a[y+1]:
            a[y],a[y+1] = a[y+1],a[y]

print('bubble sort algorithm sorting: ')

for x in range(len(a)):
    print(a[x])
    
