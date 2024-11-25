import sqlite3



# # Función para crear la tabla si no existe
def create_table():
    with sqlite3.connect("../db/arcade_scores.db") as cx:
        cu = cx.cursor()
        cu.execute("""
            CREATE TABLE IF NOT EXISTS SCORES (
                score VARCHAR(4),
                name VARCHAR(4),
                difficulty VARCHAR(1)
            );
        """)
        cx.commit()



# Función para insertar un puntaje
def insert_score(score, name, difficulty):
    try:
        with sqlite3.connect("../db/arcade_scores.db") as cx:
            cu = cx.cursor()
            cu.execute(
                "INSERT INTO SCORES (score, name, difficulty) VALUES (?, ?, ?)",
                (score, name, difficulty)
            )
            cx.commit()
    except sqlite3.Error as e:
        print(f"Error al insertar puntaje: {e}")



# Función para obtener los puntajes
def get_scores(limit=10):
    try:
        with sqlite3.connect("../db/arcade_scores.db") as cx:
            cu = cx.cursor()
            cu.execute(
                "SELECT score, name, difficulty FROM SCORES ORDER BY score DESC LIMIT ?",
                (limit,)
            )
            scores = cu.fetchall()
            return scores
    except sqlite3.Error as e:
        print(f"Error al obtener puntajes: {e}")
        return []
    

create_table()
insert_score("100", "Jorge", "0")