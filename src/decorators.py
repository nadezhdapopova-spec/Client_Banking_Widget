from functools import wraps


def log(filename: str=None) -> callable:
    """Декоратор для логирования работы функций в файл или консоль"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. "
                                   f"Result: {result}\n\n")

                    except Exception as e:
                        file.write(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n\n")

            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"\n{func.__name__} ok")
                    print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. "
                          f"Result: {result}\n")

                except Exception as e:
                    print(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n")

            return result
        return inner
    return wrapper
