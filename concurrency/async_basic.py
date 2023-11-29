# 協程可以看做是"能在中途中斷、中途返回值給其他協程、中途恢復、中途傳入參數的函數"

# the following uses low-level api
def test():
    import asyncio
    loop = asyncio.get_event_loop()  # 建立一個Event Loop

    async def example1(idx):  # 定義一個中間會被中斷的協程
        print(f"Start example1 coroutine (idx: {idx})")
        await asyncio.sleep(1)  # 中斷協程一秒
        # 即註冊新的event: sleep() 結束; 對應的callback為執行以下尚未完成的部分
        print(f"finish example1 coroutine (idx: {idx})")

    async def example2(idx):  # 定義一個協程
        print(f"Start example2 coroutine (idx: {idx})")
        # do some process...
        print(f"finish example2 coroutine (idx: {idx})")

    tasks = [  # 建立一個任務列表
        asyncio.ensure_future(example1(1)),
        asyncio.ensure_future(example1(2)),
        asyncio.ensure_future(example2(1)),
        asyncio.ensure_future(example2(2)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    # 把協程封裝成一個task對象，這個對象可以儲存任務執行時的狀態與環境
    # 通常大家會說這對象儲存了任務的"上下文"(context)
    # 最後註冊到事件循環裡
    # loop馬上觸發事件而啟動，先執行example1，中途暫停example1之後切換到example2，最後再切回example1
    # output:
    # Start example1 coroutine (idx: 1)
    # Start example1 coroutine (idx: 2)
    # Start example2 coroutine (idx: 1)
    # finish example2 coroutine (idx: 1)
    # Start example2 coroutine (idx: 2)
    # finish example2 coroutine (idx: 2)
    # finish example1 coroutine (idx: 1)
    # finish example1 coroutine (idx: 2)

# the following uses high-level api
def test2():
    import asyncio

    async def example1(idx):
        print(f"Start example1 coroutine (idx: {idx})")
        await asyncio.sleep(1)
        print(f"finish example1 coroutine (idx: {idx})")
        return f'example 1, res: {idx}'

    async def example2(idx):
        print(f"Start example2 coroutine (idx: {idx})")
        print(f"finish example2 coroutine (idx: {idx})")
        return f'example 2, res: {idx}'

    tasks = [
        example1(1),
        example1(2),
        example2(1),
        example2(2)
    ]
    # returns a list of results (same order as registered tasks)
    res = asyncio.run(asyncio.gather(*tasks))

    return res


if __name__ == "__main__":
    # test()
    # ['example 1, res: 1', 'example 1, res: 2', 'example 2, res: 1', 'example 2, res: 2']
    print(test2())
