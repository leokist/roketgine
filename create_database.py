import sqlite3

con = sqlite3.connect("rocketgine.db")
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS propelentes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    composicaO_quimica TEXT NOT NULL,
    entalpia_formacao TEXT NOT NULL,
    massa_moleular TEXT NOT NULL
)""")

c.executemany("""INSERT INTO propelentes

""")

con.commit()
con.close()

