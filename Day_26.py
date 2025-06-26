from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory database
books: List[Book] = []

# Create
@app.post("/books/", status_code=201)
def add_book(book: Book):
    # Check for duplicate ID
    if any(b.id == book.id for b in books):
        raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return {"msg": "Book added"}

# Read all
@app.get("/books/", response_model=List[Book])
def get_books():
    return books

# Read single
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Update
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return {"msg": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")

# Delete
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
            return {"msg": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
