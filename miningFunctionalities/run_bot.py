from miningFunctionalities.send_message import read_categories_links, user_agents_get


async def main():
    await user_agents_get()
    await read_categories_links()