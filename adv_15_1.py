
'''
--- Day 1: Not Quite Lisp ---

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor -
the directions he got are a little confusing. He starts on the ground floor (floor 0)
and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
        ))((((( also results in floor 3.
            ()) and ))( both result in floor -1 (the first basement level).
                ))) and )())()) both result in floor -3.
            To what floor do the instructions take Santa?


###Part Two

Now, given the same instructions, find the position of the first character that
causes him to enter the basement (floor -1). 
The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.
    What is the position of the character that causes Santa to first enter the basement?

'''

def santa(a):

    b = []
    c = 0

    for x in a:
        b.append(x)

    for x in b:
        if x == '(':
            c +=1
        elif x == ')':
            c -=1

        else:
            return 'error'

    
    return 'Santa currently is on floor: {}'.format(c)


def santa2(a):
    b = []
    c = 0

    for x in a:
        b.append(x)

    for x,y in enumerate(b):
        if y == '(':
            c+=1
        
        elif y == ')':
            c-=1

        if c == -1:
            c = x+1
            return 'Santa entered the basement at character position: {}'.format(c)



a = input('give me list of ( or ) signs: ')

print(santa(a))
print(santa2(a))
