#Reverse list without using .reverse()

def reverse_list(input):
    if len(input)<=1:
        return input
    j=len(input)-1
    i=0
    while(i<=j):
        temp=input[i]
        input[i]=input[j]
        input[j]=temp
        i=i+1
        j=j-1
    return input

print(reverse_list(["this","is","python"]))