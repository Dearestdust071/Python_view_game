import customtkinter as ctk
import time
import SerialService

class Contador(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.flagTimeOver = False
        
        self.time_left = 6  # Tiempo en segundos para el contador

        container = ctk.CTkFrame(self, fg_color="#333333")
        container.pack(fill="both", expand=True, padx=70, pady=70)

        title_label = ctk.CTkLabel(
            container,
            text="El juego comenzara en:",
            font=("Press Start 2P", 48, "bold"),
            text_color="#FFFFFF"
        )
        title_label.pack(pady=(60, 10))  # Ajuste del padding aquí

        # Label para el contador de tiempo
        self.timer_label = ctk.CTkLabel(
            container,
            text=f"Tiempo restante:",
            font=("Courier", 88),
            text_color="#FFFFFF",
        )
        self.timer_label.pack(pady=(200, 10))

        # Label para mostrar el número del contador
        self.timer_number = ctk.CTkLabel(
            container,
            text=f"{self.time_left}",
            font=("Courier", 128),
            text_color="#FFFFFF",
        )
        self.timer_number.pack(pady=(100, 10))  # Ajuste del padding aquí

        # Llamamos a la función para iniciar el contador
        self.update_timer()

    def update_timer(self):
        # Reducir el tiempo restante y actualizar la etiqueta
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f"Preparate:")
            if self.time_left !=0 :
                self.timer_number.configure(text=f"{self.time_left}")
            else:
                self.timer_number.configure(text="COMIENZA AHORA!", text_color="#FF0000" )
            # Actualizar el contador cada 1000 ms (1 segundo)
            self.after(1000, self.update_timer)
        else:
            # Cuando el tiempo se acaba, muestra el mensaje de inicio
           
            SerialService.sendDifficulty(self.controller.dificultad)
            # Si es necesario, descomenta esta línea para cambiar de pantalla:
            self.flagTimeOver = True
            time.sleep(1)
            self.controller.show_frame("ScoreInput")
            # self.controller.show_frame("ScoreInput")
