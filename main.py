import asyncio
import scrapper


async def scrappin():
    while True:
        a, b = scrapper.scrap()
        print(a)
        print(b)
        await asyncio.sleep(1)


asyncio.run(scrappin())




