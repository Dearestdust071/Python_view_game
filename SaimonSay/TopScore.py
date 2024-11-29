import customtkinter as ctk
import ServicioDB
from PIL import ImageFont, ImageTk
from PIL import Image, ImageDraw
from tkinter.font import Font
import os

# Ruta de tu archivo TTF
ruta_fuente = os.path.join(os.getcwd(), "PressStart2P-Regular.ttf")
class TopScore(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ServicioDB.create_table()  # Asegura que la tabla existe
        ServicioDB.check_table_exists()  # Verifica la existencia de la tabla
        self.controller = controller  # Guarda la referencia al controlador

        # Ejemplo de datos de prueba
        topScores = ServicioDB.get_scores()
        print("entro en topScore y saca topsccores?")
        print(topScores)

        # Definir colores
        colors = ["#c21700", "#ad7100", "#57ad00"]  # Rojo, Naranja, Verde

        # Contenedor superior (Difícil)
        container_top = ctk.CTkFrame(self, fg_color=colors[0], height=450)  # Rojo
        container_top.pack(side="top", fill="x", padx=20, pady=10)
        container_top.pack_propagate(False)

        title_top = ctk.CTkLabel(
            container_top,
            text="Difícil",
            font=("Press Start 2P", 32, "bold"),
            text_color="#FFFFFF"
        )
        title_top.pack(pady=20, anchor="center")

        # Contenedor inferior izquierda (Medio)
        container_bottom_left = ctk.CTkFrame(self, fg_color=colors[1], width=500)  # Naranja
        container_bottom_left.pack(side="left", expand=True, fill="both", padx=20, pady=10)
        container_bottom_left.pack_propagate(False)

        title_bottom_left = ctk.CTkLabel(
            container_bottom_left,
            text="Medio",
            font=("Press Start 2P", 32, "bold"),
            text_color="#FFFFFF"
        )
        title_bottom_left.pack(pady=20, anchor="center")

        # Contenedor inferior derecho (Fácil)
        container_bottom_right = ctk.CTkFrame(self, fg_color=colors[2], width=500)  # Verde
        container_bottom_right.pack(side="right", expand=True, fill="both", padx=20, pady=10)
        container_bottom_right.pack_propagate(False)

        title_bottom_right = ctk.CTkLabel(
            container_bottom_right,
            text="Fácil",
            font=("Press Start 2P", 32, "bold"),
            text_color="#FFFFFF"
        )
        title_bottom_right.pack(pady=20, anchor="center")

        cero = 0
        uno = 0
        dos = 0
        # Mostrar puntajes de prueba en cada contenedor
        for index, (score, name, difficulty) in enumerate(topScores):
            valorIndex = 0
            if difficulty == 0:
                cero += 1
                valorIndex = cero
                parent = container_bottom_right
            elif difficulty == 1:
                uno += 1
                valorIndex = uno
                parent = container_bottom_left
            elif difficulty == 2:
                dos += 1
                valorIndex = dos
                parent = container_top
            else:
                continue  # Ignorar si no coincide con ninguna dificultad

            score_label = ctk.CTkLabel(
                parent,
                text=f"{valorIndex}. {name}: {score}",
                font=("Courier", 28, "bold"),
                text_color="#FFFFFF"
            )
            score_label.pack(anchor="center", pady=5, padx=10)

        # Vincula la tecla para cambiar de vista
        self.controller.focus_set()
        self.controller.bind("<space>", lambda event: self.controller.show_frame("Dificultad"))