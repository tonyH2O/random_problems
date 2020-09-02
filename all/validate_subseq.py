

# given a string, find if it is a subsequence of another string


a = 'abc'
b = 'abced'

a = input('enter string: ')
b = input('enter second string: ')

def validate(x,y):

    m = len(x)
    n = len(y)
    aa = 0
    bb = 0

    while aa < m and bb < n:
        if x[aa] == y[bb]:
            aa += 1
        bb += 1

    return aa == m

if validate(a,b) == True:
    print('{} is a subsequence of {}'.format(a,b))
else:
    print('{} is not a subsequence of {}'.format(a,b))


