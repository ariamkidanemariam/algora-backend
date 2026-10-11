from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import auth, topics, problems, submissions, progress, projects, github

app=FastAPI(title="Algora API",version="1.0.0")
@app.on_event("startup")
def startup(): Base.metadata.create_all(bind=engine)
@app.get("/health",tags=["Health"])
def health(): return {"status":"ok"}
app.include_router(auth.router)
app.include_router(topics.router)
app.include_router(problems.router)
app.include_router(submissions.router)
app.include_router(progress.router)
app.include_router(projects.router)
app.include_router(github.router)
