import sqlite3

create_table = "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, status TEXT)"

insert_task = "INSERT INTO tasks VALUES (NULL, ?, ?)"

get_all_tasks = "SELECT * FROM tasks"

get_task_by_id = "SELECT * FROM tasks WHERE id = ?"

with sqlite3.connect('TaskDb.db') as conn:
    cur = conn.cursor()
    cur.execute(create_table)




