# 🎵 Rhythm Game Interface (En Desarrollo) 🎮  

¡Bienvenido a la **Interfaz de Juego de Ritmo**!  
Este es un proyecto en desarrollo, creado con **Python**, que busca ofrecer una experiencia interactiva para los jugadores de un juego de ritmo. Actualmente, la aplicación está enfocada en la interfaz visual y la gestión de puntajes, pero aún faltan características clave para su funcionalidad completa.  

---

## 📝 Estado del Proyecto  

⚠️ Este proyecto **no está completo**. Aunque tiene módulos para manejar una base de datos SQLite y comunicación serial con Arduino, **la integración con el hardware aún no está implementada**.  

---

## 🛠️ Requisitos  

- **Python**: 3.7.0  
- **SQLite3**: 3.43.2
- **pyserial**: 3.5.0  
- **customtkinter**: 5.2.2

Para instalar las dependencias (si hay librerías adicionales):  

```bash
pip install -r requirements.txt


📂 Estructura del Proyecto
plaintext
Copiar código
RhythmGameInterface/
├── db_services.py          # Servicios para la gestión de la base de datos SQLite.
├── serial_services.py      # Servicios para la comunicación serial con Arduino.
├── main.py                 # Archivo principal para ejecutar la aplicación.
├── arcade_scores.db        # Base de datos SQLite para almacenar puntajes.
├── assets/                 # Recursos visuales (íconos, imágenes, etc.).
└── Requirements.txt        # Para instalar los requisitos
└── README.md               # Este archivo.



🚀 Cómo Usar
Clona el repositorio:

bash
Copiar código
git clone https://github.com/tuusuario/RhythmGameInterface.git
Navega al directorio:

bash
Copiar código
cd RhythmGameInterface


Ejecuta la aplicación:

bash
Copiar código
pip install -r requirements.txt
python main.py
Explora las funcionalidades disponibles:

Selecciona la dificultad: Fácil, Media o Difícil.
Ingresa tu nombre.
Consulta tu puntaje al finalizar.
Ve los mejores 10 puntajes registrados en la base de datos.
Nota: Aunque incluye módulos para comunicación con Arduino, actualmente no hay conexión con hardware.

🎮 Características (Implementadas y Pendientes)
✔️ Implementadas
Interfaz Gráfica: Construida con Tkinter para una experiencia amigable.
Gestión de Base de Datos:
Registro y consulta de nombres y puntajes usando SQLite.
Visualización de los mejores puntajes en una tabla de clasificación.
Selección de Dificultad: Fácil, Media y Difícil.
❌ Pendientes
Integración con Arduino para el envío y recepción de datos.
Sincronización de la interfaz con el hardware para detectar interacciones del juego.
Animaciones y efectos visuales adicionales.
🛠️ Servicios Incluidos
🔧 Gestión de Base de Datos
Archivo: db_services.py
Funciones principales:

Registrar Puntaje: Guarda los datos del jugador y su puntaje.
Consultar Clasificación: Obtiene los mejores 10 puntajes registrados.
🔧 Comunicación Serial
Archivo: serial_services.py
Funciones principales:

Configurado para establecer comunicación con un Arduino a través del puerto serie. (No implementado en la interfaz actual)
📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usar, modificar y distribuir el código con libertad.

🙌 Créditos
Creado por Jorge Alejandro Exidoro López. Inspirado en el mundo de los juegos de ritmo y diseñado pensando en futuras integraciones con Arduino.

¡Gracias por tu interés! Si tienes ideas o comentarios, no dudes en contribuir o abrir un issue.

markdown
Copiar código

### Cambios:  
- **Estado del proyecto**: Incluí un aviso claro de que el proyecto no está completo.  
- **Créditos**: Agregué tu nombre completo.  
- **Pendientes**: Detallé las funcionalidades que faltan.
