from fastapi import FastAPI, Body
import pymysql

# docs_url=None and redoc_url=None disables the automatic documentation
app = FastAPI(docs_url=None, redoc_url=None)

# Database configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "%TGBbgt5",
    "database": "tpdb",
    "cursorclass": pymysql.cursors.DictCursor
}

def get_db():
    return pymysql.connect(**db_config)

@app.get("/hi")
async def hi():
    return {"message": "Hello World"}

@app.get("/sqr/{num}")
async def sqr(num: int):
    return {"result": num * num}

@app.post("/add")
async def add(num1: int = Body(...), num2: int = Body(...)):
    return {"addition": num1 + num2}

@app.get("/employees")
async def get_employees():
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM employee")
        data = cursor.fetchall()
    conn.close()
    return data

@app.post("/employees")
async def add_employee(name: str = Body(...), department: str = Body(...), salary: float = Body(...)):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)", (name, department, salary))
        conn.commit()
        new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "status": "success"}

@app.put("/employees/{id}")
async def update_employee(id: int, name: str = Body(None), department: str = Body(None), salary: float = Body(None)):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE employee SET name=%s, department=%s, salary=%s WHERE id=%s", (name, department, salary, id))
        conn.commit()
    conn.close()
    return {"message": "updated"}

@app.delete("/employees/{id}")
async def delete_employee(id: int):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM employee WHERE id = %s", (id,))
        conn.commit()
    conn.close()
    return {"message": "deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
