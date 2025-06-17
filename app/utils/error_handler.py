from fastapi import HTTPException

def handle_error(e: Exception):
    # Placeholder for standardizing exceptions into HTTP error responses
    raise HTTPException(status_code=500, detail=str(e))
