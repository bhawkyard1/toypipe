from sqlalchemy.orm import relationship

class Relationship(Serializable):
	__tablename__ = "Relationship"
    id = Column(Integer, primary_key=True)

