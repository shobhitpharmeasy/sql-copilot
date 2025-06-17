from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestRoutes:

    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_metadata_endpoint(self):
        response = client.get("/metadata")
        assert response.status_code == 200
        assert "tables" in response.json()

    def test_understanding_endpoint(self):
        response = client.post("/understand", json={"prompt": "Show me top 10 users"})
        assert response.status_code == 200
        assert "intent" in response.json()
        assert "entities" in response.json()

    def test_query_endpoint(self):
        response = client.post("/query", json={"prompt": "Show me top 10 users"})
        assert response.status_code == 200
        assert "sql" in response.json()
        assert "results" in response.json()
