import time
import asyncio as aio
import aiohttp
import json

from settings import settings

from insta import login_user, reply 

URL = 'https://api.openai.com/v1/chat/completions'

async def get_completion(url:str, session: aiohttp.ClientSession, content:str = "hello"):
    data = {
        "model": settings.model,
        "messages": [{"role": 'user', "content": content }],
        "temperature" : 0.7,
    }
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {settings.api_key}"
    }
    response = await session.post(
        url=url, headers=headers, data=json.dumps(data)
    )
    response_data = await response.json()
    print(f"content {content}")
    return(response_data['choices'][0]['message']['content'])

async def main():
    url = URL

    cl = login_user()
    
    while True:    
        async with aiohttp.ClientSession() as session:
            all_threads = cl.direct_threads(selected_filter="unread")
            if all_threads:
                for thread in all_threads:
                    content = ""
                    for msg in thread.messages:
                        content= msg.text
                    answer = await get_completion(url=url, session=session, content=content)
                    reply(cl=cl, thread_id=thread.id, answer=answer)
                        
if __name__ == '__main__':
    t0 = time.time()
    print(settings.user)
    aio.run(main())
    t1 = round(time.time() - t0, 1)
    print(f"it took {t1} secs")
