import customtkinter as ctk
from TopScore import TopScore
from ScoreInput import ScoreInput
from Dificultad import Dificultad
from contador import Contador

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PUNCH PUNCH MACHINE")
        self.wm_attributes('-fullscreen', True)
        self.state('normal')

        # Variable para mantener referencia al frame actual
        self.current_frame = None

        # Diccionario para mapear nombres de vistas a clases
        self.frame_classes = {
            "TopScore": TopScore,
            "ScoreInput": ScoreInput,
            "Dificultad": Dificultad,
            "Contador": Contador
        }

        # Configuración de la cuadrícula en el root
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Mostrar la vista inicial
        self.show_frame("Contador")
    
    def show_frame(self, frame_name):
        """Función para mostrar una vista específica."""
        # Destruir el frame actual si existe
        if self.current_frame is not None:
            self.current_frame.destroy()

        # Crear y mostrar el nuevo frame
        FrameClass = self.frame_classes.get(frame_name)
        if FrameClass:
            self.current_frame = FrameClass(self, self)
            self.current_frame.grid(row=0, column=0, sticky="nsew")
            print(f"Cambiando a la vista: {frame_name}")  # Solo para depuración
        else:
            print(f"Vista {frame_name} no encontrada.")  # Para depuración

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()