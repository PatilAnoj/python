#RATE LIMITER
def is_allowed(user_id,current_time,user_requests):
    if user_id not in user_requests:
        return True
    starting_time=current_time-60
    requests=0
    for request_time in user_requests[user_id]:
        if starting_time<request_time<=current_time:
            requests+=1
    return requests<=3

print(is_allowed("user1",50,{"user1": [10, 20, 30, 40]}))
print(is_allowed("user1",70,{"user1": [10, 20, 30, 40]}))   
print(is_allowed("user2",70,{"user1": [10, 20, 30, 40]}))   

#time complexity: bigO(n)
#space complexity: bigO(1)



    