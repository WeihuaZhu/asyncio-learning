import asyncio
from util.async_timer import async_timed_1


@async_timed_1
async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} seconds")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} seconds")
    return delay_seconds


@async_timed_1
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

if __name__ == '__main__':
    asyncio.run(main())
