# The Fibonacci

# solution 1

a,b = 0,1

for x in range(0,10):
    print(a)
    a,b = b,a+b
    

# solution 2



def fib(n):
    
    def __init__(self,n):
        self.n = n
    a,b = 0,1
    
    while n <= 0:
        n = int(input('Please enter a positive whole number, bigger than 0 and 1: '))

    for x in range(0,n):
        yield '{}: {}'.format(x+1,a)
        a,b = b,a+b
        

x = int(input('Enter a positive number: '))
f = fib(x)
for y in f:
    print(y)

# print out the N-th number from the Fibonacci sequence exampale input: 6 --> output: 5 from a 0,10 sequence


a,b = 0,1
n = int(input('enter the N-th number you want to receive from the Fib SSequence: '))
c = []

for x in range(0,10):
    c.append(a)
    a,b = b,a+b

print(c)
print('Here is your N-th number you requested: \n')
print(c[n-1])
