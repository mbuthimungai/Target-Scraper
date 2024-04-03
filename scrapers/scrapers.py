from bs4 import BeautifulSoup
import json
import random

from tools.tools import Response

params = {
    "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
    "category": "k4uyq",
    "channel": "WEB",
    "count": 24,
    "default_purchasability_filter": "true",
    "include_dmc_dmr": "true",
    "include_sponsored": "true",
    "new_search": "false",
    "offset": 0,
    "page": "/c/k4uyq",
    "platform": "desktop",
    "pricing_store_id": 1771,
    "store_ids": "1771,1768,1113,3374,1792",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "visitor_id": f"018EA380AB5E{random.randint(1000, 2000)}AD36B22C54BC2BBE",
    "zip": "52404"
}


class Target:
    def __init__(self, user_input) -> None:
        self.user_input = user_input
    
    async def extract_products(self,
                               category_code: str,
                               store_id: str,
                               offset: int) -> dict: 
        params["offset"] = offset
        params["category"] = category_code
        params["store_ids"] = store_id
        params["pricing_store_id"] = store_id
        params["page"] = f"/c/{category_code}"        
        
        content = await Response(self.user_input).content(params=params)
        
        products_data = content.json()
        return products_data
        
    async def extract_user_agents(self) -> None:
        content = await Response(self.user_input).content()
        
        soup = BeautifulSoup(content.text, "html.parser")        
        
        # find div with user agents
        div_with_json_ua = soup.find('div', id='most-common-desktop-useragents-json-csv')
        
        # find the text area
        
        textarea = div_with_json_ua.find('textarea', {'class': 'form-control'})
        
        if textarea:
            user_agents = json.loads(textarea.text)
            
            # This deletes content from the user agent.txt file
            with open("./tools/user-agents.txt", "w") as file:
                pass
            with open("./tools/user-agents.txt", "a") as file:
                for user_agent in user_agents:
                    file.write(f'{user_agent.get("ua")}\n')

    async def update_url(self, url):
        self.user_input = url        
