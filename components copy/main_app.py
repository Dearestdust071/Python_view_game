
import tkinter as tk
from TopScore import TopScore
from ScoreInput import ScoreInput
from Dificultad import Dificultad


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cambiar vistas en Tkinter")
        self.geometry("400x300")
        
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
        # Función para mostrar una vista específica
        frame = self.frames[frame_name]
        frame.tkraise()
