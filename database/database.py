from motor.motor_asyncio import AsyncIOMotorClient
import os
from pymongo.errors import DuplicateKeyError

client = AsyncIOMotorClient(os.getenv("MONGODB_URL_REMOTE"))

db = client.targetDB
products = db.products
products_ids = db.productsIDs


async def insert_product_ids(item_id: dict):
    try:
        result = await products_ids.insert_one(item_id)  # Use _id as the unique identifier
        print(f"Product ID inserted with id: {result.inserted_id}")
    except DuplicateKeyError:
        print(f"Duplicate item ID: {item_id}. No new document was inserted.")
    except Exception as e:
        print(f"An error occurred: {e}")


async def insert_product(product_data: dict):
    try:
        result = await products.insert_one(product_data)
        print(f"Product inserted with id: {result.inserted_id}")
    except Exception as e:
        print(f"An error occurred: {e}")

