import asyncio
import scrapper
import stateIO



async def scrappin():
    while True:
        a, b = scrapper.scrap()
        print(a)
        print(b)
        if(a == "69"):
            print("Changing Gate")
            stateIO.stateChange("gate")

        if(b == "69"):
            print("Changing Garage")
            stateIO.stateChange("garage")

        
        await asyncio.sleep(1)


asyncio.run(scrappin())




