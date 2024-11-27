import sqlite3
import os
import logging

# Configuración de logging
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Ruta absoluta a la base de datos
RUTADB = os.path.abspath('db/arcade_scores.db')
print(RUTADB)
# Verificar existencia del directorio y crearlo si no existe
db_directory = os.path.dirname(RUTADB)
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

def get_connection():
    try:
        return sqlite3.connect(RUTADB)
    except sqlite3.Error as e:
        logging.error(f"No se pudo conectar a la base de datos: {e}")
        raise

def create_table():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS SCORES (
                    score INTEGER NOT NULL CHECK(score >= 0),
                    name TEXT NOT NULL CHECK(LENGTH(name) <= 4),
                    difficulty INTEGER NOT NULL CHECK(difficulty BETWEEN 0 AND 9)
                );
            """)
            connection.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al crear la tabla: {e}")

def insert_score(score, name, difficulty):
    print(score, name, difficulty)
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO SCORES (score, name, difficulty) VALUES (?, ?, ?)",
                (score, name, difficulty)
            )
            connection.commit()
    except sqlite3.Error as e:
        logging.error(f"Error al insertar puntaje: {e}")

def get_scores(limit=10):
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT score, name, difficulty FROM SCORES ORDER BY score DESC LIMIT ?",
                (limit,)
            )
            scores = cursor.fetchall()
            return scores
    except sqlite3.Error as e:
        logging.error(f"Error al obtener puntajes: {e}")
        return []

def check_table_exists():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SCORES';")
            table_exists = cursor.fetchone() is not None
            if table_exists:
                print("La tabla SCORES existe.")
            else:
                print("La tabla SCORES no existe.")
    except sqlite3.Error as e:
        logging.error(f"Error al verificar la tabla: {e}")
