import tkinter as tk

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="lightcoral")
        self.controller = controller
        
        label = tk.Label(self, text="Esta es la Página 2", bg="lightcoral")
        label.pack(pady=10)
        
        button = tk.Button(self, text="Volver a Inicio", bg="lightcoral",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack(pady=5)
        
        button2 = tk.Button(self, text="Ir a Página 1", bg="lightcoral",
                            command=lambda: controller.show_frame("PageOne"))
        button2.pack(pady=5)
