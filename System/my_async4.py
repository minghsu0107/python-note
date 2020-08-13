import asyncio
import json
import aiohttp
import requests
import logging
import os
from dotenv import load_dotenv
load_dotenv()


API_ENTPOINT = os.getenv('API_ENTPOINT')


def blockingRequest():
    payload = {}
    mylist = ['hello', 'world']
    mydict = {'hello': 'world', 'world': 'hello'}
    payload['data'] = mylist
    payload['other'] = mydict
    headers = {'Content-Type': 'application/json'}

    try:
        resp = requests.post(API_ENTPOINT, json=payload, headers=headers)
        resp.raise_for_status()
        return resp.json()['predictions']
    except requests.HTTPError as errh:
        print("An Http Error occurred:" + repr(errh))
        raise
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:" + repr(errc))
        raise
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred:" + repr(errt))
        raise
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred" + repr(err))
        raise


async def main():
    payload = {}
    mylist = ['hello', 'world']
    mydict = {'hello': 'world', 'world': 'hello'}
    payload['data'] = mylist
    payload['other'] = mydict
    headers = {'Content-Type': 'application/json'}

    cookies = {'cookies_are': 'working'}
    try:
        async with aiohttp.ClientSession(cookies=cookies) as session:
            async with session.post(API_ENTPOINT, json=payload, headers=headers) as resp:
                if resp.status == 200:
                    data = await resp.read()
                    return json.loads(data)['predictions']
                else:
                    raise Exception(f'response code: {resp.status}')
    except Exception as e:
        logging.error(e)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
