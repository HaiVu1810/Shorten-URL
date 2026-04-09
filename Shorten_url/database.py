from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import os
uri=os.getenv("MONGODB_URI")
client = MongoClient(uri)
db=client.get_database("Url0")
Url_collection=db.get_collection("Url_list")

def Url_helper(url) -> dict:
    return {
        "id": str(url["_id"]),
        "URL_ori": url["URL_ori"],
        "Short_code": url["Short_code"],
        "Created_at": url["Created_at"],
        "Update_at": url["Update_at"],
        "Access_count": url["Access_count"],
    }

async def retrieve_urls():
    urls = []
    for url in Url_collection.find():
        urls.append(Url_helper(url))
    return urls


# Add a new url into to the database
async def add_url(url_data: dict) -> dict:
    url =  Url_collection.insert_one(url_data)
    new_url = Url_collection.find_one({"_id": url.inserted_id})
    return Url_helper(new_url)

async def check_url(URL_ori: str) -> dict:
    url =  Url_collection.find_one({"URL_ori": URL_ori})
    if url:
        return Url_helper(url)

# Retrieve a url with a matching ID
async def retrieve_url(short_code: str) -> dict:
    url = Url_collection.find_one({"Short_code": str(short_code)})
    if url:
        return Url_helper(url)


# Update a url with a matching ID
async def update_url(Short_code: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    data.pop("id", None) 
    data.pop("_id", None)
    url = Url_collection.find_one({"Short_code": Short_code})
    if url:
        updated_url = Url_collection.update_one(
            {"Short_code": Short_code}, {"$set": data}
        )
        if updated_url:
            return True
        return False


# Delete a url from the database
async def delete_url(shorten_code: str):
    url = Url_collection.find_one({"Short_code": shorten_code})
    if url:
        Url_collection.delete_one({"Short_code": shorten_code})
        return True
