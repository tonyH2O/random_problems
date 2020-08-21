

#take 2 floats in 1 line on input
#make them to be A and B --> A*B , print the result
# example: 42.42 13.37 --> 567.1554

a,b = map(float,input('give me 2 floats separated by space on this line: ').split())
print(a)
print(b)

c = a*b
print( '{} * {} = {}'.format(a,b,c))
