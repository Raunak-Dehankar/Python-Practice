from fastapi import FastAPI, HTTPException
import sqlite3

#to launch FastAPI and handles the webpage
app = FastAPI()

# Database setup, creating a table here for the database users

#connecting to database
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
conn.commit()



# Create user
@app.post("/users/")
def create_user(user: dict):

    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user["name"], user["email"])
        )
        conn.commit()

        return {"message": "User created successfully"}

    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Email already exists")


# Read user data, basically get the database
@app.get("/users/")
def get_users():

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    result = []
    for user in users:
        result.append({
            "id": user[0],
            "name": user[1],
            "email": user[2]
        })

    return result


# Read one specific user 
@app.get("/users/{user_id}")
def get_user(user_id: int):

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user[0],
        "name": user[1],
        "email": user[2]
    }


# Updatr user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    cursor.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (updated_user["name"], updated_user["email"], user_id)
    )
    conn.commit()

    return {"message": "User updated successfully"}


# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    return {"message": "User deleted successfully"}