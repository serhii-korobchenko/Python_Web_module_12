import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org', ssl=False) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    '''For Windows environment uncomment next row'''
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())