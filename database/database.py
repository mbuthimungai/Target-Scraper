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

async def upsert_product(product_data: dict):
    try:
        # Create a filter that matches documents based on both item_Id and store_id
        filter_condition = {
            'item_Id': product_data['item_Id'],
            'store_id': product_data['store_id']
        }

        # Perform an upsert operation: update the document if it exists, insert it if it doesn't
        result = await products.update_one(
            filter_condition,
            {'$set': product_data},
            upsert=True
        )
        
        # Check the result to determine if the operation inserted or updated a document
        if result.upserted_id:
            print(f"Product inserted with id: {result.upserted_id}")
        else:
            if result.matched_count > 0:
                print(f"Product with item_Id: {product_data['item_Id']} and store_id: {product_data['store_id']} description: {product_data['title']} was updated.")
            else:
                print("No matching document found, but an unexpected issue prevented insertion.")

    except Exception as e:
        print(f"An error occurred: {e}")