import sqlite3
import requests

print("Pobieranie danych z API...")
response = requests.get("https://randomuser.me/api/?results=30")
users = response.json()["results"]

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    age INTEGER,
    gender TEXT,
    country TEXT
)
''')

cursor.execute("DELETE FROM Users")

insert_query = '''
INSERT INTO Users (first_name, last_name, email, age, gender, country)
VALUES (?, ?, ?, ?, ?, ?)
'''

print("Zapisywanie danych do bazy SQLite...")
for user in users:
    first_name = user['name']['first']
    last_name = user['name']['last']
    email = user['email']
    age = user['dob']['age']
    gender = user['gender']
    country = user['location']['country']
    
    cursor.execute(insert_query, (first_name, last_name, email, age, gender, country))

conn.commit()

print("\n--- WYNIKI ANALIZY ---")

cursor.execute("SELECT gender, COUNT(*) FROM Users GROUP BY gender")
print("\n1. Podział na płeć:")
for row in cursor.fetchall():
    print(f" - {row[0]}: {row[1]}")

cursor.execute("SELECT AVG(age) FROM Users")
avg_age = cursor.fetchone()[0]
print(f"\n2. Średni wiek użytkowników: {avg_age:.1f} lat")

cursor.execute("SELECT COUNT(DISTINCT country) FROM Users")
countries_count = cursor.fetchone()[0]
print(f"\n3. Użytkownicy mieszkają łącznie w {countries_count} krajach.")

cursor.execute("SELECT country, COUNT(*) FROM Users GROUP BY country ORDER BY COUNT(*) DESC")
print("\nRozkład na poszczególne kraje:")
for row in cursor.fetchall():
    print(f" - {row[0]}: {row[1]}")

conn.close()