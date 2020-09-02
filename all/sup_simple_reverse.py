
# given a string or ints --> print it backwards
# 1st row is Array or String --> mean you need to enter only integers or only strings
# in: String / Ellyis --> out: siyllE

a = input('type a word: Array or String: ').lower()

b = []
if a == 'array':
    b = list(map(int,input('enter nums: ').strip().split()))
    b.reverse()

elif a == 'string':
    b = input('strings: ')
    b = b[::-1]


else:
    print('enter only Array or String')


print('your options are: ')
print(a)
print(b)
