# import requests

# headers = {
#     "accept": "application/json",
#     "accept-language": "en-US,en;q=0.9",
#     "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
# }
# res = requests.get("https://www.targetoptical.com/to-us/eyeglasses/womens?cid=EP-RET_191219-Target_TOpage_CategoryWomensEye",
#                    headers=headers)


# with open("file.txt", "w", encoding="utf-8") as file:
#     file.write(str(res.text))
# # print(res.text)

from pymongo import MongoClient
import os
# Connect to MongoDB
# Replace 'mongodb_uri' with your MongoDB URI, e.g., "mongodb://localhost:27017/"
client = MongoClient(os.getenv("MONGODB_URL_REMOTE"))

# Select your database
db = client['targetDB']

# Select your collection
collection = db['products']

# Count documents in the collection
document_count = collection.count_documents({})
print(f"Number of documents in the collection before dropping: {document_count}")

# Drop the collection
# collection.drop()

print(f"The collection '{collection.name}' has been dropped.")
