from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_ENGINE = create_engine("postgresql://ben:foo@localhost/database")
Session = sessionmaker(bind=_ENGINE)