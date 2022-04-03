import asyncio
from util import delay


async def add_one(number: int) -> int:
    result = number + 1
    print(f"result computed: {result}, right before return")
    return result


async def hello_world_message() -> str:
    await delay(1)
    return "Hello World!"


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

if __name__ == '__main__':
    asyncio.run(main())




