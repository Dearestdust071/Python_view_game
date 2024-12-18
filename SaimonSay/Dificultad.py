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
            font=("Press Start 2P", 36, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(pady=(20, 10))

        # Subtítulo
        subtitle_label = ctk.CTkLabel(
            container,
            text="Elige una opción con las teclas 1, 2 o 3",
            font=("Courier", 32),
            text_color="#BBBBBB"
        )
        subtitle_label.pack()

        # Contenedor interno para alinear las tarjetas de dificultad
        inner_container = ctk.CTkFrame(container, fg_color="#444444")
        inner_container.pack(pady=40, padx=40, fill="x")
        inner_container.pack_propagate(False)
        inner_container.grid_columnconfigure(0, weight=1)
        inner_container.grid_rowconfigure(0, weight=1) 

        # Configuración de dificultades
        self.frames = []
        difficulties = ["Fácil", "Medio", "Difícil"]
        descriptions = [
            "Ideal para principiantes. ¡Diviértete!",
            "Un reto moderado. ¡Prepárate!",
            "Solo para expertos. ¡Buena suerte!"
        ]
        colors = [ "#57ad00", "#ad7100", "#c21700"]

        for i in range(len(colors)):  # Configurar el peso de las filas dinámicamente
            inner_container.grid_rowconfigure(i, weight=1)
            inner_container.grid_columnconfigure(0, weight=1)

        for i in range(len(colors)):
            frame = ctk.CTkFrame(inner_container, corner_radius=15, fg_color=colors[i])
            frame.grid(row=i, column=0, padx=20, pady=40, sticky="nsew")

            frame.grid_rowconfigure(0, weight=1)
            frame.grid_rowconfigure(1, weight=1)
            frame.grid_rowconfigure(2, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            label = ctk.CTkLabel(frame, text=difficulties[i], font=("Press Start 2P", 30, "bold"), text_color="#FFFFFF", wraplength=500)
            label.grid(row=0, column=0, padx=10, pady=(15, 0), sticky="nsew")

            description_label = ctk.CTkLabel(frame, text=descriptions[i], font=("Courier", 20), text_color="#F0F0F0")
            description_label.grid(row=1, column=0, padx=10, sticky="nsew")

            key_label = ctk.CTkLabel(frame, text=f"Presiona {i + 1}", font=("Courier", 20, "italic"), text_color="#FFFFFF")
            key_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

            self.frames.append(frame)

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
            self.controller.dificultad = 0
            print("AH")
            self.highlight_difficulty(self.frames[0])
       
            
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput
        elif event.keysym == '2':
            print("AH2")
            self.selected_difficulty = 1
            self.controller.dificultad = 1

            self.highlight_difficulty(self.frames[1])
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput
        elif event.keysym == '3':
            print("AH3")
            self.selected_difficulty = 2
            self.controller.dificultad = 2
       
            self.highlight_difficulty(self.frames[2])
            self.controller.show_frame("Contador")  # Cambiar de vista a ScoreInput