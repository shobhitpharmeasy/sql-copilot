import pytest

from app.agents.metadata_agent import MetadataAgent
from app.agents.understanding_agent import UnderstandingAgent
from app.agents.sql_generation_agent import SQLGenerationAgent
from app.agents.validation_agent import ValidationAgent
from app.agents.execution_agent import ExecutionAgent
from app.agents.postprocessing_agent import PostProcessingAgent
from app.agents.packaging_agent import PackagingAgent
from app.agents.retrieval_agent import RetrievalAgent

class TestAgents:
    @pytest.mark.asyncio
    async def test_metadata_agent(self):
        agent = MetadataAgent()
        result = await agent.fetch_metadata()
        assert "tables" in result

    @pytest.mark.asyncio
    async def test_understanding_agent(self):
        agent = UnderstandingAgent()
        result = await agent.parse_intent("Show me top 10 users")
        assert "intent" in result
        assert "entities" in result

    @pytest.mark.asyncio
    async def test_sql_generation_agent(self):
        agent = SQLGenerationAgent()
        result = await agent.generate_sql({"intent": "query", "entities": ["users"]}, {"tables": ["users"]})
        assert isinstance(result, str)

    @pytest.mark.asyncio
    async def test_validation_agent(self):
        agent = ValidationAgent()
        result = await agent.validate_sql("SELECT * FROM users LIMIT 10")
        assert result is True

    @pytest.mark.asyncio
    async def test_execution_agent(self):
        agent = ExecutionAgent()
        result = await agent.execute_sql("SELECT * FROM users LIMIT 10")
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_postprocessing_agent(self):
        agent = PostProcessingAgent()
        result = await agent.process_results([{"id": 1, "name": "John Doe"}])
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_packaging_agent(self):
        agent = PackagingAgent()
        result = await agent.package_response("SELECT * FROM users LIMIT 10", [{"id": 1, "name": "John Doe"}])
        assert hasattr(result, "sql")
        assert hasattr(result, "results")

    @pytest.mark.asyncio
    async def test_retrieval_agent(self):
        agent = RetrievalAgent()
        result = await agent.search("Show me top 10 users")
        assert isinstance(result, list)
