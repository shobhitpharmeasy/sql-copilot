from pydantic import BaseModel

class QueryRequest(BaseModel):
    prompt: str
    # Add more fields as needed
