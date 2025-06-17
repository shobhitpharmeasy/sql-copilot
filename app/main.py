from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="SQL Copilot API",     version="1.0.0",
    docs_url="/swagger",
    redoc_url=None,
    swagger_ui_parameters={
        "tryItOutEnabled": True,
        "tagsSorter": "alpha",
        "operationsSorter": "alpha",
        "displayRequestDuration": True,
        # "defaultModelsExpandDepth": -1
    })

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, use_colors=True)

"""
TODO [CORE]:
  - [ ] 🎯 Implement centralized error handling middleware
        • Catch, normalize & format all exceptions
        • Ensure graceful degradation on agent errors
  - [ ] 🔐 Add authentication & authorization
        • JWT introspection
        • Role-based access checks
        • Token error handling (expired, malformed)
  - [ ] 📈 Integrate structured logging & correlation
        • Request‑ID propagation across all layers
        • Agent‑level logs with trace metadata
        • Include correlation IDs in streaming outputs

TODO [API]:
  1. `/query` Orchestration
      - [ ] Input validation & prompt sanitization
      - [ ] Orchestrate full agent pipeline via `MasterAgent`
      - [ ] Stream intermediate/final results (chunked, SSE or WebSocket)
      - [ ] Handle partial failures (e.g., SQL generated, but execution failed)
      - [ ] Return structured response: `{ sql, rows, explainPlan, summary }`
  2. (Future) Agent‑specific debug/test endpoints:
      - [ ] `/metadata`, `/understand`, `/generate-sql`, etc.
      - [ ] Enable isolated agent invocation & inspection for dev/debug

TODO [AGENTS]:
  - [ ] 📊 `MetadataAgent`
        • Fetch, normalize & cache OpenMetadata schemas
        • Support hybrid context (schema + usage logs if available)
  - [ ] 🧠 `DynamicRAGAgent`
        • Construct RAG pipeline dynamically for metadata injection
        • Inject context into prompts based on user question type
  - [ ] 🧠 `MemoryAgent`
        • Persist & retrieve conversation state
        • Use vector-based RAG over past queries, feedback, corrections
        • Manage context window limits with priority trimming
        • Support memory types: ephemeral, long-term, episodic
  - [ ] 🤖 `UnderstandingAgent`
        • NL → intent & entity extraction (e.g., metrics, filters)
        • Detect query type: ask, compare, aggregate, optimize
  - [ ] 📝 `SQLGenerationAgent`
        • Schema-aware SQL generation via templates or LLM
        • Handle user intent, joins, aggregations, filters
  - [ ] ✅ `ValidationAgent`
        • Check syntax, SQL-injection, reserved keywords
        • Enforce whitelist/blacklist of operations (e.g., no DDL)
  - [ ] ⚙️ `ExecutionAgent`
        • Execute SQL (`RUN`) and explain (`EXPLAIN`) using MCP server
        • Capture runtime errors and DB feedback
  - [ ] 🔍 `PlanAnalysisAgent`
        • Parse EXPLAIN plans
        • Identify inefficiencies (e.g., seq scan, missing index)
        • Recommend or trigger optimization
  - [ ] 🧪 `OptimizationAgent`
        • Iterate on SQL → EXPLAIN loop
        • Use MCP server to test & validate improvements
        • Summarize final rationale for changes
  - [ ] 🔄 `PostProcessingAgent`
        • Type coercion, null handling, pagination, formatting
  - [ ] 🎁 `PackagingAgent`
        • Assemble `{ sql, rows, summary, plan, trace }` for return
        • Attach metadata like source tables, tokens used, latency
  - [ ] 🔎 `RetrievalAgent` *(optional)*
        • Vector search for prior queries, docs, past results
        • Use Heystack or FAISS-backed embedding store
  - [ ] 🤝 `MasterAgent` (Orchestrator)
        • Top‑level controller for agent delegation
        • Can pause, inject clarifying sub-questions, or retry
        • Streams intermediate + final agent results to client
        • Supports dry-run (simulate without execution)

TODO [DEV EXPERIENCE]:
  - [ ] 🧰 Agent Dev Harness
        • CLI/mini UI to test individual agents with mock inputs
        • Snapshot memory state, step-through pipelines
        • Log intermediate agent outputs and traces

TODO [INFRA]:
  - [ ] 🛠️ LangFlow integration: map workflows to orchestrator
  - [ ] 🔄 Experiment with Dify as an alternative orchestration layer
  - [ ] 🗄️ Stand up `MCP` server
        • Support for Postgres, Snowflake, MySQL
        • Handle SQL execution + EXPLAIN interface + caching
        • Auth layer & logging built-in
  - [ ] ⚙️ Configure OpenMetadata client
        • Externalize URL, auth token in `config.py`
        • Enable schema preloading and polling

TODO [NEXT STEPS]:
  - [ ] 🧪 Testing strategy
        • Unit tests for each agent
        • Integration tests for multi-agent flows
        • End-to-end tests for `/query` (streaming & sync modes)
  - [ ] 🔄 CI/CD pipeline
        • Format, lint & type-check (Black, myPy, Checkstyle)
        • Dependency & SQL‑i security scans
        • Auto-deploy pipeline (dev → staging → prod)
  - [ ] 📊 Metrics & Monitoring
        • Per-agent success/failure & latency
        • MasterAgent orchestration metrics
        • DB query success/failure counts
        • Alerting on error thresholds
  - [ ] 📡 Observability & Tracing
        • OpenTelemetry-based tracing across agents
        • Correlate logs, metrics, traces via request ID
        • Enable distributed trace visualization (e.g., Jaeger)
  - [ ] 📚 Documentation
        • OpenAPI spec (including streaming event model)
        • Agent & memory customization how-tos
        • Architecture & troubleshooting guides
        • Quickstart + deployment instructions

MERMAID DIAGRAM:
(See `docs/architecture.md`, or paste below to visualize agent interactions)
"""
