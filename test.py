import requests
import json, random

import hashlib
import time
import os

def generate_hashed_visitor_id():
    random_data = os.urandom(16)  # Generates a random byte string
    timestamp = str(time.time()).encode('utf-8')
    base_string = random_data + timestamp
    hashed_id = hashlib.sha256(base_string).hexdigest()  # Creates a SHA-256 hash
    return hashed_id

visitor_id = generate_hashed_visitor_id()


url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2"
params = {
    "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
    "category": "q8v16",
    "channel": "WEB",
    "count": 24,
    "default_purchasability_filter": True,
    "include_dmc_dmr": True,
    "include_sponsored": True,
    "new_search": False,
    "offset": 0,
    "page": "/c/q8v16",
    "platform": "desktop",
    "pricing_store_id": 1771,
    "store_ids": "1771,1768,1113,3374,1792",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "visitor_id": f"018EA380AB5E{random.randint(1000, 2000)}AD36B22C54BC2BBE",
    "zip": "52404"
}

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
# 89490549
response = requests.get(url, headers=headers, params=params)

products_data = response.json()
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
