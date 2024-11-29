import customtkinter as ctk
import ServicioDB
import SerialService

class ScoreInput(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Guarda la referencia al controlador
        self.getScore = None
        # Enviar dificultad y obtener el puntaje desde el servicio serial
        self.getScore = SerialService.getScore()
        print(self.getScore)
        #self.controller.dificultad = self.getDificultad
        # Funciones/Metodos:
        
        # Limita la cantidad de caracteres en el entry
        def limit_chars(event):
            current_text = event.widget.get()
            if len(current_text) > 6:
                event.widget.delete(6, "end")

        # Insertar a la base de datos el score
        def insert(event=None):
            print("Entro en el insert")
            nombre = entry.get()
            # dificultad = self.getDificultad  Cambiamos a un valor predeterminado para probar
            ServicioDB.insert_score(self.getScore, nombre, self.controller.dificultad )
            self.controller.show_frame("TopScore")  # Cambiar de vista a ScoreInput

        # Configuración de la ventana para utilizar todo el espacio
        frame = ctk.CTkFrame(self, fg_color="#333333")
        frame.pack(pady=70, padx=70, fill="both", expand=True)

        # Creamos columnas y filas para centrar widgets
        frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Título de la pantalla
        label = ctk.CTkLabel(
            frame, 
            font=("Press Start 2P", 52, "bold"), 
            text="Inserta tu nombre", 
            anchor="center"  # Centrado
        )
        label.grid(row=0, column=0, sticky="", columnspan=5)

        # Label para mostrar el puntaje obtenido (con márgenes internos)
        score_frame = ctk.CTkFrame(frame, fg_color="#111111")  # Contenedor para márgenes internos
        score_frame.grid(row=1, column=1, sticky="ew", columnspan=3, padx=10, pady=10)

        label = ctk.CTkLabel(
            score_frame,
            font=("Press Start 2P", 82, "bold"),
            text=self.getScore,
            fg_color="#FFFFFF"
        )
        label.pack(expand=True, fill="both", padx=20, pady=20)  # Márgenes internos

        # Texto para el input de nombre
        label = ctk.CTkLabel(
            frame, 
            text="NOMBRE:", 
            fg_color="#FFFFFF", 
            font=("Press Start 2P", 52, "bold"), 
            anchor="center"  # Centrado
        )
        label.grid(row=2, column=1, sticky='ew', columnspan=1, padx=10)

        # Input para el nombre
        entry = ctk.CTkEntry(
            frame, 
            placeholder_text="",
            font=("Press Start 2P", 24),  # Aumentar el tamaño de la fuente
            height=50
        )
        entry.grid(row=2, column=2, sticky='ew', columnspan=2, padx=10)
        entry.bind("<KeyRelease>", limit_chars)  # Límite de caracteres
        entry.bind("<Return>", insert)  # Insertar el nombre y puntaje

        # Establecer el foco en el input al iniciar
        entry.focus()


        # Vincular teclas para cambiar a otras vistas, si es necesario
        
        # self.bind("<e>", lambda event: self.controller.show_frame("Dificultad"))