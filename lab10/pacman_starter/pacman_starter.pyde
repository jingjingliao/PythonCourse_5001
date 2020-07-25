WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0

START_ANGLE = 45
END_ANGLE = 315

START_ANGLE_OF_DOWN_DIRECTION = 140
END_ANGLE_OF_DOWN_DIRECTION = 405

START_ANGLE_OF_UP_DIRECTION = 315
END_ANGLE_OF_UP_DIRECTION = 585

START_ANGLE_OF_LEFT_DIRECTION = 225
END_ANGLE_OF_LEFT_DIRECTION = 495

START_ANGLE_OF_RIGHT_DIRECTION = 45
END_ANGLE_OF_RIGHT_DIRECTION = 315

ADJUST_ANGLE = 1

OPEN_ANGLE_LIST = [45, 140, 225, 315]
CLOSE_ANGLE_LIST = [0, 95, 180, 270]

status = True

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y  # Must be declared as global
    background(0)

    x = x + x_add
    y = y + y_add
    
    # The following cases deal with when PacMan
    # is near the edge of the screen
    
    # If PacMan moves completely behond the right edge 
    if (x > WIDTH + (PACMAN_WIDTH/2)): 
        # Reset the x value to the left side
        x = PACMAN_WIDTH/2
    # If PacMan is overlapping the right edge
    elif (x > WIDTH - (PACMAN_WIDTH/2)):
        # draw a second PacMan on the left side, also
        # overlapping
        pacman(x - WIDTH, y)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT)
    
    # Always draw PacMan at his real current location.
    pacman(x, y)

def pacman(x, y):
    """Draw PacMan to the screen"""
    # Use global variables as necessary
    global START_ANGLE, END_ANGLE
    global status
    global ADJUST_ANGLE
    arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
        radians(START_ANGLE), 
        radians(END_ANGLE))

    if START_ANGLE in CLOSE_ANGLE_LIST:
        status = False
    elif START_ANGLE in OPEN_ANGLE_LIST:
        status = True
        
    if status == True:
        START_ANGLE = START_ANGLE - ADJUST_ANGLE
        END_ANGLE = END_ANGLE + ADJUST_ANGLE
    else:
        START_ANGLE = START_ANGLE + ADJUST_ANGLE
        END_ANGLE = END_ANGLE - ADJUST_ANGLE
    
def keyPressed():
    global x_add, y_add  # Must be declared as global
    global START_ANGLE, END_ANGLE
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
            START_ANGLE = START_ANGLE_OF_DOWN_DIRECTION
            END_ANGLE = END_ANGLE_OF_DOWN_DIRECTION
            
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
            START_ANGLE = START_ANGLE_OF_UP_DIRECTION
            END_ANGLE = END_ANGLE_OF_UP_DIRECTION
            
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
            START_ANGLE = START_ANGLE_OF_LEFT_DIRECTION
            END_ANGLE = END_ANGLE_OF_LEFT_DIRECTION
            
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
            START_ANGLE = START_ANGLE_OF_RIGHT_DIRECTION
            END_ANGLE = END_ANGLE_OF_RIGHT_DIRECTION
