from functools import wraps

__all__ = (
    'after_finish',
)


def after_finish(after_finish_function):
    def decorator_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            after_finish_function()
            return result

        return wrapper

    return decorator_function
