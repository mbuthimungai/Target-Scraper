import aiohttp
import asyncio
import async_timeout
from aiohttp import ClientResponseError, ClientConnectionError
import secrets
import random

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


class Response:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        
    
            
    async def content(self, isUserAgent=False, max_retries: int = 3, ) -> str:
        """
        Fetch content from a URL with retries. After encountering specific errors,
        pause for a long duration before retrying.
        
        :param max_retries: Maximum number of retries for the request.
        :return: The content of the response, if successful. None otherwise.
        """
                
        user_agent = user_agents()
        headers["User-Agent"] = user_agent
        params["useragent"] = user_agent
        
        async with aiohttp.ClientSession() as session:
            for attempt in range(1, max_retries + 1):
                try:
                    async with async_timeout.timeout(10):  # Timeout for each request
                        async with session.get(self.base_url,
                                               headers=headers, 
                                               params=params) as response:
                            response.raise_for_status()  # Raises error for 4xx/5xx responses
                            return await response.text()  # Correctly await the text of the response
                except (ClientConnectionError, ClientResponseError) as e:
                    print(f"Attempt {attempt} failed due to connection issue: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")

                if attempt < max_retries:
                    sleep_time = random.randint(600, 900)  # Between 10 to 15 minutes
                    print(f"Pausing for {sleep_time / 60} minutes before next attempt.")
                    await asyncio.sleep(sleep_time)
                else:
                    print("Max retries reached. Giving up.")
                    return None
                        
def random_values(d_lists):
    """
    Returns a random value from a list.

    Args
    """
    idx = secrets.randbelow(len(d_lists))
    return d_lists[idx]

def user_agents():
    """
    Returns a random user agent string from a file containing a list of user agents.

    Args:
        -None

    Returns:
        -A string representing a ranom user agent.
    """
    with open('tools//user-agents.txt') as f:
        agents = f.read().split("\n")
        return random_values(agents)
    