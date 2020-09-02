

# compare x with the middle element
# if x > mid --> x is on the right
# applt again..


def bin(a,low,high,x):

    if high >= low:
        mid = (high + low) // 2
        if a[mid] == x:
            return mid

        elif a[mid] > x:
            return bin(a,low,mid-1,x)
        else:
            return bin(a,mid+1,high,x)

    else:
        return -1


a = [2,3,4,10,40]
low = 0
high = len(a) -1
x = 10

b = bin(a,low,high,x)

if b != -1:
    print('the element is in the index: {}'.format(str(b)))
else:
    print('the element is not in the array')




