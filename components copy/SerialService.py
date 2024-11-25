import serial
import time

# ser = serial.Serial(port='/dev/cu.usbmodem11201', baudrate=9600, timeout=1)
# time.sleep(2)  # Espera a que se establezca la conexión



# ser.write(bytes("s", 'utf-8'))





# def configPort(timeout_screen):
#     """Funcion que retorne un objeto de la clase serial, timeout modificable"""
#     ser = serial.Serial()
#     ser.baudrate = 9600
#     ser.port = '/dev/cu.usbmodem1401'
#     ser.timeout  =  timeout_screen
#     # print(ser)
#     return ser    


ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/cu.usbmodem1401'
ser.timeout  =  None
ser.open()

time.sleep(2)

def sendDifficulty(difficulty):
    """Envia la dificultad, esta funcion solo puede ser un unico digito"""
    ser.write(bytes([difficulty]))
    

def getScore():
    print("Entro")
    msgrd = ser.readline().decode('utf-8').strip()
    print(f'Score final: {msgrd}')
    return msgrd


# sendDifficulty(0)
# getScore()


# #Todo 
# 1. Crear una funcion que retorne un objeto de la clase serial que pueda configurar  unicamente el timeout (para manejar el  tiempo de espera en lo que dura el juego  del arduino)
# 2. Crear una funcion que use la primer funcion y envie un mensaje numerico de un solo digito a el puerto 
# 3, Crear una funcion que use la primer funcion y reciba un mensaje (SCORE) (aqui  ya no sabre como mandarlo a llamar asincrono osea  no se si es aqui o donde)

