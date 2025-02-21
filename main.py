from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Model for input request
class DataRequest(BaseModel):
    data: List[str]

# Replace with your details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.get("/bfhl")
async def get_operation_code():
    return {"operation_code": 1}

@app.post("/bfhl")
async def process_data(request: DataRequest):
    numbers = []
    alphabets = []

    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)

    highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

    return {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
