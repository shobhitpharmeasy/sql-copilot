from fastapi import APIRouter, HTTPException
from app.models.request import QueryRequest
from app.models.response import QueryResponse
from app.agents.orchestrator import Orchestrator

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    try:
        orchestrator = Orchestrator()
        result = await orchestrator.process(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
