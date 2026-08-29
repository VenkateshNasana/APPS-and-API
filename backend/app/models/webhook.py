from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Webhook(Base):
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    event_type = Column(String)
