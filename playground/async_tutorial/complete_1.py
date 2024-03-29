import asyncio


async def count():
    print("1")
    await asyncio.sleep(1)
    print("2")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s

    print(f"{__file__} executed in {elapsed:.2f} seconds")
