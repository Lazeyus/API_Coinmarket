import asyncio
import my_test
import time
import pytest


@pytest.mark.asyncio
async def test_my_coro():
    timers = []
    time_before_response = time.time()

    for i in range(8):
        start_time = time.time()
        my_test.test_access_to_10_tickers_sorted_by_volume()
        end_time = time.time()
        timers.append(end_time - start_time)

    time_after_response = time.time()
    timers = sorted([i for i in timers])
    percentile = timers[round(len(timers) * 0.8) - 1]

    assert percentile < 0.450, "80-Percentile more than 450 ms"
    assert round(len(timers) / (time_after_response - time_before_response)) >= 5, "rps less than 5"


async def main():
    await test_my_coro()


asyncio.run(main())
