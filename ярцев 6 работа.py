from functools import wraps
def cast(type_):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                casted_result = type_(result)
            except (ValueError, TypeError):
                casted_result = result
            return casted_result
        return wrapper
    return decorator
@cast(int)
def add(a, b):
    return a + b
print(add(1, 2))
print(add("1", "2")) 
print(add("1", "2a"))  