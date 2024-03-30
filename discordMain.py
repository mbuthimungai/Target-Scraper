import asyncio
from scrapers.scrapers import Target


target = Target(user_input="https://www.useragents.me/")

async def main():
    await target.extract_user_agents()
    
    
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())