from fastapi import APIRouter, Body , HTTPException
from fastapi.encoders import jsonable_encoder
from datetime import datetime

import random
import string

from server.database import (
    retrieve_urls,
    add_url,
    retrieve_url,
    check_url,
    update_url,
    delete_url,
)
from server.models.url_schem import(
    ErrorResponseModel,
    ResponseModel,
    UpdateUrlModel,
    url_schema,
)
router = APIRouter()
def generate_short_code(length=6):
    # Combines letters and numbers for the code
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


@router.post("/shorten",response_description="Add Url to make Shorten")
async def Add_and_shorten_url(url: str):
    new_data = {
            "URL_ori": url,
            "Short_code": generate_short_code(6),
            "Created_at": datetime.now(),
            "Update_at": datetime.now(),
            "Access_count": 0,
        }
    new_data=jsonable_encoder(new_data)
    url_exist=await check_url(url)
    if (url_exist):
        return ResponseModel(url_exist,"Already Have")
    res= await add_url(new_data)    
    return ResponseModel(res, "Student added successfully.")

@router.get("/shorten/")
async def Get_URL_from_shortcode():
    get_url= await retrieve_urls()
    if(get_url):
        return ResponseModel(get_url,"Url Retrived")
    raise ErrorResponseModel("Could not retrive any URL",404,"URL not exist")

@router.get("/shorten/{short_code}")
async def Get_URL_from_shortcode(short_code: str):
    get_url=await retrieve_url(short_code)
    if (get_url):
        return ResponseModel(get_url, "data retrieved successfully")
    raise ErrorResponseModel("Could not retrive any URL",404,"URL not exist")

    
@router.put("/shorten/{Short_code}")
async def Update_Shorten_code(Short_code: str , New_URL_to_update: str):
    get_url=await retrieve_url(Short_code)
    if (get_url):
        get_url["URL_ori"] = New_URL_to_update
        res = await update_url(Short_code,get_url)
        if(res):
            return ResponseModel(
            res,
            "Short Code  update is successful",
            )
        return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the  data.",
    )
    raise ErrorResponseModel("Could not retrive any URL",404,"URL not exist")

@router.delete("/shorten/{shorten_code}")
async def Delete_url(Short_code:str):
    get_url = await retrieve_url(Short_code)
    if (get_url):
        Delete_url=await delete_url(Short_code)
        if Delete_url:
            return "204 No Content"
    raise ErrorResponseModel("Status Code:",404,"URL not found")

@router.get("/shorten/{Short_code}/stats")
async def Update_Shorten_code(Short_code: str):
    get_url=await retrieve_url(Short_code)
    if (get_url):
        get_url["Access_count"] += 1
        res = await update_url(Short_code,get_url)
        if(res):
            return ResponseModel(
            get_url,"200 ok")
    raise ErrorResponseModel("Could not retrive any URL",404,"URL not exist")

