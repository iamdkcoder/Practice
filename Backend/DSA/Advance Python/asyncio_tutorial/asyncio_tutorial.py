import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# main() -> <coroutine object main at 0x7f7f7f7f7f7f7f7f>
asyncio.run(main())