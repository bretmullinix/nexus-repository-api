import base64



def get_base64_string(value):
    value_bytes = value.encode('ascii')
    base64_bytes = base64.b64encode(value_bytes)
    base64_value = base64_bytes.decode('ascii')
    return base64_value