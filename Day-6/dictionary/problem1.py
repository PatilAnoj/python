#Count frequency of words

def count_frequency(input):
    stringy=input.strip()
    word=''
    dict1=dict()
    for index,letter in enumerate(stringy):
        if letter !=' ':
            word+=letter
        if(letter==' ' or index==len(stringy)-1):
            if word.lower() not in dict1:
                dict1[word.lower()]=1
            else:
                dict1[word.lower()]+=1
            word=''
    return dict1

print(count_frequency("this is python Python is this not is python"))