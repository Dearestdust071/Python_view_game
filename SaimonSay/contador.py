import customtkinter as ctk
import time
import SerialService  # Asegúrate de que SerialService esté correctamente importado

class Contador(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        
        container = ctk.CTkFrame(self, fg_color="#333333")
        container.pack(fill="both", expand=True, padx=70, pady=70)

        title_label = ctk.CTkLabel(
            container,
            text="Selecciona tu Nivel de Dificultad",
            font=("Courier", 28, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(pady=(20, 10))

        time.sleep(1)
        print(1)

        time.sleep(1)
        print(1)


        time.sleep(1)
        print(1)
        
        self.controller.show_frame("ScoreInput")



        


        