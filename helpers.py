from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship, declarative_base
from models import Base, SessionLocal

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    movies = relationship('Movie', back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"
    
    @classmethod
    def create(cls, session, name):
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category

