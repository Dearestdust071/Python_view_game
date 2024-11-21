import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="lightgreen")
        self.controller = controller
        
        label = tk.Label(self, text="Esta es la Página 1", bg="lightgreen")
        label.pack(pady=10)
        
        button = tk.Button(self, text="Volver a Inicio", bg="lightgreen",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack(pady=5)
        
        button2 = tk.Button(self, text="Ir a Página 2", bg="lightgreen",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack(pady=5)
