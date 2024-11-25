import customtkinter as ctk
import ServicioDB

class TopScore(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Guarda la referencia al controlador

        # Ejemplo de datos de prueba
        topScores = ServicioDB.get_scores()
        print("entro en topScore y saca topsccores?")
        print(topScores)

        # Definir colores
        colors = ["#FF4500", "#FFA500", "#7FFF00"]  # Rojo, Naranja, Verde

        # Contenedor superior (Difícil)
        container_top = ctk.CTkFrame(self, fg_color=colors[0], height=450)  # Rojo
        container_top.pack(side="top", fill="x", padx=20, pady=10)
        container_top.pack_propagate(False)

        title_top = ctk.CTkLabel(
            container_top,
            text="Difícil",
            font=("Courier", 28, "bold"),
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
            font=("Courier", 28, "bold"),
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
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        title_bottom_right.pack(pady=20, anchor="center")

        # Mostrar puntajes de prueba en cada contenedor
        for index, (name, score, difficulty) in enumerate(topScores):
            if difficulty == "0":
                parent = container_top
            elif difficulty == "1":
                parent = container_bottom_left
            elif difficulty == "2":
                parent = container_bottom_right
            else:
                continue  # Ignorar si no coincide con ninguna dificultad

            score_label = ctk.CTkLabel(
                parent,
                text=f"{index + 1}. {name}: {score}",
                font=("Arial", 18),
                text_color="#FFFFFF"
            )
            score_label.pack(anchor="center", pady=5, padx=10)

        # Vincula la tecla para cambiar de vista
        self.controller.focus_set()
        self.controller.bind("<space>", lambda event: self.controller.show_frame("Dificultad"))