import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    link TEXT PRIMARY KEY,
    title TEXT
)
""")

conn.commit()
conn.close()