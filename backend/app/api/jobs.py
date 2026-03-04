from fastapi import APIRouter
router = APIRouter(tags=["Jobs"])

@router.get("/")
def get_jobs():
    return {"jobs": [], "message": "Jobs endpoint ready"}