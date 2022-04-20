from sqlalchemy.orm import Session
from .models import Data
from .schemas import DataSchema


def get_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Data).offset(skip).limit(limit).all()


def get_data_by_id(db: Session, data_id: int):
    return db.query(Data).filter(Data.id == data_id).first()


def get_data_by_address(db: Session, data_address: int):
    return db.query(Data).filter(Data.ip_address == data_address).first()


def get_data_by_agent(db: Session, data_agent: int):
    return db.query(Data).filter(Data.user_agent == data_agent).first()


def create_data(db: Session, data: DataSchema):
    _data = Data(user_agent=data.user_agent, ip_address=data.ip_address)
    db.add(_data)
    db.commit()
    db.refresh(_data)
    return _data


def remove_data(db: Session, data_id: int):
    _data = get_data_by_id(db=db, data_id=data_id)
    db.delete(_data)
    db.commit()


def update_data(db: Session, data_id: int, user_agent: str, ip_address: str):
    _data = get_data_by_id(db=db, data_id=data_id)

    _data.user_agent = user_agent
    _data.ip_address = ip_address

    db.commit()
    db.refresh(_data)
    return _data


def exists(db: Session, user_agent: str, ip_address: str):
    _data_agent_exists = get_data_by_agent(db, user_agent) is not None
    _data_address_exists = get_data_by_address(db, ip_address) is not None
    return _data_agent_exists and _data_address_exists
