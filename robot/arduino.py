# import json
# import serial

# ser = serial.Serial('/dev/ttyACM1',
#         baudrate=9600,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE)

# class Arduino:
#     @staticmethod
#     def execute(data):
#         data_json = json.loads(data)
#         pin = data_json['pin']
#         state = data_json['state']
        
#         buffer = pin << 1
#         buffer = buffer | state
        
#         buffer = buffer | 0x10
        
#         ser.write(bufferuffer)