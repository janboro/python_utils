from typing import Any, Callable


def db_retry(stop: int) -> Any:
    def decorator(function: Callable) -> Any:
        def wrapper(self, *args, **kwargs) -> Any:
            for _ in range(stop):
                try:
                    return function(self, *args, **kwargs)
                except Exception as e:
                    print(e)
                    self.reset()

        return wrapper

    return decorator
