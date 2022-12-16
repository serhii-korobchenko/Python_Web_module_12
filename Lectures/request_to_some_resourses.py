import aiohttp
import asyncio


async def index(session):
    url = 'http://python.org'
    async with session.get(url, ssl=False) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        print("Body:", html[:15], "...")


async def doc(session):
    url = "https://www.python.org/doc/"
    async with session.get(url, ssl=False) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        print("Body:", html[:15], "...")


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(index(session), doc(session))


if __name__ == "__main__":
    '''For Windows environment uncomment next row'''
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())