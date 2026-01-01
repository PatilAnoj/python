#API request logger
def log_api_requests(requests):
    request_dict=dict()
    for element in requests:
       if element[0] not in request_dict:
           request_dict[element[0]]=dict()
           request_dict[element[0]][element[1]]=1
       else:
           if element[1] not in request_dict[element[0]]:
               request_dict[element[0]][element[1]]=1
           else:
               request_dict[element[0]][element[1]]+=1
    return request_dict

print(log_api_requests([
    ("user1", "/login"),
    ("user1", "/login"),
    ("user2", "/profile"),
    ("user1", "/profile")
]))