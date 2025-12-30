#API Request Validation

def validate_request(data):
    if "email" not in data:
        return "Missing Field:email"
    if "age" not in data:
        return "Missing Field:age"
    if "country" not in data:
        return "Missing Field:country"
    if  (not isinstance(data["email"],str) or '@' not in data["email"]):
        return 'Invalid email'
    if  (not isinstance(data["age"],int) or not(18<=data['age']<=60)):
        return 'Invalid age'
    if (not isinstance(data["country"],str) or data["country"].strip()=="" ):
        return "Invalid country"
    return "VALID"

data = {
    "email": "user@gmail.com",
    "age": 45,
    "country": "japan"
}
print(validate_request(data))

#time complexity bigO(1)
#space complexity bigO(1)


