from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.schemas import CodeRequest, ReviewResponse
from app.coordinator import CoordinatorAgent

app = FastAPI(title="Multi-Agent Code Review System")
coordinator = CoordinatorAgent()

@app.post("/review", response_model=ReviewResponse)
def review_code(req: CodeRequest):
    return coordinator.run(req.code)

# UI here
app.mount("/ui", StaticFiles(directory="web", html=True), name="ui")
