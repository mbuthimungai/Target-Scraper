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
    "offset": "0",
    "page": "/c/4xq89",
    "platform": "desktop",
    "pricing_store_id": "1771",
    "store_ids": "1771",
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

with open("file.json", "w") as file:
    json.dump(response.json(), file, indent=4)
