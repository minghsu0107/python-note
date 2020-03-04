# 協程可以看做是"能在中途中斷、中途返回值給其他協程、中途恢復、中途傳入參數的函數"

# loop.run_forever()
# 這個函數一執行，Event Loop就會永遠執行不會被關閉，除非在程式中出現loop.stop()就停止
def test():
	import asyncio
	loop = asyncio.get_event_loop() #建立一個Event Loop

	async def example1(): # 定義一個中間會被中斷的協程
	    print("Start example1 coroutin.")
	    await asyncio.sleep(1) # 中斷協程一秒
	    # 即註冊新的event: sleep() 結束; 對應的callback為執行以下尚未完成的部分
	    print("Finish example1 coroutin.")

	async def example2(): # 定義一個協程
	    print("Start example2 coroutin.")
	    # do some process...
	    print("Finish example2 coroutin.")

	tasks = [ # 建立一個任務列表
	    asyncio.ensure_future(example1()),
	    asyncio.ensure_future(example2()),
	]

	loop.run_until_complete(asyncio.wait(tasks))
	# 把協程封裝成一個task對象，這個對象可以儲存任務執行時的狀態與環境
	# 通常大家會說這對象儲存了任務的"上下文"(context)
	# 最後註冊到事件循環裡
	# loop馬上觸發事件而啟動，先執行example1，中途暫停example1之後切換到example2，最後再切回example1
	# output:
	# Start example1 coroutin.
	# Start example2 coroutin.
	# Finish example2 coroutin.
	# Finish example1 coroutin.

test()