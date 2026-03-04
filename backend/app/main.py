from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import jobs, applications, analytics, resume

app = FastAPI(
    title="Job Platform API",
    description="AI-Powered Job Intelligence Platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobs.router,         prefix="/jobs")
app.include_router(applications.router, prefix="/applications")
app.include_router(analytics.router,    prefix="/analytics")
app.include_router(resume.router,       prefix="/resume")

@app.get("/")
def root():
    return {"status": "running", "message": "Job Platform API is live 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}