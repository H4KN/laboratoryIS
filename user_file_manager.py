# user_file_manager.py
from user import User
import sqlite3

class UserFileManager:
    @staticmethod
    def initDB():
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            role TEXT,
            password TEXT
        )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def saveUserToDB(user):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users (id, name, role, password) VALUES (?, ?, ?, ?)
        ''', (user.id, user.name, user.role, user.password))
        conn.commit()
        conn.close()

    @staticmethod
    def updateUserInDB(user):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE users SET name = ?, role = ?, password = ? WHERE id = ?
        ''', (user.name, user.role, user.password, user.id))
        conn.commit()
        conn.close()

    @staticmethod
    def removeUserFromDB(user):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM users WHERE id = ?
        ''', (user.id,))
        conn.commit()
        conn.close()

    @staticmethod
    def getUserFromDB(id):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE id = ?
        ''', (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1], row[2], row[3])
        return None

    @staticmethod
    def getUsersFromDB():
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users
        ''')
        rows = cursor.fetchall()
        conn.close()
        users = []
        for row in rows:
            users.append(User(row[0], row[1], row[2], row[3]))
        return users

# Initialize the database if it doesn't exist
UserFileManager.initDB()