""" All sizes in pixels and speeds in pixels per second """
FPS = 60

# Screen size
HEIGHT = 600
WIDTH = 1200

# Paddle
PADDLE_SIZE = 40
PADDLE_SPEED = 400
PADDLE_MASS = 2000

# Paddle 1 start position.
PADDLE1X = 20
PADDLE1Y = HEIGHT / 2

# Paddle 2 start position.
PADDLE2X = WIDTH - 20
PADDLE2Y = HEIGHT / 2

# Puck
PUCK_SIZE = 30
PUCK_SPEED = 450
PUCK_MASS = 500

# Goal Position
GOAL_WIDTH = 180
GOAL_Y1 = HEIGHT / 2 - GOAL_WIDTH / 2
GOAL_Y2 = HEIGHT / 2 + GOAL_WIDTH / 2

# Speed levels
EASY = 450
MEDIUM = 650
HARD = 850

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Scoring
SCORE_LIMIT = 5
ROUND_LIMIT = 2

# Environment
FRICTION = 0.998
MAX_SPEED = 1500

# mute button
MUTE_BUTTON_RADIUS = 32

# pause button
PAUSE_BUTTON_RADIUS = 32

# info button
INFO_BUTTON_RADIUS = 32
