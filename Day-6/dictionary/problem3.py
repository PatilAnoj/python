#find key with maximum value

def key_with_max_value(input):
    max_Value=float('-inf')
    key=''
    for pair in input:
        if input[pair]>max_Value:
            max_Value=input[pair]
            key=pair
    return key

print(key_with_max_value({"a": 10, "b": 25, "c": 15}))