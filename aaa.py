import sys
import pygame

# Pygame Initialization
pygame.init()

# Set up some constants
WIDTH, HEIGHT, SIDE = 600, 600, 600/3
RADIUS = int(SIDE/2 - 10)
LINE_WIDTH = 15
FONT_SIZE = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font object for drawing text
font = pygame.font.SysFont(None, FONT_SIZE)

# Board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Drawing the board
def draw_board():
    for i in range(3):
        pygame.draw.line(screen, BLACK, (0, i*SIDE), (WIDTH, i*SIDE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i*SIDE, 0), (i*SIDE, HEIGHT), LINE_WIDTH)

    for i, line in enumerate(board):
        for j, cell in enumerate(line):
            if cell is not None:
                draw_cell(j, i, cell)

# Drawing a single cell
def draw_cell(x, y, player):
    if player == 'X':
        color = RED
    elif player == 'O':
        color = BLUE

    x_center, y_center = int(x*SIDE + SIDE/2), int(y*SIDE + SIDE/2)
    pygame.draw.circle(screen, color, (x_center, y_center), RADIUS, LINE_WIDTH)
    text = font.render(player, True, WHITE)
    screen.blit(text, (x_center - text.get_width()/2, y_center - text.get_height()/2))

# Checking if a player has won
def check_win(player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True

    i = 0
    j = 1
    if board[i][i] == player and board[i+1][i+1] == player and all([cell is not None for cell in board[i:i+2]]):
        return True

    if board[i][2-i] == player and board[i+1][3-i] == player and all([cell is not None for cell in board[i:i+2]]):
        return True

    return False

# Main game loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
draw_board()

player = 'X'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not check_win(player):
            x, y = pygame.mouse.get_pos()
            x, y = x//SIDE, y//SIDE
            if board[y][x] is None:
                board[y][x] = player
                player = 'O' if player == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    if check_win(player):
        text = font.render(f"Winner: {player}", True, WHITE)
        screen.blit(text, (35, HEIGHT/2-text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(100)