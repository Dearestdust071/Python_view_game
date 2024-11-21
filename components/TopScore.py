import customtkinter as ctk
import ServicioDB

# Crear la ventana principal
root = ctk.CTk()
root.title("High Scores")
ctk.set_default_color_theme("../assets/custom_theme.json")
root.attributes("-fullscreen", True)

# Ejemplo de datos de prueba
topScores = ServicioDB.get_scores()
print(topScores)

# Contenedor principal
container = ctk.CTkFrame(root, fg_color="#333333", width=500, height=500)  # Tamaño mínimo para mejor visualización
container.pack(side="left", expand=True, fill="both", padx=20, pady=20)
container.pack_propagate(False)

# Contenedor secundario
container2 = ctk.CTkFrame(root, fg_color="#999999", width=500, height=500)  # Tamaño mínimo para mejor visualización
container2.pack(side="right", expand=True, fill="both", padx=20, pady=20)
container2.pack_propagate(False)

# Título principal dentro de `container`
title_label = ctk.CTkLabel(
    container,
    text="Top Scores",
    font=("Courier", 28, "bold"),
    text_color="#FFFFFF"
)
title_label.pack(pady=(20, 10))

# Muestra los puntajes en el contenedor secundario
for index, (name, score) in enumerate(topScores):
    score_label = ctk.CTkLabel(
        container2,
        text=f"{index + 1}. {name}: {score}",
        font=("Arial", 18),
        text_color="#FFFFFF"
    )
    score_label.pack(anchor="w", pady=5, padx=10)

root.mainloop()