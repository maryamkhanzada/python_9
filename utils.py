from functools import wraps

def log_action(action):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] {action}")
            return func(*args, **kwargs)
        return wrapper
    return decorator