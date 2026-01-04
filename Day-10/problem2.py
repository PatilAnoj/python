#Query Simulation (Filtering)

def get_users_by_domain(users, domain):
    filtered_users=[user for user in users if user["email"].endswith(domain) ]
    return filtered_users

def search_users_by_username(users, keyword):
    matching_usernames=[]
    for user in users:
        if keyword.lower() in user["username"].lower():
            matching_usernames.append(user["username"])
    
    return matching_usernames

