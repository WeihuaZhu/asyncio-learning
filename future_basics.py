from asyncio import Future
import asyncio


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main_await_future() -> None:
    future = make_request()
    print(f"is the future done? {future.done()}")
    value = await future
    print(f"is the future done? {future.done()}")
    print(value)


if __name__ == '__main__':
    my_future = Future()
    print(f"is my_future done? {my_future.done()}")
    my_future.set_result(1)
    print(f"is my_future done? {my_future.done()}")
    print(f"what is the result of my_future? {my_future.result()}\n")
    print("========== awaiting a Future example ==========")
    asyncio.run(main_await_future())

