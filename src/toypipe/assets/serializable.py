from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Serializable(Base):
    __tablename__ = "Serializable"
    id = Column(Integer, primary_key=True)
    
    # Username of whoever has published this.
    author = Column(String)

    # Whether this item is published and finalized.
    published = Column(Boolean)

    # The time that this item was last updated, if not published.
    # The time that this item was published, if it is published.
    publishTime = Column(Integer)

    #The workstation this item was published from.
    workstation = Column(String)

    def __init__(self):
        pass

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def markedForDeletion(self) -> bool:
        return self._markedForDeletion

    def publish(self):
        pass

    def serialize(self):
        pass
    