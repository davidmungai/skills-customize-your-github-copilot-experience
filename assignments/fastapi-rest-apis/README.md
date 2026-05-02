# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI and practice how backend services handle requests, validation, and responses. By the end of this assignment, you will create and test endpoints for managing a simple collection of books.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI app and implement foundational endpoints to confirm your API is running and can return data.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Implement a `GET /` endpoint that returns a welcome message in JSON
- Implement a `GET /health` endpoint that returns a status such as `{ "status": "ok" }`


### 🛠️ Add Data Models and Input Validation

#### Description
Define a Pydantic model for a `Book` and use it to validate incoming request data.

#### Requirements
Completed program should:

- Define a `Book` model with fields like `id`, `title`, `author`, and `year`
- Implement a `POST /books` endpoint that accepts a book payload and stores it in memory
- Return the created book in the response and reject invalid payloads automatically


### 🛠️ Implement Read and Delete Operations

#### Description
Finish the API by adding endpoints to list all books, get one book by id, and delete a book.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return a single book or a 404 error if not found
- Implement `DELETE /books/{book_id}` to remove a book and return a clear success message
