import sqlite3

conn = sqlite3.connect('banque.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_naissance TEXT NOT NULL,
    identifiant TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL,
    question_securite TEXT NOT NULL,
    reponse_securite TEXT NOT NULL
)
''')

conn.commit()
conn.close()