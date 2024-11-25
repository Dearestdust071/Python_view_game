import customtkinter as ctk
import ServicioDB

# Crear la ventana principal
class TopScore(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__()
        # Ejemplo de datos de prueba
        topScores = ServicioDB.get_scores()
        print(topScores)

        # Definir colores
        colors = ["#FF4500", "#FFA500", "#7FFF00"]  # Rojo, Naranja, Verde

        # Contenedor superior (Dificil)
        container_top = ctk.CTkFrame(root, fg_color=colors[0], height=200)  # Rojo
        container_top.pack(side="top", fill="x", padx=20, pady=10)
        container_top.pack_propagate(False)

        title_top = ctk.CTkLabel(
            container_top,
            text="Difícil",
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        title_top.pack(pady=20)

        # Contenedor inferior izquierda (Medio)
        container_bottom_left = ctk.CTkFrame(root, fg_color=colors[1], width=500)  # Naranja
        container_bottom_left.pack(side="left", expand=True, fill="both", padx=20, pady=10)
        container_bottom_left.pack_propagate(False)

        title_bottom_left = ctk.CTkLabel(
            container_bottom_left,
            text="Medio",
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        title_bottom_left.pack(pady=20)

        # Contenedor inferior derecho (Fácil)
        container_bottom_right = ctk.CTkFrame(root, fg_color=colors[2], width=500)  # Verde
        container_bottom_right.pack(side="right", expand=True, fill="both", padx=20, pady=10)
        container_bottom_right.pack_propagate(False)

        title_bottom_right = ctk.CTkLabel(
            container_bottom_right,
            text="Fácil",
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        title_bottom_right.pack(pady=20)

        # Mostrar puntajes de prueba en cada contenedor
        # Filtrando por dificultad (esto dependerá de cómo esté organizada tu base de datos)
        for index, (name, score, difficulty) in enumerate(topScores):
            if difficulty == "Dificil":
                parent = container_top
            elif difficulty == "Medio":
                parent = container_bottom_left
            elif difficulty == "Fácil":
                parent = container_bottom_right
            else:
                continue  # Ignorar si no coincide con ninguna dificultad

            score_label = ctk.CTkLabel(
                parent,
                text=f"{index + 1}. {name}: {score}",
                font=("Arial", 18),
                text_color="#FFFFFF"
            )
            score_label.pack(anchor="w", pady=5, padx=10)

