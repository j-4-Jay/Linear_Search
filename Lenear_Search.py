'''
Given an array... and a target number to find from array...
find the index of the target number.

'''
# ! test comment
array = [1,2,4,3,5,6,7,8,9,10]
target = 91
for i in array:

    if i == target:
        print(f'The number is Present in the array at the {array.index(i+1)} position')
        break
    
print(f'The number is NOT Present in the array')