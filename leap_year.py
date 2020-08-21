
# calculate if a year is LEAP or not

def leap(x):

    y = False

    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                y = True
                return 'It is {}, the year {} is LEAP'.format(y,x)
            else:
                return '{}...{} is not LEAP'.format(y,x)
        else:
            y = True
            return '()...{} is LEAP'.format(y,x)

    else:
        return '{}...{} is not LEAP'.format(y,x)


a = int(input('give me a year: '))

l = leap(a)
print(l)



