import time
import asyncio as aio
import aiohttp
import json

from settings import settings


# async def get_completion(url:str, session: aiohttp.ClientSession, content:str = "hello"):
#     data = {
#         "model": settings.model,
#         "messages": [{"role": 'user', "content": content }],
#         "temperature" : 0.7,
#     }
#     headers = {
#         "Content-type": "application/json",
#         "Authorization": f"Bearer {settings.api_key}"
#     }
#     response = await session.post(
#         url=url, headers=headers, data=json.dumps(data)
#     )
#     response_data = await response.json()
#     print(response_data)

# async def main():
#     url = settings.url
#     async with aiohttp.ClientSession() as session:
#         await get_completion(url=url, session=session)
    
if __name__ == '__main__':
    t0 = time.time()
    print(settings.user)
    # aio.run(main())
    t1 = round(time.time() - t0, 1)
    print(f"it took {t1} secs")
