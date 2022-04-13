import rx
from rx import of, interval, operators
from rx import Observable
import asyncio

ob = of(1, 2, 34, 5, 6, 7, 7)
ob.subscribe(
    on_next=lambda i: print(f'Received: {i}'),
    on_error=lambda e: print(f'Error: {e}'),
    on_completed=lambda: print('Completed')

)


def fc(x) -> int:
    return 5


def printff(x):
    print(fc(x))


def printxxc(xxc):
    print(f'DDD:::{xxc}')


x_xx = False
# ob2 = interval(1).pipe(operators.distinct_until_changed()).subscribe()
# operators.filter(lambda x: x == True),
ob2 = interval(1).pipe(operators.map(lambda x: x_xx),
                       operators.distinct_until_changed())
ob2.subscribe(lambda x: print(x))


# rx.of(ob2).subscribe(lambda x: print(x))

# .subscribe(on_next=lambda x: printxxc(x))
# ob2.subscribe(lambda x: print(x))
# ob2.subscribe(
#     on_next=lambda x: printff(x)
# )

# rx.internal(10)
# Observable
# print(fc())

async def changes():
    global x_xx
    await asyncio.sleep(5)
    x_xx = True
    print('AAAA{}'.format(x_xx))
    await asyncio.sleep(5)
    print('BBBB{}'.format(x_xx))
    x_xx = False


asyncio.run(changes())
