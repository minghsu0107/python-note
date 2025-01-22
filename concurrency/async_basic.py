import asyncio
import time

async def coroutine1():
    print('coroutine1 start')
    time.sleep(2)
    print('coroutine1 end')
    return 'coro1 result'

async def coroutine2():
    print('coroutine2 start')
    time.sleep(3)
    print('coroutine2 end')
    return 'coro2 result'

async def main():

    tasks = []
    tasks.append(asyncio.create_task(coroutine1()))
    tasks.append(asyncio.create_task(coroutine2()))

    # the order of result values is preserved
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f'results: {results}')

if __name__ == '__main__':
    asyncio.run(main())
