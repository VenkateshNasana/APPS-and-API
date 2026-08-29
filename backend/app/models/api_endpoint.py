from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class ApiEndpoint(Base):
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True)
    method = Column(String)
    description = Column(String)
