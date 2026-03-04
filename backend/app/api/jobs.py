from fastapi import APIRouter, Query
from app.config import supabase

router = APIRouter(tags=["Jobs"])

@router.get("/")
def get_jobs(
    search: str = Query(None),
    company: str = Query(None),
    remote: bool = Query(None),
    limit: int = Query(20),
    offset: int = Query(0)
):
    query = supabase.table("jobs").select("*").eq("is_active", True)

    if search:
        query = query.ilike("title", f"%{search}%")
    if company:
        query = query.ilike("company_name", f"%{company}%")
    if remote is not None:
        query = query.eq("remote", remote)

    result = query.order("date_posted", desc=True).range(offset, offset + limit - 1).execute()
    return {"jobs": result.data, "count": len(result.data)}

@router.get("/{job_id}")
def get_job(job_id: str):
    result = supabase.table("jobs").select("*").eq("id", job_id).single().execute()
    return result.data