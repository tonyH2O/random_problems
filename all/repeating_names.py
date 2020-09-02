
# set a number on the 1st line
# give this much names on the next lines

# find the name that is most repeated, there can be many repeated names, we need to most repeated 

from collections import Counter


a = int(input('give me num: '))
d = []
for x in range(a):
    a = input('give me name: ')
    d.append(a)

print(d)


dd = Counter(d)
print(dd.most_common(1)[0][0])



'''
c = [x for x,y in dd.items() if y > 1]
print(c)



c = set([x for x in d if d.count(x) > 1])
print('repeating name is: ')
print(c)

'''



