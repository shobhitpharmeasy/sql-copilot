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
