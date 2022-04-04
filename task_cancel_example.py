import asyncio
from asyncio import CancelledError
from util import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0
    while not long_task.done():
        print("Task not finished yet, checking again in 1 second")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print("Task is cancelled")


if __name__ == '__main__':
    asyncio.run(main())