import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        
        label = tk.Label(self, text="Página de inicio", bg="lightblue")
        label.pack(pady=10)
        
        button1 = tk.Button(self, text="Ir a Página 1", bg="lightblue",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack(pady=5)
        
        button2 = tk.Button(self, text="Ir a Página 2", bg="lightblue",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack(pady=5)
