from sqlalchemy import Column, Integer, String, JSON
from app.db.base_class import Base

class Workflow(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    nodes = Column(JSON)
