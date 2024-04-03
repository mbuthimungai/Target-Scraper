import asyncio
from aiohttp import ClientResponseError, ClientConnectionError
import secrets
import random
from requests_html import AsyncHTMLSession


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
        
    
            
    async def content(self, params=None, max_retries: int = 3) -> str:
        """
        Fetch content from a URL with retries using AsyncHTMLSession from requests-html.
        After encountering specific errors, pause for a long duration before retrying.
        
        :param base_url: The base URL to fetch content from.
        :param headers: Headers to include in the request.
        :param params: Parameters to include in the request.
        :param max_retries: Maximum number of retries for the request.
        :return: The content of the response, if successful. None otherwise.
        """
        session = AsyncHTMLSession()

        user_agent = user_agents()
        headers["User-Agent"] = user_agent
        if params:
            params["useragent"] = user_agent
        
        
        for attempt in range(1, max_retries + 1):            
            await asyncio.sleep(30)            
            try:
                
                # Perform the GET request
                response = await session.get(self.base_url, headers=headers,
                                             params=params,
                                             proxies={
                                                "http": rotate_proxies(),
                                                "https": rotate_proxies()
                                             })
                
                # Check for HTTP errors
                response.raise_for_status()
                
                # Return the HTML content of the page
                return response
            except Exception as e:  # Catching a broad exception for simplicity, refine as needed
                print(f"Attempt {attempt} failed: {e}")
                if attempt < max_retries:
                    sleep_time = random.randint(600, 900)  # 10 to 15 minutes
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
    
def rotate_proxies():
    proxies = []
    with open("./proxies.txt", "r") as file:
        proxies = file.readlines()
        
    random_proxy = random_values(proxies)
    return f"http://{random_proxy}"
    