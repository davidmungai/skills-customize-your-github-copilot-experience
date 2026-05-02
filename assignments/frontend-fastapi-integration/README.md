# 📘 Assignment: Frontend to API Integration with FastAPI

## 🎯 Objective

Connect a simple webpage to a FastAPI backend so students can fetch and display live data from REST endpoints. Students will practice making HTTP requests with JavaScript and rendering API responses in the browser.

## 📝 Tasks

### 🛠️ Run and Verify the FastAPI Backend

#### Description
Start the provided FastAPI app and test that the endpoints return JSON responses.

#### Requirements
Completed program should:

- Run the backend server locally with Uvicorn
- Confirm `GET /health` returns a successful status JSON response
- Confirm `GET /books` returns a JSON list


### 🛠️ Fetch API Data from the Frontend

#### Description
Complete the frontend JavaScript logic to request book data from the API and display it on the page.

#### Requirements
Completed program should:

- Use `fetch()` to call `GET /books` from the browser
- Parse the JSON response and render each book in a visible list
- Display a clear error message if the request fails


### 🛠️ Submit New Data from the Frontend

#### Description
Add form handling so users can submit a new book entry from the webpage to the backend.

#### Requirements
Completed program should:

- Collect form values for `id`, `title`, `author`, and `year`
- Send a `POST /books` request with JSON data
- Refresh the displayed book list after a successful submission
