#Username Validation
import re
def is_valid_username(username,existing_users):
    pattern='^[a-z0-9_]+$'
    if not 3<len(username)<20:
        return False
    if not re.match(pattern,username):
        return False
    if username in set(existing_users):
        return False
    return True

print(is_valid_username("ana",["ayush_jwala","kejriwal123","modi_1234","thala_hukka234"]))
print(is_valid_username("thala_hukka234",["ayush_jwala","kejriwal123","modi_1234","thala_hukka234"]))
print(is_valid_username("Modi_nars",["ayush_jwala","kejriwal123","modi_1234","thala_hukka234"]))
print(is_valid_username("krrish_ganna",["ayush_jwala","kejriwal123","modi_1234","thala_hukka234"]))

#time complexity bigO(n) as every thing is done in constant operation
#space complexity bigO(n) since our username doesn't need extra space 
#username in set(existing_users) → O(n) to build set

#Regex match → O(len(username))
    