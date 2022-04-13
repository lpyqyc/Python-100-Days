import asyncio
import threading


async def hello(tx):
    print(f"Hello world!{tx}")
    r = await asyncio.sleep(1)
    print(f"Hello again!{r}")
    return threading.currentThread().ident


# asyncio.run(hello())
it = hello(43)


# next(it)

async def two():
    # tk = asyncio.create_task(hello())

    try:
        pass
    except Exception as e:
        print(e)
    finally:
        print("ffaa!!")

    tk = asyncio.create_task(hello(56))
    tk.add_done_callback(b)
    # tk.cancel("一个取消消息")
    await tk
    # print(tk)
    df = await asyncio.gather(hello(12), hello(34))
    # df.cancel()
    # await df
    print(df)
    print(threading.currentThread().ident)


def b(c):
    print(f'AAA:{c}')


asyncio.run(two())
# asyncio.run(asyncio.gather(hello(12), hello(34)))
# send(it)
# await hello()
