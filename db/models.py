from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class DBAuthor(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, nullable=False)
    bio = Column(String(550))

    books = relationship("DBBook")


class DBBook(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    summary = Column(String(500))
    publication_date = Column(DateTime)
    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship(DBAuthor)
