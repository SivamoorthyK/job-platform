from fastapi import APIRouter
router = APIRouter(tags=["Applications"])

@router.get("/")
def get_applications():
    return {"applications": [], "message": "Applications endpoint ready"}