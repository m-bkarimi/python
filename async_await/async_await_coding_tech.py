import asyncio
import time
counter =  0 
async def func1():
    global counter 
    while True:

        print(counter,'def1')
        counter+=1
        counter-=1
        await asyncio.sleep(50) # switch between function
        print('def1')



async def func2():
    global counter
    while True:
        print(counter,'def2')
        counter+=1
        counter-=1
        await asyncio.sleep(15) # switch between function
        print('def2')
        
asyncio.gather(func1(),func2())
asyncio.get_event_loop().run_forever()
