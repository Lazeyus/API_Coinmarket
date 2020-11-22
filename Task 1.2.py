import asyncio
import my_test
import time

async def my_coro(itr):
    """A coroutine."""
    timers = []
    time_before_response = time.time()
    while itr != 0:
        start_time = time.time()
        my_test.test_access_to_10_tickers_sorted_by_volume()
        end_time = time.time()
        timers.append(end_time - start_time)
        itr -= 1

    time_after_response = time.time()
    timers = sorted([i for i in timers])
    percentile = timers[round(len(timers) * 0.8) -1]

    print(percentile)
    print(round(len(timers) / (time_after_response - time_before_response)))


async def main():
    """The top-level coroutine."""
    await my_coro(8)


asyncio.run(main())
