import asyncio
import pandas as pd
import json
import math
import logging
import random

from scrapers.scrapers import Target
from database.database import insert_product_ids, upsert_product

# Configure logging
logging.basicConfig(filename='scraping_log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

stores_df = pd.read_csv("./data/stores.csv")


async def send_to_db(products_data: list, store_id):
    for product_data in products_data:
        try:
            product_id = product_data.get("tcin", "")
            item_data = product_data.get("item", {})
            price_data = product_data.get("price", {})
            promotions = product_data.get("promotions", [{}])

            # Use the last promotion if available, otherwise use an empty dict
            promotion = promotions[-1] if promotions else {}

            product = {
                "item_Id": product_id,
                "title": item_data.get("product_description", {}).get("title", ""),
                "image_url": item_data.get("enrichment", {}).get("images", {}).get("primary_image_url", ""),
                "current_price": price_data.get("current_retail", 0),
                "retail_price": price_data.get("reg_retail", 0),
                "product_url": item_data.get("enrichment", {}).get("buy_url", ""),
                "percent_off": promotion.get("reward_value", 0),
                "plp_message": promotion.get("plp_message", ""),
                "promotion_class": promotion.get("promotion_class", ""),
                "circle_offer": promotion.get("circle_offer", False),
                "store_id": store_id,
                "reviews_count": product_data.get("ratings_and_reviews", {}).get("statistics", {}).get("rating", {}).get("count", 0),
                "reviews_average": product_data.get("ratings_and_reviews", {}).get("statistics", {}).get("rating", {}).get("average", 0.0),
            }
            await upsert_product(product_data=product)
            await insert_product_ids(item_id={"_id": product_id})
        except Exception as e:
            print(f"Error inserting product {product_id}: {e}")
            

async def get_products(url: str, category_code: str):
    target = Target("https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2")
    products_per_page = 24
    
    
    for index, row in stores_df.iterrows():
        
        offset = 0
        store_id = row["store_id"]    
        store_name = row["store_name"]
        products_data = await target.extract_products(
            category_code=category_code, store_id=store_id,
            offset=offset
        )
        
                
        num_products = products_data.get("data", {}).get("search", {}).get("search_response", {}).get("metadata", {}).get("total_results", 0)        
        
        pages = math.ceil(num_products / products_per_page)
        print(f"{store_name} {num_products} {category_code}")
        for i in range(0, pages):
            if offset <= 1176:                
                products_data = await target.extract_products(
                category_code=category_code, store_id=store_id, offset=offset
            )
                products_data_json = products_data.get("data", {}).get("search", {}).get("products", [])            
                await send_to_db(products_data_json, store_id)
                offset += 24
        # Log the completion of scraping for a store
        logging.info(f"Store scraped: {store_name} (ID: {store_id}), Category Code: {category_code}")
                

    

async def read_categories_links():
    while True:  # Infinite loop to continuously monitor and scrape
        categories_links = []
        tasks = []
        
        with open("./data/categories-links.json", "r") as file:
            categories_links = json.load(file)
        
        for category_link in categories_links:        
            category_code = category_link.split("/")[-1].split("-")[-1]
            task = asyncio.create_task(
                get_products(url=category_link, category_code=category_code)
            )
            tasks.append(task)
            # await get_products(url=category_link, category_code=category_code)
        
        await asyncio.gather(*tasks)
        
        wait_for_next_scrape = random.randint(3600, 4200)
        # Wait for a specified delay before re-scraping
        print("Completed all categories. Waiting before rescraping...")
        with open("./Completed.txt", "w") as file:
            file.write("Completed all categories. Waiting before rescraping...")
            
        await asyncio.sleep(wait_for_next_scrape)  # Delay for 1 hour (3600 seconds). Adjust as necessary.    

async def user_agents_get():
    target = Target(user_input="https://www.useragents.me/")
    await target.extract_user_agents()
        
    