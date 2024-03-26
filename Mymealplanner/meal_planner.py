import sqlite3

def connect():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    return conn, cur

def create_table():
    conn, cur = connect()
    cur.execute('CREATE TABLE IF NOT EXISTS meal_plans (id INTEGER PRIMARY KEY, name TEXT, day TEXT, recipe_id INTEGER, FOREIGN KEY(recipe_id) REFERENCES recipes(id))')
    conn.commit()
    conn.close()

def check_table_exists(table_name):
    conn, cur = connect()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    exists = cur.fetchone() is not None
    conn.close()
    return exists

if __name__ == "__main__":
    print("Is meal_plans table created:", check_table_exists("meal_plans"))
   

def create_meal_plan(name, day, recipe_id):
    conn, cur = connect()
    cur.execute('INSERT INTO meal_plans VALUES (NULL, ?, ?, ?)', (name, day, recipe_id))
    conn.commit()
    conn.close()

def view_meal_plans():
    conn, cur = connect()
    cur.execute('SELECT * FROM meal_plans')
    rows = cur.fetchall()
    conn.close()
    return rows
