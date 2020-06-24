import requests
import time
from . import reqmap, CLEAR_TIME
def get(url: str) -> requests.Response:
    cached_req = reqmap.get(url, 0)
    if not cached_req or time.time() - cached_req[1]> CLEAR_TIME:
        r = requests.get(url)
        reqmap.update({url: (r, time.time())})
        return r
    return cached_req[0]
