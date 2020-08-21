

# check if a string can be read same way forward and backwards


a = 'hoh'

a = a.casefold()
print(a)


b = reversed(a)



if list(a) == list(b):
    print('the string {} is palindrome'.format(a))

else:
    print('not a palindrome')


