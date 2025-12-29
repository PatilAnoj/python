#merge dictionaries safely
import copy

def merge_dictionaries(dict1,dict2):
    merged_dict=copy.deepcopy(dict1)
    for key in dict2:
        if key not in dict1:
            merged_dict[key]=dict2[key]
        else:
            merged_dict[key]=merged_dict[key]+dict2[key]
    return merged_dict

print(merge_dictionaries({"a": 10, "b": 20},{"b": 5, "c": 15}))
