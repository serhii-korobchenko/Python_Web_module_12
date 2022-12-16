import aiohttp
import asyncio
from uuid import uuid4


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(
        headers={"Request-Id": str(uuid4())},
        timeout=timeout,
    ) as session:
        async with session.get('http://python.org', ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    '''For Windows environment uncomment next row'''
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())