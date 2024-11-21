import customtkinter as ctk
import ServicioDB
import SerialService




# declaramos las clases
root = ctk.CTk()
# Seteamos el colortheme de todos los widgets
ctk.set_default_color_theme("../assets/custom_theme.json")


SerialService.sendDifficulty(1)
getScore = SerialService.getScore()


# Funciones/Metodos:

# Limita la cantidad de caracteres en el entry
def limit_chars(event):

    current_text = event.widget.get()
    if len(current_text) > 4:
        event.widget.delete(4, "end")
# Insertar a la bd el score
def insert(event=None):
    score = "100"
    nombre = entry.get()
    ServicioDB.insert_score(score, nombre)



# Ventana (Configuracion de titulo, atributo pantalla completa)
root.title("PUNCH PUNCH MACHINE")
root.attributes("-fullscreen", True)



# Configuracion de la ventana para utilizar todo el espacio
frame = ctk.CTkFrame(root, fg_color="#333333")
frame.pack(pady=70, padx=70, fill="both", expand=True)


# Creamos columnas y filas para centrar widgets
frame.grid_columnconfigure((0,1,2,3,4), weight=1) 
frame.grid_rowconfigure((0,1,2), weight=1)  


# Titulo de la pantalla:
label = ctk.CTkLabel(frame, text="Registro de nombres")
label.grid(row = 0, column = 0, sticky="", columnspan=5)


# Label para el input
label = ctk.CTkLabel(frame, text=getScore, fg_color="#111111")
label.grid(row = 1, column = 1, sticky='ew', columnspan=1, padx="10")

# Score para el input
label = ctk.CTkLabel(frame, text="NOMBRE:", fg_color="#111111")
label.grid(row = 1, column = 2, sticky='ew', columnspan=1, padx="10")


# Input
entry = ctk.CTkEntry(frame, placeholder_text="USER")
entry.grid(row = 1,column = 2, sticky='ew', columnspan=2, padx="10")
entry.bind("<KeyRelease>", limit_chars)
entry.bind("<Return>", insert)


# Loop para que la ventana se ejecute
root.mainloop()