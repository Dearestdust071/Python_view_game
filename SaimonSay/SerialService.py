import serial
import time
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
portMaestro = '/dev/cu.usbmodem14012'
for port in ports:
    print(port.description)
    if any(keyword in port.description for keyword in ["IOUSBHostDevice", "Arduino Uno", "ttyACM0"]):
        portMaestro = port.device
ser = serial.Serial()
ser.baudrate = 9600
ser.port = portMaestro
ser.timeout  =  None
try:
    if not ser.is_open:
        ser.open()
        print(f"Puerto {portMaestro} abierto con éxito.")
except serial.SerialException as e:
    print(f"Error al abrir el puerto {portMaestro}: {e}")

time.sleep(2)

def sendDifficulty(difficulty):
    print(difficulty)
    """Envia la dificultad, esta funcion solo puede ser un unico digito"""
    #ser.write(bytes([difficulty]))
    ser.write(f"{difficulty}\n".encode('utf-8'))

    

def getScore():
    """Recibe informacion del arduino"""
    print("Entro a getScore")
    while True:
        if ser.in_waiting > 0:  # Verifica si hay datos en el buffer de entrada
            msgrd = ser.readline().decode('utf-8').strip()  # Lee y decodifica la línea
            print(f'Score final: {msgrd}')
            if len(msgrd) != 4 or not msgrd.isdigit():
                raise ValueError("La entrada debe ser una cadena de exactamente 4 dígitos.")
            dificultad = int(msgrd[0])       # Primer dígito
            score = int(msgrd[1:])
            return dificultad , score


# sendDifficulty(0)
# getScore()


# #Todo 
# 1. Crear una funcion que retorne un objeto de la clase serial que pueda configurar  unicamente el timeout (para manejar el  tiempo de espera en lo que dura el juego  del arduino)
# 2. Crear una funcion que use la primer funcion y envie un mensaje numerico de un solo digito a el puerto 
# 3, Crear una funcion que use la primer funcion y reciba un mensaje (SCORE) (aqui  ya no sabre como mandarlo a llamar asincrono osea  no se si es aqui o donde)

