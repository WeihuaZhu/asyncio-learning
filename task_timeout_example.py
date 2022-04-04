import asyncio
from util import delay


async def main() -> None:
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Got a timeout")
        print(f"Was the task cancelled? {delay_task.cancelled()}")


if __name__ == '__main__':
    asyncio.run(main())