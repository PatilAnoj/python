#Product Creation Validation

def validate_data_presence(data):
    if not "name" in data:
        raise ValueError("name must pe present")
    if not "price" in data:
        raise ValueError("price must pe present")
    if not "stock" in data:
        raise ValueError("stock must pe present")
    return True

def data_type_validation(data):
    if not isinstance(data["name"],str):
        raise ValueError("name must be string")
    if not isinstance(data["price"],int) or isinstance(data["price"],float):
        raise ValueError("price must be int'\'float")
    if not isinstance(data["stock"],int):
        raise ValueError("stock must be int")
    return True

def range_validation(data):
    if data["name"].strip()=="":
        raise ValueError("name must not be empty")
    if not data["price"]>0:
        raise ValueError("price must be greater then 0")
    if not data["stock"]>=0:
        raise ValueError("stock must not be negative")
    return True

def validate_product(data):
    if validate_data_presence(data) and data_type_validation(data) and range_validation(data):
        return "VALID"
    
#time complexity O(1)
#space constant