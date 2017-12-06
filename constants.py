""" All sizes in pixels and speeds in pixels per second """
FPS = 60

# Screen size
HEIGHT = 600
WIDTH = 1200

# Paddle
PADDLESIZE = 40
PADDLESPEED = 400
PADDLEMASS = 2000

# Paddle 1 start position.
PADDLE1X = 20
PADDLE1Y = HEIGHT / 2

# Paddle 2 start position.
PADDLE2X = WIDTH - 20
PADDLE2Y = HEIGHT / 2

# Puck
PUCKSIZE = 30
PUCKSPEED = 450
PUCKMASS = 500

# Goal Position
GOALWIDTH = 180
GOALY1 = HEIGHT / 2 - GOALWIDTH / 2
GOALY2 = HEIGHT / 2 + GOALWIDTH / 2

# Speed levels
EASY = 450
MEDIUM = 650
HARD = 850

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTRED = (255, 82, 82)

# Scoring
SCORELIMIT = 5
ROUNDLIMIT = 2

# Environment
FRICTION = 0.998
MAXSPEED = 1500

# Pause
pause_flag = False
