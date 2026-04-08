from typing import Optional
from pydantic import BaseModel,EmailStr,Field
from datetime import datetime

class url_schema(BaseModel):
    URL_ori: str = Field(...) 
    Short_code: str=Field(...)
    Created_at: datetime = Field(...)
    Update_at: datetime = Field(...)
    Access_count: int = Field(...)
    class Config:
        json_schema_extra={
            "example":{
            "URL_ori": "https://www.google.com/search?q=gemini+ai+is+awesome",
            "Short_code": "gem123",
            "Created_at": {
                "$date": "2026-04-06T10:24:30.000Z"
            },
            "Update_at": {
                "$date": "2026-04-06T10:24:30.000Z"
            },
            "Access_count": 0
        }
    }

class UpdateUrlModel(BaseModel):
    URL_ori: Optional[str]  
    Short_code: Optional[str]
    Created_at: Optional[datetime] 
    Update_at: Optional[datetime] 
    Access_count: Optional[int] 
    class Config:
        json_schema_extra={
            "example":{
            "URL_ori": "https://www.google.com/search?q=gemini+ai+is+awesome",
            "Short_code": "gem123214",
            "Created_at": {
                "$date": "2026-06-06T10:24:30.000Z"
            },
            "Update_at": {
                "$date": "2026-06-06T10:24:30.000Z"
            },
            "Access_count": 2
        }
    }
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
