def authenticate_request(headers):
    if "authorization" not in headers:
        return "401 : unauthorized"
    token = headers["authorization"]

    if token !="valid-token":
        return "401 :Unauthorized"
    
    return "200 ok"