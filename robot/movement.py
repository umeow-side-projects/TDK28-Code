from .raspberry.motor import Motor

class Movement:
    right_ahead_wheel = Motor(24, 23, 21)
    right_rear_wheel = Motor(26, 19, 20)

    left_ahead_wheel = Motor(27, 17, 12)
    left_rear_wheel = Motor(5, 6, 13)
    
    right_ahead_wheel.stop()
    right_rear_wheel.stop()
    left_ahead_wheel.stop()
    left_rear_wheel.stop()
    
    @staticmethod
    def execute(direction):
        print("movement:", direction)
        if direction == 'forward':
            # wheel process...
            Movement.right_ahead_wheel.forward()
            Movement.right_rear_wheel.forward()
            Movement.left_ahead_wheel.forward()
            Movement.left_rear_wheel.forward()
            pass

        if direction == 'backward':
            # wheel process...
            Movement.right_ahead_wheel.backward()
            Movement.right_rear_wheel.backward()
            Movement.left_ahead_wheel.backward()
            Movement.left_rear_wheel.backward()
            pass

        # if direction == 'right':
        #     # wheel process...
        #     right_ahead_wheel.backward()
        #     right_rear_wheel.backward()
        #     left_ahead_wheel.forward()
        #     left_rear_wheel.forward()
        #     pass

        if direction == 'right':  #麥輪
            # wheel process...
            Movement.right_ahead_wheel.backward()
            Movement.right_rear_wheel.forward()
            Movement.left_ahead_wheel.forward()
            Movement.left_rear_wheel.backward()
            pass

        # if direction == 'left':
        #     # wheel process...
        #     right_ahead_wheel.forward()
        #     right_rear_wheel.forward()
        #     left_ahead_wheel.backward()
        #     left_rear_wheel.backward()
        #     pass

        if direction == 'left':   #麥輪
            # wheel process...
            Movement.right_ahead_wheel.forward()
            Movement.right_rear_wheel.backward()
            Movement.left_ahead_wheel.backward()
            Movement.left_rear_wheel.forward()
            pass

        if direction == 'stop':
            # wheel process...
            Movement.right_ahead_wheel.stop()
            Movement.right_rear_wheel.stop()
            Movement.left_ahead_wheel.stop()
            Movement.left_rear_wheel.stop()
            pass