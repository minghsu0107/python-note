import concurrent.futures
import asyncio
import json
import aiohttp
import requests
import logging
import os
# from dotenv import load_dotenv
# load_dotenv()


API_ENTPOINT = os.getenv('API_ENTPOINT')
API_ENTPOINT = 'http://www.google.com'


def blockingRequest(payload: dict):
    success = False
    tries = 0
    predictions = []
    while not success:
        tries += 1
        try:
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


def run_block():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(10):
            payload = {}
            mylist = ['hello', 'world']
            mydict = {'hello': 'world', 'world': 'hello'}
            payload['data'] = mylist
            payload['other'] = mydict
            futures.append(executor.submit(blockingRequest, payload=payload))
        # output may be ordered differently
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


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

if __name__ == '__main__':
    asyncio.run(main())
