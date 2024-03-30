import requests
import json

url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2"
params = {
    "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
    "category": "4xq89",
    "channel": "WEB",
    "count": "24",
    "default_purchasability_filter": "true",
    "include_dmc_dmr": "true",
    "include_sponsored": "true",
    "new_search": "false",
    "offset": "24",
    "page": "/c/4xq89",
    "platform": "desktop",
    "pricing_store_id": "1777",
    "store_ids": "1777",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "visitor_id": "018E80561A130201ABA6237C959E4080",
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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, params=params)

products_data = response.json()

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
    json.dump(products_data["data"]["search"]["products"][0], file, indent=4)
