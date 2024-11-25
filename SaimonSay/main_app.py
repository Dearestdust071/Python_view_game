import customtkinter as ctk
from TopScore import TopScore
from ScoreInput import ScoreInput
from Dificultad import Dificultad

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PUNCH PUNCH MACHINE")
        self.wm_attributes('-fullscreen', True)
        self.state('normal')

        # Diccionario para almacenar las instancias de las vistas
        self.frames = {}

        # Configuración de la cuadrícula en el root
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Inicializar las vistas y añadirlas al diccionario
        for FrameClass in (Dificultad, ScoreInput, TopScore):
            frame = FrameClass(self, self)
            self.frames[FrameClass.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Mostrar la vista inicial
        self.show_frame("TopScore")
    
    def show_frame(self, frame_name):
        """Función para mostrar una vista específica."""
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()
            print(f"Cambiando a la vista: {frame_name}")  # Solo para depuración
        else:
            print(f"Vista {frame_name} no encontrada.")  # Para depuración