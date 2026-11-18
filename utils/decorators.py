from functools import wraps
def log_action(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Before Starting Decorator",func.__name__)
        result = func(*args,**kwargs)
    
        print("After completing Decorator",func.__name__)
        return result
    return wrapper

def validate_amount(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if result["amount"] > 0:
            print("Sucessful")
            return result
        elif result["amount"] <= 0:
            print("UnSucessful")
    return wrapper
