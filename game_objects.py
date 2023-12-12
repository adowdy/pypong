# game_objects.py
# Contains the classes for the different game elements like paddles and ball.

class Paddle:
    """
    Represents a paddle in the game with position, speed, and key bindings for movement.
    """
    def __init__(self, position, speed, key_up, key_down):
        self.position = position  # Paddle's starting position on screen as a tuple (x, y)
        self.speed = speed        # Speed at which the paddle moves
        self.key_up = key_up      # Key binding to move the paddle up
        self.key_down = key_down  # Key binding to move the paddle down

    def move_up(self):
        """
        Moves the paddle up by its speed.
        """
        self.position = (self.position[0], self.position[1] - self.speed)

    def move_down(self):
        """
        Moves the paddle down by its speed.
        """
        self.position = (self.position[0], self.position[1] + self.speed)

    def get_position(self):
        """
        Returns the current position of the paddle.
        """
        return self.position


class Ball:
    """
    Represents the ball in the game with position and velocity.
    """
    def __init__(self, position, velocity):
        self.position = position  # Ball's starting position on screen as a tuple (x, y)
        self.velocity = velocity  # Current velocity of the ball as a tuple (x_speed, y_speed)

    def update_position(self):
        """
        Updates the ball's position based on its velocity.
        """
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def get_position(self):
        """
        Returns the current position of the ball.
        """
        return self.position

    def reverse_velocity_x(self):
        """
        Reverses the ball's horizontal velocity.
        """
        self.velocity = (-self.velocity[0], self.velocity[1])

    def reverse_velocity_y(self):
        """
        Reverses the ball's vertical velocity.
        """
        self.velocity = (self.velocity[0], -self.velocity[1])
