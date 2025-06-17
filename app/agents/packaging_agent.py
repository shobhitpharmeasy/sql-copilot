from app.models.response import QueryResponse

class PackagingAgent:
    async def package_response(self, sql: str, results: list) -> QueryResponse:
        # Placeholder for wrapping final SQL and data into the JSON response model
        return QueryResponse(sql=sql, results=results)
