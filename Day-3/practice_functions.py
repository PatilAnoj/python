#Create a function that: Takes a string,Returns count of vowels

def Vouels_count(sentence):
    vowel_count={'a':0,'e':0,'i':0,'o':0,'u':0}
    for word in sentence:
        if word in vowel_count:
            vowel_count[word]=vowel_count[word]+1
    print(vowel_count)
Vouels_count("hello world")

#average of numbers from a list

def avg(list1):
    sum=0
    for digit in list1:
        sum=sum+digit
    return int(sum/len(list1))
print(avg([10, 20, 30]))


#Password Length Validation

def length_validation(str):
    if(len(str)>=8):
        return True
    else:
        return False
print(length_validation("Password123"))
print(length_validation("pass123"))



