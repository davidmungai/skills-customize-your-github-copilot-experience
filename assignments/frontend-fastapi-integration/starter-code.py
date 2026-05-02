"""Starter backend for Frontend to API Integration with FastAPI.

Run:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Classroom Books API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


books: list[Book] = [
    Book(id=1, title="Python Crash Course", author="Eric Matthes", year=2019),
    Book(id=2, title="Automate the Boring Stuff", author="Al Sweigart", year=2020),
]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.post("/books", response_model=Book)
def create_book(book: Book) -> Book:
    books.append(book)
    return book
