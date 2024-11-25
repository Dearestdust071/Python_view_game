import customtkinter as ctk
import SerialService
# Configuración de la ventana principal
# root = ctk.CTk()
root.title("Selecciona una Dificultad")
ctk.set_default_color_theme("../assets/custom_theme.json")
root.attributes("-fullscreen", True)

# Variables para manejar la dificultad seleccionada
selected_difficulty = 0

# Función para resaltar la tarjeta seleccionada
def highlight_difficulty(frame):
    """Resalta la tarjeta seleccionada."""
    for f in frames:
        f.configure(fg_color="transparent")  # Color original
    frame.configure(fg_color="#FFD700")  # Color resaltado (dorado)

def select_difficulty(event):
    """Selecciona la dificultad según la tecla presionada."""
    global selected_difficulty
    if event.keysym == '1':
        selected_difficulty = 0 
        highlight_difficulty(frames[0])
        SerialService.sendDifficulty(selected_difficulty)
        SerialService.getScore()
    elif event.keysym == '2':
        selected_difficulty = 1
        highlight_difficulty(frames[1])
    elif event.keysym == '3':
        selected_difficulty = 2
        highlight_difficulty(frames[2])
    

# Contenedor principal
container = ctk.CTkFrame(root, fg_color="#333333")
  # Fondo oscuro
#   Aqui esta el margen
container.pack(fill="both", expand=True, padx=70, pady=70)

# Título principal
title_label = ctk.CTkLabel(
    container,
    text="Selecciona tu Nivel de Dificultad",
    font=("Courier", 28, "bold"),
    text_color="#FFFFFF"
)
title_label.pack(pady=(20, 10))

# Subtítulo
subtitle_label = ctk.CTkLabel(
    container,
    text="Elige una opción con las teclas 1, 2 o 3",
    font=("Courier", 16),
    text_color="#BBBBBB"
)
subtitle_label.pack()

# Contenedor interno para alinear las tarjetas de dificultad
inner_container = ctk.CTkFrame(container, fg_color="#444444")
inner_container.pack(pady=40, padx=40, fill="x")
inner_container.pack_propagate(False)  # Evitar que el contenedor cambie de tamaño
inner_container.grid_columnconfigure((0, 1, 2), weight=1)  # Centrar tarjetas

# Configuración de dificultades
frames = []
difficulties = ["Fácil", "Medio", "Difícil"]
descriptions = [
    "Ideal para principiantes. ¡Diviértete!",
    "Un reto moderado. ¡Prepárate!",
    "Solo para expertos. ¡Buena suerte!"
]
colors = ["#7FFF00", "#FFA500", "#FF4500"]  # Verde, Naranja, Rojo

# Crear tarjetas de dificultad
for i in range(3):
    frame = ctk.CTkFrame(inner_container, width=200, height=200, corner_radius=15, fg_color=colors[i])
    frame.grid(row=0, column=i, padx=20, pady=10, sticky="nsew")
    
    # Título de dificultad
    label = ctk.CTkLabel(frame, text=difficulties[i], font=("Courier", 20, "bold"), text_color="#FFFFFF")
    label.pack(expand=True, fill="both", pady=(15, 0))
    
    # Descripción de dificultad
    description_label = ctk.CTkLabel(frame, text=descriptions[i], font=("Courier", 14), text_color="#F0F0F0")
    description_label.pack(expand=True, fill="both", padx=10)
    
    # Instrucción de teclas
    key_label = ctk.CTkLabel(frame, text=f"Presiona {i + 1}", font=("Courier", 14, "italic"), text_color="#FFFFFF")
    key_label.pack(expand=True, fill="both", pady=10)

    frames.append(frame)

# Vincular teclas a la función de selección
root.bind("<Key>", select_difficulty)

# Iniciar el bucle principal
root.mainloop()