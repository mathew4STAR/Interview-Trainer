from serial import Serial

bluetooth = Serial("COM6", baudrate=115200)

bluetooth.flushInput()

while True:
    print("what")
    input = bluetooth.readline()
    print(input)