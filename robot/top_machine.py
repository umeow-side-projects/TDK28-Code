from .raspberry.motor import Motor

try:
    top_motor = Motor(2, 3, 4)
except:
    pass

class TopMachine:
    @staticmethod
    def execute(direction):
        print("top_machine:", direction)
        if direction == 'right':
            top_motor.forward()
            pass

        if direction == 'left':
            top_motor.backward()
            pass

        if direction == 'stop':
            top_motor.stop()
            pass