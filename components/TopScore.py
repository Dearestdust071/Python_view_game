import customtkinter as ctk
import ServicioDB

# Crear la ventana principal
root = ctk.CTk()
root.title("High Scores")
root.attributes("-fullscreen", True)

# Ejemplo de datos de prueba
topScores = ServicioDB.get_scores()
print(topScores)

# Definir colores
colors = ["#FF4500", "#FFA500", "#7FFF00"]  # Rojo, Naranja, Verde

# Contenedor superior (Difícil) ocupa la mitad de la pantalla
container_top = ctk.CTkFrame(root, fg_color=colors[0], height=root.winfo_screenheight() // 2)  # Rojo
container_top.pack(side="top", fill="x", padx=20, pady=10)
container_top.pack_propagate(False)

title_top = ctk.CTkLabel(
    container_top,
    text="Difícil",
    font=("Courier", 28, "bold"),
    text_color="#FFFFFF"
)
title_top.pack(pady=20)

# Contenedor inferior izquierdo (Medio)
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

# Mostrar puntajes según dificultad
for index, (score, name, difficulty) in enumerate(topScores):
    if difficulty == "2":  # Difícil
        parent = container_top
    elif difficulty == "1":  # Medio
        parent = container_bottom_left
    elif difficulty == "0":  # Fácil
        parent = container_bottom_right
    else:
        continue  # Ignorar si no coincide con ninguna dificultad

    score_label = ctk.CTkLabel(
        parent,
        text=f"{index + 1}. {name}: {score}",
        font=("Arial", 18),
        text_color="#FFFFFF"
    )
    score_label.pack(anchor="center", pady=10)  # Centrado y con espaciado vertical
 
root.mainloop()