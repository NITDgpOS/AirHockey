import constants as const

smallfont = None
score1, score2 = 0, 0

# Sound globals.
paddleHit = None
goal_whistle = None
backgroundMusic = None

# game globals.
clock = None
screen = None
screenColor = (224, 214, 141)

# width and height of the screen.
width, height = const.WIDTH, const.HEIGHT

# button constants
buttonRadius = 60
squareSide = 80

# color globals
# (dimgreen,green) , (dimred,red) , (dimblue,blue ) , (yellow,dimyellow), (orange, dimorange)
colors = [ [(46, 120, 50),(66, 152, 60)] , [(200, 72, 72),(255, 92, 92)] ,
           [(0, 158, 239),(100, 189, 219)] , [(221, 229, 2),(252, 255, 59)],
           [(232, 114, 46),(244, 133, 51)]]
