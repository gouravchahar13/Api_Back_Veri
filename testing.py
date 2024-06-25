import requests
import json,asyncio

async def get():
    url="http://localhost:8000/"
    response=json.loads(requests.get(url).text)
    response=response[1:-1]
    response=response.replace("\\","")
    print((response))
async def search():
    url="http://localhost:8000/search/000/"
    response=(requests.get(url))
    # response=response[1:-1]
    # response=response.replace("\\","")
    print((response.status_code))

asyncio.run(search())