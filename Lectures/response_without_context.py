import aiohttp
import asyncio


async def main():

    session = aiohttp.ClientSession()
    response = await session.get('http://python.org', ssl=False)

    print("Status:", response.status)
    print("Content-type:", response.headers['content-type'])

    html = await response.text()
    response.close()
    print("Body:", html[:15], "...")
    await session.close()


if __name__ == "__main__":
    '''For Windows environment uncomment next row'''
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())