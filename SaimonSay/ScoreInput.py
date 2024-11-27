import customtkinter as ctk
import ServicioDB
import SerialService

class ScoreInput(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Guarda la referencia al controlador
        
        # Enviar dificultad y obtener el puntaje desde el servicio serial
        # SerialService.sendDifficulty(1)
        self.getScore = SerialService.getScore()
    

        # Funciones/Metodos:
        
        # Limita la cantidad de caracteres en el entry
        def limit_chars(event):
            current_text = event.widget.get()
            if len(current_text) > 4:
                event.widget.delete(4, "end")

        # Insertar a la base de datos el score
        def insert(event=None):
            print("Entro en el isnert")
            score = "100"  # Asumir un puntaje por defecto (se puede modificar)
            nombre = entry.get()
            dificultad = "0"
            ServicioDB.insert_score(score, nombre, dificultad )
            self.controller.show_frame("TopScore")  # Cambiar de vista a ScoreInput

        # Configuración de la ventana para utilizar todo el espacio
        frame = ctk.CTkFrame(self, fg_color="#333333")
        frame.pack(pady=70, padx=70, fill="both", expand=True)

        # Creamos columnas y filas para centrar widgets
        frame.grid_columnconfigure((0,1,2,3,4), weight=1) 
        frame.grid_rowconfigure((0,1,2), weight=1)  

        # Título de la pantalla:
        label = ctk.CTkLabel(frame, text="Registro de nombres")
        label.grid(row=0, column=0, sticky="", columnspan=5)

        # Label para mostrar el puntaje obtenido
        label = ctk.CTkLabel(frame, text=self.getScore, fg_color="#111111")
        label.grid(row=1, column=1, sticky='ew', columnspan=1, padx="10")

        # Texto para el input de nombre
        label = ctk.CTkLabel(frame, text="NOMBRE:", fg_color="#111111")
        label.grid(row=1, column=2, sticky='ew', columnspan=1, padx="10")

        # Input para el nombre
        entry = ctk.CTkEntry(frame, placeholder_text="USER")
        entry.grid(row=1, column=2, sticky='ew', columnspan=2, padx="10")
        entry.bind("<KeyRelease>", limit_chars)  # Límite de caracteres
        entry.bind("<Return>", insert)  # Insertar el nombre y puntaje

        # Establecer el foco en el input al iniciar
        entry.focus()

        # Vincular teclas para cambiar a otras vistas, si es necesario
        
        # self.bind("<Escape>", lambda event: self.controller.show_frame("Dificultad"))