import serial.tools.list_ports as ports

ports = list(ports.comports())
for p in ports:
    print(p)
    if 'MyCDCDevice' in p.description:
        print(p)
        # Conexión al puerto
        s = serial.Serial(p.device)
