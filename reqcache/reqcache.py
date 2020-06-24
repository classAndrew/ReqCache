import requests
import time
reqmap = {}
def get(url: str) -> requests.Response:
    cached_req = reqmap.get(url, 0)
    if not cached_req:
        r = requests.get(url)
        reqmap.update({url: r})
        return r
    print("Already Sent")
    return cached_req
