from app.models.request import QueryRequest
from app.models.response import QueryResponse

class Orchestrator:
    async def process(self, request: QueryRequest) -> QueryResponse:
        # Placeholder for orchestrating downstream agents
        # Example: Call metadata_agent, understanding_agent, etc.
        return QueryResponse(sql="SELECT * FROM example", results=[])
