import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3"
}
res = requests.get("https://www.target.com/store-locator/find-stores",
                   headers=headers)



with open("store.txt", "w", encoding="utf-8") as file:
    
    file.write(str(res.text))