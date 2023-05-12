from typing import Any
from sqlalchemy import create_engine, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

engine = create_engine('sqlite:///workers.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Projektas(Base):
    __tablename__ = "workers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=True)
    last_name = mapped_column(String(50), nullable=True)
    birth_date = mapped_column(Date, nullable=True)
    position = mapped_column(String(50), nullable=True)
    salary = mapped_column(Float(2), nullable=True)
    work_since = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            if key == 'birth_date':
                value = datetime.strptime(value, '%Y-%m-%d')
            setattr(self, key, value)
    
    def __repr__(self) -> str:
        return f"({self.id}, {self.name}, {self.last_name}, {self.birth_date}, {self.position}, {self.salary}, {self.work_since})"

Base.metadata.create_all(engine)

session.close()