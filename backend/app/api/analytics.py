from fastapi import APIRouter
router = APIRouter(tags=["Analytics"])

@router.get("/")
def get_analytics():
    return {"analytics": {}}
