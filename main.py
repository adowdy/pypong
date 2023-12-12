from game_objects import Paddle, Ball
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, BALL_SIZE, PADDLE_SPEED, BALL_VELOCITY

# Key bindings for player movement
PLAYER_2_UP = "Up"
PLAYER_2_DOWN = "Down"
PLAYER_1_UP = "w"
PLAYER_1_DOWN = "s"

class PongGame:
    def __init__(self):
        self.win = turtle.Screen()
        self.win.title("PyPong")
        self.win.bgcolor("black")
        self.win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.win.tracer(0)

        # Initialize paddles
        self.paddle_a = Paddle(-SCREEN_WIDTH/2 + PADDLE_WIDTH, 0, PADDLE_SPEED, PLAYER_1_UP, PLAYER_1_DOWN)
        self.paddle_b = Paddle(SCREEN_WIDTH/2 - PADDLE_WIDTH, 0, PADDLE_SPEED, PLAYER_2_UP, PLAYER_2_DOWN)

        # Initialize ball
        self.ball = Ball(0, 0, BALL_VELOCITY)

        # Keyboard bindings
        self.win.listen()
        self.win.onkeypress(self.paddle_a.move_up, PLAYER_1_UP)
        self.win.onkeypress(self.paddle_a.move_down, PLAYER_1_DOWN)
        self.win.onkeypress(self.paddle_b.move_up, PLAYER_2_UP)
        self.win.onkeypress(self.paddle_b.move_down, PLAYER_2_DOWN)

    def run(self):
        while True:
            self.win.update()
            self.ball.move()

            # Ball collision with paddles
            if self.ball.xcor() > SCREEN_WIDTH/2 - PADDLE_WIDTH and self.ball.xcor() < SCREEN_WIDTH/2:
                if self.ball.ycor() < self.paddle_b.ycor() + PADDLE_HEIGHT/2 and self.ball.ycor() > self.paddle_b.ycor() - PADDLE_HEIGHT/2:
                    self.ball.bounce_x()

            if self.ball.xcor() < -SCREEN_WIDTH/2 + PADDLE_WIDTH and self.ball.xcor() > -SCREEN_WIDTH/2:
                if self.ball.ycor() < self.paddle_a.ycor() + PADDLE_HEIGHT/2 and self.ball.ycor() > self.paddle_a.ycor() - PADDLE_HEIGHT/2:
                    self.ball.bounce_x()

            # Ball collision with walls
            if self.ball.ycor() > SCREEN_HEIGHT/2 - BALL_SIZE/2 or self.ball.ycor() < -SCREEN_HEIGHT/2 + BALL_SIZE/2:
                self.ball.bounce_y()

def main():
    game = PongGame()
    game.run()

if __name__ == "__main__":
    main()
