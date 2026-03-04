from fastapi import APIRouter
router = APIRouter(tags=["Resume"])

@router.get("/")
def get_resume():
    return {"resume": {}, "message": "Resume endpoint ready"}