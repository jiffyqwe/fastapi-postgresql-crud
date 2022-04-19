from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from .config import SessionLocal
from sqlalchemy.orm import Session
from .schemas import DataSchema, Request, Response, RequestData

from .crud import create_data, get_data, get_data_by_address, get_data_by_agent, get_data_by_id, exists, remove_data, update_data

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_data_entry(request: RequestData, db: Session = Depends(get_db)):
    create_data(db, data=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="data created successfully").dict(exclude_none=True)


@router.get("/")
async def get_datas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _datas = get_data(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_datas)



@router.delete("/delete")
async def delete_data(request: RequestData,  db: Session = Depends(get_db)):
    remove_data(db, data_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)

@router.post("/check")
async def check_exists(request: RequestData, db: Session = Depends(get_db)):
    _exists = exists(db, request.parameter.user_agent, request.parameter.ip_address)
    return Response(status="Ok", code="200", message="Success", result=_exists)
