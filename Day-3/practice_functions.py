#Create a function that: Takes a string,Returns count of vowels

def count_vowels(sentence):
    count=0
    vowels='aeiouAEIOU'
    for word in sentence:
        if word in vowels:
           count=count+1
    return count
print(count_vowels("hello world"))

#average of numbers from a list

def calculate_averages(list1):
    total=0
    for digit in list1:
        total=total+digit
    return total/len(list1)
print(calculate_averages([10, 20, 30]))


#Password Length Validation

def is_valid_password(password):
    return len(password)>=8
print(is_valid_password("Password123"))
print(is_valid_password("pass123"))



