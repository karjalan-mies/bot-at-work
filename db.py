import sqlite3

conn = sqlite3.connect('my_database.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS messages(key TEXT, value TEXT);")
cur.execute("""INSERT INTO messages(key, value) 
VALUES('east_conf', 'Описание восточной конференции')""")
conn.commit()

# cur.execute("SELECT value FROM messages WHERE key='west_conf'")
# one_result = cur.fetchone()
# print(one_result)
