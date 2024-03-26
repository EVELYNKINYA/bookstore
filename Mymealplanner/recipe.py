import sqlite3

def connect():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    return conn, cur

def create_table():
    conn, cur = connect()
    cur.execute('CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, instructions TEXT)')
    conn.commit()
    conn.close()

def add_recipe(name, ingredients, instructions):
    conn, cur = connect()
    cur.execute('INSERT INTO recipes VALUES (NULL, ?, ?, ?)', (name, ingredients, instructions))
    conn.commit()
    conn.close()

def view_recipes():
    conn, cur = connect()
    cur.execute('SELECT * FROM recipes')
    rows = cur.fetchall()
    conn.close()
    return rows

def find_recipe_by_id(recipe_id):
    conn, cur = connect()
    cur.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
    row = cur.fetchone()
    conn.close()
    return row

def find_recipes_by_keyword(keyword):
    conn, cur = connect()
    cur.execute('SELECT * FROM recipes WHERE name LIKE ? OR ingredients LIKE ?', ('%'+keyword+'%', '%'+keyword+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_recipe(recipe_id, name, ingredients, instructions):
    conn, cur = connect()
    cur.execute('UPDATE recipes SET name = ?, ingredients = ?, instructions = ? WHERE id = ?', (name, ingredients, instructions, recipe_id))
    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    conn, cur = connect()
    cur.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,))
    conn.commit()
    conn.close()

def filter_recipes_by_ingredients(ingredient):
    conn, cur = connect()
    cur.execute('SELECT * FROM recipes WHERE ingredients LIKE ?', ('%'+ingredient+'%',))
    rows = cur.fetchall()
    conn.close()
    return rows
