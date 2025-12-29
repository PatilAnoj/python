#find common elements between two lists using sets

def common_elements(list1,list2):
    set1=set(list1)
    set2=set(list2)
    return list(set1.intersection(set2))

print(common_elements([1, 2, 3, 4, 4],[3, 4, 5, 6]))