# FastAPI MySQL Backend API

A simple, beginner-friendly backend API project built with FastAPI in Python, using **native SQL** to connect to a MySQL database.

## Project Structure

```text
fast/
├── main.py          # Main application file & route implementations
├── database.py      # Native SQL functions for database interaction
├── schemas.py       # Pydantic models for data validation
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Features

- **Basic Endpoints**: Greeting, Square calculation, and Addition.
- **Employee CRUD**: Fully functional CRUD operations using native SQL queries.
- **Database**: Connects to `tpdb` MySQL database.
- **Validation**: Strict type checking and validation using Pydantic.
- **Swagger Documentation**: Interactive API documentation available at `/docs`.

## How to Run

### 1. Install Dependencies
Make sure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```

### 2. Start the Server
Run the project using `uvicorn`:
```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

## API Documentation

Once the server is running, you can access:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Example Requests

- **GET `/hi`**: Simple greeting.
- **GET `/sqr/5`**: Returns `{"result": 25}`.
- **GET `/add?a=10&b=5`**: Returns `{"result": 15}`.
- **GET `/employees`**: List all employees.
- **POST `/employees`**: Add a new employee.
  ```json
  {
    "id": 3,
    "name": "Alice Wonderland",
    "role": "QA Engineer"
  }
  ```
