from functools import wraps
import time
from typing import Callable
from typing import Any


def async_timed_1(func: Callable) -> Callable:
    @wraps(func)
    async def wrapped(*args, **kwargs) -> Any:
        print(f"starting {func} with args {args} {kwargs}")
        start_time = time.time()
        try:
            return await func(*args, **kwargs)
        finally:
            end_time = time.time()
            latency_ms = (end_time - start_time) * 1000
            print(f"finished {func} in {latency_ms:.2f} milliseconds")

    return wrapped


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"starting {func} with args {args} {kwargs}")
            start_time = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end_time = time.time()
                latency_ms = (end_time - start_time) * 1000
                print(f"finished {func} in {latency_ms:.2f} milliseconds")

        return wrapped

    return wrapper
