from sqlalchemy import Column, Integer, String
from .config import Base


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    user_agent = Column(String)
    ip_address = Column(String)
