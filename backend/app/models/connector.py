from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from app.db.base_class import Base

class Connector(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    connector_type = Column(String)
    config_schema = Column(JSON)
