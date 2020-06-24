import reqcache
import aiohttp
import asyncio
import time
async def main():
    sess = aiohttp.ClientSession()
    a = await reqcache.aget_json("", sess)
    print(a)
    a = await reqcache.aget("", sess)
    print(a)
    await sess.close()
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())
loop.run_until_complete(future)