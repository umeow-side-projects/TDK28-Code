from time import sleep
from .arduino.arduino import Arduino
from .arduino.arduino_motor import ArduinoMotor
from ..joystick.joystick import Joystick
from ..utils import mapping

class Movement:
    right_wheel = ArduinoMotor(pwm_pin=2, forward_pin=24, backward_pin=25)
    left_wheel = ArduinoMotor(pwm_pin=3, forward_pin=22, backward_pin=23)
    
    state = 'stop'
    
    button_last_state = 0
    inverse = False
    
    def brightness_circle():
        while True:
            for birghtness in range(0, 256, 15):
                if not Movement.inverse:
                    Arduino.analogWrite(8, 255)
                    Arduino.analogWrite(9, birghtness)
                    Arduino.analogWrite(10, 255)
                    Arduino.analogWrite(11, birghtness)
                    Arduino.analogWrite(12, 255)
                    Arduino.analogWrite(13, 255)
                else:
                    Arduino.analogWrite(8, birghtness)
                    Arduino.analogWrite(9, 255)
                    Arduino.analogWrite(10, 255)
                    Arduino.analogWrite(11, 255)
                    Arduino.analogWrite(12, birghtness)
                    Arduino.analogWrite(13, 255)
                sleep(0.1)
            for birghtness in range(0, 256, 15)[::-1]:
                if not Movement.inverse:
                    Arduino.analogWrite(8, 255)
                    Arduino.analogWrite(9, birghtness)
                    Arduino.analogWrite(10, 255)
                    Arduino.analogWrite(11, birghtness)
                    Arduino.analogWrite(12, 255)
                    Arduino.analogWrite(13, 255)
                else:
                    Arduino.analogWrite(8, birghtness)
                    Arduino.analogWrite(9, 255)
                    Arduino.analogWrite(10, 255)
                    Arduino.analogWrite(11, 255)
                    Arduino.analogWrite(12, birghtness)
                    Arduino.analogWrite(13, 255)
                sleep(0.1)
    
    @Joystick.when_axis_left_change_wrapper
    def joystick_axis_left_update(value, *args, **kwargs):    
        if value[2] and value[2] != Movement.button_last_state:
            Movement.inverse = not Movement.inverse
        
        # if Movement.inverse:
        #     ArduinoLight.fill(0, 255, 0, 0, True)
        #     ArduinoLight.fill(1, 0, 255, 0, True)
        # else:
        #     ArduinoLight.fill(0, 0, 255, 0, True)
        #     ArduinoLight.fill(1, 255, 0, 0, True)
        
        abs_x, abs_y = abs(value[0]), abs(value[1])
          
        if abs_x < 500 and abs_y < 500:
            return
        
        if abs(value[0]) < 15000 and value[1] > 16000:
            Movement.forward()
            
            # print(abs(value[1]))
            if abs_y < 30393:
                speed = mapping(abs_y, 16000, 30392, 60, 150)
            else:
                speed = mapping(abs_y, 30393, 32767, 150, 255)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
        
        elif abs(value[0]) < 15000 and value[1] < -16000:
            Movement.backward()
            
            if abs_y < 30393:
                speed = mapping(abs_y, 16000, 30392, 60, 150)
            else:
                speed = mapping(abs_y, 30393, 32767, 150, 255)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
            
        elif value[0] > 16000 and abs(value[1]) < 15000:
            Movement.right()
            
            if abs_x < 30393:
                speed = mapping(abs_x, 16000, 30392, 100, 200)
            else:
                speed = mapping(abs_x, 30393, 32767, 200, 255)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
        
        elif value[0] < -16000 and abs(value[1]) < 15000:
            Movement.left()
            
            if abs_x < 30393:
                speed = mapping(abs_x, 16000, 30392, 100, 200)
            else:
                speed = mapping(abs_x, 30393, 32767, 200, 255)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)

        else:
            Movement.stop()
        
        Movement.button_last_state = value[2]
    
    @Joystick.when_axis_right_change_wrapper
    def joytick_axis_right_update(value, *args, **kwargs):
        abs_x, abs_y = abs(value[0]), abs(value[1])
        
        if abs_x < 500 and abs_y < 500:
            return
        
        if abs(value[0]) < 15000 and value[1] > 16000:
            Movement.forward()
            
            # print(abs(value[1]))
            if abs_y < 30393:
                speed = mapping(abs_y, 16000, 30392, 40, 60)
            else:
                speed = mapping(abs_y, 30393, 32767, 60, 80)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
        
        elif abs(value[0]) < 15000 and value[1] < -16000:
            Movement.backward()
            
            if abs_y < 30393:
                speed = mapping(abs_y, 16000, 30392, 40, 60)
            else:
                speed = mapping(abs_y, 30393, 32767, 60, 80)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
            
        elif value[0] > 16000 and abs(value[1]) < 15000:
            Movement.right()
            
            if abs_x < 30393:
                speed = mapping(abs_x, 16000, 30392, 50, 100)
            else:
                speed = mapping(abs_x, 30393, 32767, 100, 180)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)
        
        elif value[0] < -16000 and abs(value[1]) < 15000:
            Movement.left()
            
            if abs_x < 30393:
                speed = mapping(abs_x, 16000, 30392, 50, 100)
            else:
                speed = mapping(abs_x, 30393, 32767, 100, 180)
            # print(f"setSpeed: {speed}")
            Movement.right_wheel.setSpeed(speed)
            Movement.left_wheel.setSpeed(speed)

        else:
            Movement.stop()
    
    @staticmethod
    def forward():
        if Movement.state == 'forward':
            return
        print('movement: forward')
        Movement.left_wheel.forward(inverse=Movement.inverse)
        Movement.right_wheel.forward(inverse=Movement.inverse)
        Movement.state = 'forward'
    
    @staticmethod
    def backward():
        if Movement.state == 'backward':
            return
        print('movement: backward')
        Movement.left_wheel.backward(inverse=Movement.inverse)
        Movement.right_wheel.backward(inverse=Movement.inverse)
        Movement.state = 'backward'
    
    @staticmethod
    def right():
        if Movement.state == 'right':
            return
        print('movement: right')
        Movement.left_wheel.forward()
        Movement.right_wheel.backward()
        Movement.state = 'right'
    
    @staticmethod
    def left():
        if Movement.state == 'left':
            return
        print('movement: left')
        Movement.left_wheel.backward()
        Movement.right_wheel.forward()
        Movement.state = 'left'
    
    @staticmethod
    def stop():
        if Movement.state == 'stop':
            return
        print('movement: stop')
        Movement.left_wheel.stop()
        Movement.right_wheel.stop()
        Movement.state = 'stop'
    
    @staticmethod
    def execute(direction):
        if direction == 'forward':
            Movement.forward()

        if direction == 'backward':
            Movement.backward()

        if direction == 'right':
            Movement.right()

        # if direction == 'right':  #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.backward()
        #     Movement.right_rear_wheel.forward()
        #     Movement.left_ahead_wheel.forward()
        #     Movement.left_rear_wheel.backward()
        #     pass

        if direction == 'left':
            Movement.left()

        # if direction == 'left':   #麥輪
        #     # wheel process...
        #     Movement.right_ahead_wheel.forward()
        #     Movement.right_rear_wheel.backward()
        #     Movement.left_ahead_wheel.backward()
        #     Movement.left_rear_wheel.forward()
        #     pass

        # if direction == 'clockwise':
        #     Movement.right_wheel.backward()
        #     Movement.left_wheel.forward()
        #     pass
            
        # if direction == 'counterclockwise':
        #     Movement.right_wheel.forward()
        #     Movement.left_wheel.backward()
        #     pass

        if direction == 'stop':
            Movement.stop()
        
        # if soft and direction != 'stop':
        #     for speed in range(100, 256):
        #         Movement.right_wheel.setSpeed(speed)
        #         Movement.left_wheel.setSpeed(speed)
        #         sleep(0.005)
        # elif soft:
        #     for speed in range(0, 101)[::-1]:
        #         Movement.right_wheel.setSpeed(speed)
        #         Movement.left_wheel.setSpeed(speed)
        #         sleep(0.005)
        #     Movement.right_wheel.stop()
        #     Movement.left_wheel.stop()
                