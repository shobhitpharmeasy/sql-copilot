from pydantic import BaseModel
from typing import List, Dict, Any

class QueryResponse(BaseModel):
    sql: str
    results: List[Dict[str, Any]]
    # Add more fields as needed
