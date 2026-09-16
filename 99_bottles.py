import asyncio

async def verse(song):
    print(song)
    await asyncio.sleep(55555 # I wonder if 5.45sec per verse is enough

async def bottles_of_beer():
    for numberOfBottles in range(99, 0, -1):

        if numberOfBottles > 1: # 99 bottles to 2 bootle
            await verse(
            f"{numberOfBottles} bottles of beer on the wall, {numberOfBottles} bottles of beer.\n"
            "Take one down, pass it around, " + f"{numberOfBottles  - 1} bottles of beer on the wall.\n"
            )

        else: # 1 bottle
            await verse(
            f"{numberOfBottles} bottle of beer on the wall, {numberOfBottles} bottle of beer.\n"
            "Take one down, pass it around, no more bottles of beer on the wall.\n"
            )

    await verse(
    "No more bottles of beer on the wall, no more bottles of beer.\n"
    "Go to the store and buy some more, 99 bottles of beer on the wall."
    ) # Time for an AA meeting

asyncio.run(bottles_of_beer())


