import asyncio

async def verse(song):
    print(song)
    await asyncio.sleep(5.45) # I wonder if 5.45sec per verse is enough

async def bottles_of_beer():
    for number_of_bottles in range(99, 0, -1):

        if number_of_bottles > 1: # 99 bottles to 2 bootle
            await verse(
            f"{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer.\n"
            "Take one down, pass it around, " + f"{number_of_bottles  - 1} bottles of beer on the wall.\n"
            )

        else: # 1 bottle
            await verse(
            f"{number_of_bottles} bottle of beer on the wall, {number_of_Bottles} bottle of beer.\n"
            "Take one down, pass it around, no more bottles of beer on the wall.\n"
            )

    await verse(
    "No more bottles of beer on the wall, no more bottles of beer.\n"
    "Go to the store and buy some more, 99 bottles of beer on the wall."
    ) # Time for an AA meeting

asyncio.run(bottles_of_beer())
