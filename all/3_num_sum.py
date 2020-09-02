

# the sum of 3 nums in the list should be equal to a target number, return them in sorted array or empty if none



target = 24
random_list = [12,3,4,1,6,9]


pair_list = [(random_list[x],random_list[y],random_list[z]) for x in range(len(random_list))\
        for y in range(x+1, len(random_list)) for z in range(y+1,len(random_list))]

print('We have a random list: {}\n'.format(random_list))

print('\nAll combinations of the Random List, now made in a Paired List: ')

print(pair_list)

print('\nIndex 0 from the new Paired list: ')

print(pair_list[0])

print('\nAll the sums of the different pairs from the new paired list: ')

sum_pairs = [sum(x) for x in pair_list]
print(sum_pairs)


print('\nWe will now find if the sum of some 2 pairs is equal to our Target: ')

for x in pair_list:
    if sum(x) == target:
        print('We found the pair, equal to {} ---> {} = {}'.format(target,x,target))
    else:
        pass





