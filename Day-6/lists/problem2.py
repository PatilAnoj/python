#Find second largest number in list
def second_largest_number(input):
    if len(input)<2 :
        raise ValueError('invalid input must contain at least two elements')
    max1=float('-inf')
    max2=float('-inf')
    for num in input:
        if(num>max1):
            max2=max1
            max1=num
        elif(num<max1 and num>max2):
            max2=num

    if(max2== float('-inf')):
        raise ValueError('no second largest element')
    return max2

print(second_largest_number([1,2,3,4,5,6,7,8,9]))
# print(second_largest_number([5, 5, 5]))
print(second_largest_number([10,10,9]))
print(second_largest_number([2, 1]))
print(second_largest_number([-1, -2, -3]))


            