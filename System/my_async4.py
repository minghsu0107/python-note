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
    success = False
    tries = 0
    predictions = []
    while not success:
        tries += 1
        try:
            payload = {}
            mylist = ['hello', 'world']
            mydict = {'hello': 'world', 'world': 'hello'}
            payload['data'] = mylist
            payload['other'] = mydict
            headers = {'Content-Type': 'application/json'}
            resp = requests.post(API_ENTPOINT, json=payload, headers=headers)
            resp.raise_for_status()
            predictions = resp.json()['predictions']
            success = True
        except requests.HTTPError as errh:
            logging.error("An Http Error occurred:" + repr(errh))
        except requests.exceptions.ConnectionError as errc:
            logging.error(
                "An Error Connecting to the API occurred:" + repr(errc))
        except requests.exceptions.Timeout as errt:
            logging.error("A Timeout Error occurred:" + repr(errt))
        except requests.exceptions.RequestException as err:
            logging.error("An Unknown Error occurred" + repr(err))
        finally:
            if tries >= 3:
                logging.error('tries exceeded:%s ', tries)
                return []

    return predictions


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
