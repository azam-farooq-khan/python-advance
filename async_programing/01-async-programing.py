import asyncio
async def brew (Tea):
    print(f"Brewing {Tea}")
    await asyncio.sleep(2)
    print(f"{Tea} is ready!")

async def main ():
    await asyncio.gather(
    brew ("Masala chai"),
    brew("green tea"))

asyncio.run(main())