

# given a list of integers, find N largest integers from it
# input - [4,5,1,2,9] output 3 --> 9,5,4



n = int(input('give me N numbers: '))
a = []

for x in range(0,n):
    n = int(input('nums: '))
    a.append(n)

n1 = int(input('how many largest nums do you need from that list?: '))

print(a)
a.sort()
print(a)
b = a[::-1]
print(b)

print('here are the 3 largest numbers from the {} list'.format(b))
while n1:
    print(b[0:n1])
    break
        
    

