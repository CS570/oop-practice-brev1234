from motor import Motor

class Robot:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.left_motor = Motor()
        self.right_motor = Motor()

    def drive_forward(self, speed: float):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

    def reverse(self):
        self.left_motor.reverse()
        self.right_motor.reverse()

    def turn_left(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(1)

    def turn_right(self):
        self.left_motor.set_speed(1)
        self.right_motor.set_speed(0)