import asyncio
from util import delay


async def main_timeout() -> None:
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Got a timeout")
        print(f"Was the task cancelled? {delay_task.cancelled()}")


async def main_shield() -> None:
    delay_task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(delay_task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Task took longer than 5 seconds, it will finish soon")
        result = await delay_task
        print(result)


if __name__ == '__main__':
    print("========== timeout example ==========")
    asyncio.run(main_timeout())
    print("========== shield example ==========")
    asyncio.run(main_shield())