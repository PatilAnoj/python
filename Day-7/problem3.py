#Detect duplicate API calls

def find_duplicate_requests(request_ids):
    request_dict=dict()
    for request in request_ids:
        if request not in request_dict:
            request_dict[request]=1
        else:
            request_dict[request]+=1
        
    list1=[]
    for request in request_dict:
        if request_dict[request]>1:
            list1.append(request)
    return list1

print(find_duplicate_requests(["req1", "req2", "req1", "req3", "req2"]))

#time complexity bigO(m+n) m for finding frequency and n for list generation of duplicates
#space complexity bigO(m+n) m for the dictionary and n for the list
