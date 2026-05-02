"""Starter code for Building REST APIs with FastAPI.

Run locally (after installing dependencies):
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# In-memory storage for assignment practice.
books: list[Book] = []


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Book API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/books", response_model=Book)
def create_book(book: Book) -> Book:
    books.append(book)
    return book


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": f"Book {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
