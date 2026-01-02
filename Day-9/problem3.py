#API Payload Guard (Defensive Backend)

def validate_order_payload(data):
    if data is None or data is {}:
        raise ValueError("payload is empty")
    if not "user_id" in data:
        raise ValueError("user_id not found")
    if not "product_id" in data:
        raise ValueError("product_id not found")
    if not "quantity" in data:
        raise ValueError("quantity not found")
    if not isinstance(data["user_id"],int):
        raise ValueError("user_id must be int")
    if not isinstance(data["product_id"],int):
        raise ValueError("product_id must be int")
    if not isinstance(data["quantity"],int):
        raise ValueError("quantity must be int")
    if not data["user_id"]>0:
        raise ValueError("user_id must be greater than 0")
    if not data["product_id"]>0:
        raise ValueError("product_id must be greater than 0")
    if not data["quantity"]<1:
        raise ValueError("quantity must be greater than or equals to 0")
    return True


def process_order(data):
    validate_order_payload(data)
    return "ORDER PROCESSED"

#time complexity and space both are constant