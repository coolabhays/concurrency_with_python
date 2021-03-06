from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        time.sleep(delay)

        duration = time.perf_counter() - start
        print("%0.4f\t%s%s = %i" % (duration, indents, name, n))
        n -= 1

async def main():
    res_futures = [loop.run_in_executor(
            executor,
            count_down,
            *args
        ) for args in [('A', 1), ('B', 0.8), ('C', 0.5)]]

    await asyncio.gather(*res_futures)

    print('-' * 40)
    print("done")

if __name__ == "__main__":
    start = time.perf_counter()
    executor = ThreadPoolExecutor(max_workers=3)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
