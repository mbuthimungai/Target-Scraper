import requests, secrets
import json, random

import hashlib
import time
import os, asyncio
from requests_html import AsyncHTMLSession

def generate_hashed_visitor_id():
    random_data = os.urandom(16)  # Generates a random byte string
    timestamp = str(time.time()).encode('utf-8')
    base_string = random_data + timestamp
    hashed_id = hashlib.sha256(base_string).hexdigest()  # Creates a SHA-256 hash
    return hashed_id

visitor_id = generate_hashed_visitor_id()


def random_values(d_lists):
    """
    Returns a random value from a list.

    Args
    """
    idx = secrets.randbelow(len(d_lists))
    return d_lists[idx]

def rotate_proxies():
    """
    Selects a random proxy from a list of proxies stored in a file, adjusts the format to 
    remove extra semicolons, and returns it with the HTTP scheme prefixed.
    """
    with open("./proxies.txt", "r") as file:
        proxies = file.readlines()

    # Select a random proxy and strip newline characters
    random_proxy = random_values(proxies).strip()

    # Remove the extra semicolon from the proxy string
    formatted_proxy = random_proxy.replace(";;", ";")

    # Return the formatted proxy with 'http://' prefixed
    return f"http://{formatted_proxy}"



url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2"
s = requests.session()
s.get('https://www.target.com');
key = s.cookies['visitorId']

params = {
    "key": f"{generate_hashed_visitor_id()}",
    "category": "4slzs",
    "channel": "WEB",
    "count": 24,
    "default_purchasability_filter": True,
    "include_dmc_dmr": True,
    "include_sponsored": True,
    "new_search": False,
    "offset": 0,
    "page": "/c/4slzs",
    "platform": "desktop",
    "sort_by": "newest",
    "pricing_store_id": 1771,
    "store_ids": "1771,1768,1113,3374,1792",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "visitor_id": f"{key}",
    "zip": "52404"
}


headers = {
    'authority': 'redsky.target.com',
 'method': 'GET',
 'path': '/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&category=k4uyq&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&new_search=false&offset=1176&page=%2Fc%2Fk4uyq&platform=desktop&pricing_store_id=2069&store_ids=2069%2C2784%2C1872%2C3241%2C1794&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F120.0.0.0+Safari%2F537.36&visitor_id=018EA5ADA06C0201977511924105B48E&zip=40000',
 'scheme': 'https',
 'Accept': 'application/json',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
 'Cookie': 'TealeafAkaSid=vf8zcL4xLeF3i96wNUqH4LFYZx_5cduP; visitorId=018EA5ADA06C0201977511924105B48E; sapphire=1; UserLocation=40000|18.940|72.840|MH|IN; ffsession={"sessionHash":"1e2a71650a737f1712176617394"}; fiatsCookie=DSI_2069|DSN_Durham Renaissance Pkwy|DSZ_27713; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIzZDhlYTA1ZS01YjQxLTRhNWYtYmNiZS0zNDg4NDEyNzU3N2MiLCJpc3MiOiJNSTYiLCJleHAiOjE3MTI2MDgwMTcsImlhdCI6MTcxMjUyMTYxNywianRpIjoiVG...',
 'Origin': 'https://www.target.com',
 'Referer': 'https://www.target.com/c/facial-tissue-household-essentials/all-deals/-/N-tv7qhZakkos',
 'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
 'Sec-Ch-Ua-Mobile': '?0',
 'Sec-Ch-Ua-Platform': '"Windows"',
 'Sec-Fetch-Dest': 'empty',
 'Sec-Fetch-Mode': 'cors',
 'Sec-Fetch-Site': 'same-site',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Geck"
}

session = AsyncHTMLSession()
# 89490549
response = requests.get("https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&category=tp9m7Z5y6q6Z5y761Z5y746&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&new_search=false&offset=0&page=%2Fc%2Ftp9m7Z5y6q6Z5y761Z5y746&platform=desktop&sort_by=newest&pricing_store_id=1771&store_ids=1771&useragent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F122.0.0.0+Safari%2F537.36+OPR%2F108.0.0.&visitor_id=78492aca48953485cb18815340d299b3c790ef384a7ffbff5e60906be833fe69&zip=52404", headers=headers)
# print(response)
res = ""
async def get_pd():
    global res
    print(rotate_proxies())
    res = await session.get(f"https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&category=5xtu8Zakkos&channel=WEB&count=24&default_purchasability_filter=true&include_dmc_dmr=true&include_sponsored=true&new_search=false&offset=480&page=%2Fc%2F5xtu8Zakkos&platform=desktop&sort_by=newest&pricing_store_id=1768&store_ids=1768&useragent=Mozilla%2F5.0+%28Windows+NT+6.1%3B+Win64%3B+x64%3B+rv%3A109.0%29+Gecko%2F20100101+Firefox%2F115.&zip=52404&visitor_id=33c4ab3114d872225f6fe506dff210659a3a5b69fd85e86d90e74dfdb447aabf",
                    headers=headers,
                    proxies = {
                        'http': rotate_proxies(),
                        'https': rotate_proxies(),
                    }
    )
    print("This is the res")
    print(res)
    # res.raise_for_status()
    print(res.text)

s = requests.session()
s.get('https://www.target.com');
key = s.cookies['visitorId']
print(key)    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_pd())
    
products_data = res.json()
print(products_data)
num_prods = products_data["data"]["search"]["search_response"]["metadata"]["total_results"]

product = products_data["data"]["search"]["products"][0]
product_title = product["item"]["product_description"]["title"]
product_image = product["item"]["enrichment"]["images"]["primary_image_url"]
product_id = product["tcin"]
curr_price = product["price"]["current_retail"]
retail_price = product["price"]["reg_retail"]
product_url = product["item"]["enrichment"]["buy_url"]

print(f"Number of products: {num_prods}\n")
print(f"Product Title: {product_title}\n"
      f"Product Image URL: {product_image}\n"
      f"Product ID: {product_id}\n"
      f"Current Price: {curr_price}\n"
      f"Retail Price: {retail_price}\n"
      f"Product Url: {product_url}")


with open("file.json", "w") as file:
    json.dump(products_data["data"]["search"]["products"], file, indent=4)
