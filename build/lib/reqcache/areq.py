import aiohttp
import time
from . import reqmap, CLEAR_TIME

async def aget(url: str, ses: aiohttp.ClientSession) -> aiohttp.ClientResponse:
    cached = reqmap.get(url, 0)
    if not cached or time.time() - cached[1] > CLEAR_TIME:
        async with ses.get(url) as res:
            t = await res.text()
            reqmap.update({url: (t, time.time())})
            return t
    return cached[0]

async def aget_json(url: str, ses: aiohttp.ClientSession) -> aiohttp.ClientResponse:
    cached = reqmap.get(url, 0)
    if not cached or time.time() - cached[1] > CLEAR_TIME:
        async with ses.get(url) as res:
            reqmap.update({url: (res, time.time())})
            return await res.json()
    return cached[0]
