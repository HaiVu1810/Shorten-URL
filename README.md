# URL Shortener

A simple and efficient URL shortening service built with **FastAPI** and **MongoDB**. This application allows you to convert long URLs into short, memorable codes for easy sharing and tracking.

## Features

- ✨ **URL Shortening**: Convert long URLs to short, random 6-character codes
- 📊 **Access Tracking**: Monitor how many times each shortened URL is accessed
- 🔍 **URL Management**: Create, retrieve, update, and delete shortened URLs
- ⚡ **Fast Performance**: Built on FastAPI for high-speed async operations
- 💾 **MongoDB Integration**: Persistent storage with cloud-based MongoDB
- 🛡️ **Duplicate Detection**: Prevents duplicate entries for the same original URL

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **Server**: [Uvicorn](https://www.uvicorn.org/)
- **Language**: Python 3.x
- **Data Validation**: Pydantic

## Project Structure

```
Shorten_url/
├── main.py                 # Application entry point
├── README.md              # Project documentation
├── __init__.py            # Package initialization
└── server/
    ├── app.py             # FastAPI application setup
    ├── database.py        # MongoDB operations and helpers
    ├── models/
    │   └── url_schem.py   # Pydantic data models
    └── routes/
        └── Url_shorten.py # URL shortening API endpoints
```

## Installation

### Prerequisites

- Python 3.7+
- MongoDB Atlas account (for cloud database)
- pip (Python package installer)

### Setup Steps

1. **Clone the repository**
   ```bash
   cd Shorten_url
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn pymongo
   ```

3. **Configure MongoDB Connection**
   - Update the MongoDB URI in [server/database.py](server/database.py) with your credentials
   - Replace the connection string with your MongoDB Atlas connection details

4. **Run the application**
   ```bash
   python main.py
   ```

   The server will start at `http://localhost:8000`

## API Endpoints

### Root Endpoint
- **GET** `/` - Welcome message
  ```json
  Response: { "message": "Welcome to this fantastic app!" }
  ```

### URL Management
- **POST** `/shorten` - Create a shortened URL
  ```
  Query Parameters: url (string) - Original URL to shorten
  ```
  
  Example Request:
  ```bash
  curl -X POST "http://localhost:8000/shorten?url=https://www.google.com/search?q=gemini+ai+is+awesome"
  ```

  Response:
  ```json
  {
    "data": [{
      "id": "65g8b3h9c2e1a4f6",
      "URL_ori": "https://www.google.com/search?q=gemini+ai+is+awesome",
      "Short_code": "abc123",
      "Created_at": "2026-04-06T10:24:30",
      "Update_at": "2026-04-06T10:24:30",
      "Access_count": 0
    }],
    "code": 200,
    "message": "Student added successfully."
  }
  ```

- **GET** `/shorten/` - Retrieve all shortened URLs
  
  Response:
  ```json
  {
    "data": [{...}, {...}],
    "code": 200,
    "message": "Url Retrived"
  }
  ```

## Data Model

### URL Schema

| Field | Type | Description |
|-------|------|-------------|
| id | String | MongoDB ObjectID |
| URL_ori | String | Original long URL |
| Short_code | String | 6-character random code |
| Created_at | DateTime | Timestamp of creation |
| Update_at | DateTime | Last update timestamp |
| Access_count | Integer | Number of times accessed |

## Usage Example

### Creating a Shortened URL

```bash
curl -X POST "http://localhost:8000/shorten?url=https://example.com/very/long/url/path"
```

### Retrieving All URLs

```bash
curl -X GET "http://localhost:8000/shorten/"
```

## Key Functions

### [server/database.py](server/database.py)

- `retrieve_urls()` - Get all shortened URLs
- `add_url(url_data)` - Add new URL to database
- `check_url(URL_ori)` - Check if URL already exists
- `retrieve_url(short_code)` - Get URL by short code
- `update_url(Short_code, data)` - Update URL information
- `delete_url(Short_code)` - Remove a shortened URL

### [server/routes/Url_shorten.py](server/routes/Url_shorten.py)

- `generate_short_code(length=6)` - Create random 6-character codes
- `Add_and_shorten_url(url)` - API endpoint for URL shortening
- `Get_URL_from_shortcode()` - API endpoint for retrieving URLs

## Error Handling

The API returns appropriate HTTP status codes and error messages:

```json
{
  "detail": "Error message here",
  "code": 404,
  "message": "URL not exist"
}
```

## Future Enhancements

- [ ] Add authentication and user accounts
- [ ] Custom short codes
- [ ] QR code generation
- [ ] Analytics dashboard
- [ ] URL expiration (TTL)
- [ ] Redirect functionality
- [ ] API rate limiting

## Notes

- Short codes are generated randomly using alphanumeric characters
- Duplicate URLs are detected and prevented during creation
- All timestamps are stored in UTC format
- MongoDB Atlas is used for cloud-based data persistence

## License

This project is open source and available under the MIT License.

## Contact & Support

For questions or issues, please create an issue in the repository.

---

**Happy URL Shortening!** 🚀
