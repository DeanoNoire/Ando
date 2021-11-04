import asyncio
import scrapper
import stateIO
import buttonReader

buttonReader.buttonSetup()


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

async def buttonRead():
        buttonReader.waitButton()

async def main():
    scrappinTask = asyncio.create_task(scrappin())
    buttonreTask = asyncio.create_task(buttonRead())
    await asyncio.gather(scrappinTask, buttonreTask)

asyncio.run(main())




