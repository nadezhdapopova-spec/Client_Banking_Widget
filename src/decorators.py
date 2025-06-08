from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")


def log(filename: str | None = None) -> Any:
    """Декоратор для логирования работы функций в файл или консоль"""
    def wrapper(func: Callable[F_Spec, F_Return]) -> Callable[F_Spec, F_Return]:
        @wraps(func)
        def inner(*args: F_Spec.args, **kwargs: F_Spec.kwargs) -> F_Return:

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok\n")
                        file.write(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. "
                                   f"Result: {result}\n\n")

                        return result

                    except Exception as e:
                        file.write(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n\n")
                        raise e
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"\n{func.__name__} ok")
                    print(f"Function {func.__name__} called with args: {args} and kwargs: {kwargs}. "
                          f"Result: {result}\n")

                    return result

                except Exception as e:
                    print(f"{func.__name__} error: {e} Inputs: {args}, {kwargs}\n")
                    raise e
        return inner
    return wrapper
