import customtkinter as ctk
import SerialService  # Asegúrate de que SerialService esté correctamente importado

class Dificultad(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        parent.bind("<Key>", self.select_difficulty)

        # Variables para manejar la dificultad seleccionada
        self.selected_difficulty = 0

        # Contenedor principal
        container = ctk.CTkFrame(self, fg_color="#333333")
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
        inner_container.pack_propagate(False)
        inner_container.grid_columnconfigure((0, 1, 2), weight=1)

        # Configuración de dificultades
        self.frames = []
        difficulties = ["Fácil", "Medio", "Difícil"]
        descriptions = [
            "Ideal para principiantes. ¡Diviértete!",
            "Un reto moderado. ¡Prepárate!",
            "Solo para expertos. ¡Buena suerte!"
        ]
        colors = ["#7FFF00", "#FFA500", "#FF4500"]

        # Crear tarjetas de dificultad
        for i in range(3):
            frame = ctk.CTkFrame(inner_container, width=200, height=200, corner_radius=15, fg_color=colors[i])
            frame.grid(row=0, column=i, padx=20, pady=10, sticky="nsew")

            label = ctk.CTkLabel(frame, text=difficulties[i], font=("Courier", 20, "bold"), text_color="#FFFFFF")
            label.pack(expand=True, fill="both", pady=(15, 0))

            description_label = ctk.CTkLabel(frame, text=descriptions[i], font=("Courier", 14), text_color="#F0F0F0")
            description_label.pack(expand=True, fill="both", padx=10)

            key_label = ctk.CTkLabel(frame, text=f"Presiona {i + 1}", font=("Courier", 14, "italic"), text_color="#FFFFFF")
            key_label.pack(expand=True, fill="both", pady=10)

            self.frames.append(frame)

        # Vincular teclas a la función de selección en el widget raíz
    

    def highlight_difficulty(self, frame):
        """Resalta la tarjeta seleccionada."""
        for f in self.frames:
            f.configure(fg_color="transparent")  # Color original
        frame.configure(fg_color="#FFD700")  # Color resaltado (dorado)

    def select_difficulty(self, event):
        """Selecciona la dificultad según la tecla presionada y cambia la vista."""
        print()
        if event.keysym == '1':
            self.selected_difficulty = 0
            print("AH")
            self.highlight_difficulty(self.frames[0])
            SerialService.sendDifficulty(self.selected_difficulty)  # Enviar dificultad
            
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput
        elif event.keysym == '2':
            print("AH2")
            self.selected_difficulty = 1
            SerialService.sendDifficulty(self.selected_difficulty)  # Enviar dificultad
            self.highlight_difficulty(self.frames[1])
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput
        elif event.keysym == '3':
            print("AH3")
            self.selected_difficulty = 2
            SerialService.sendDifficulty(self.selected_difficulty)  # Enviar dificultad
            self.highlight_difficulty(self.frames[2])
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput