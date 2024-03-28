import aiohttp
import asyncio
import async_timeout
from aiohttp import ClientResponseError, ClientConnectionError
import secrets
import random




class Response:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
            
    async def content(self, max_retries: int = 3) -> str:
        """
        Fetch content from a URL with retries. After encountering specific errors,
        pause for a long duration before retrying.
        
        :param max_retries: Maximum number of retries for the request.
        :return: The content of the response, if successful. None otherwise.
        """
        headers = {'User-Agent': 'Your User Agent Here'}
        async with aiohttp.ClientSession() as session:
            for attempt in range(1, max_retries + 1):
                try:
                    async with async_timeout.timeout(10):  # Timeout for each request
                        async with session.get(self.base_url, headers=headers) as response:
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
    with open('tool//user-agents.txt') as f:
        agents = f.read().split("\n")
        return random_values(agents)
    