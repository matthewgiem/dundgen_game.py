import random
import os

#draw the grid
#pic random location for player
#pic random location for exit
#pic random location for dragon
#draw player in grid
#input for movement
#move player unless invalid movement
#check for win or loss
#clear the screen and redraw the grid

CELLS = [
        (0,0), (1,0), (2,0), (3,0), (4,0),
        (0,1), (1,1), (2,1), (3,1), (4,1),
        (0,2), (1,2), (2,2), (3,2), (4,2),
        (0,3), (1,3), (2,3), (3,3), (4,3),
        (0,4), (1,4), (2,4), (3,4), (4,4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x = player[0]
    y = player[1]
    if move == "UP":
        y += 1
    if move == "DOWN":
        y -= 1
    if move == "RIGHT":
        x += 1
    if move == "LEFT":
        x -= 1
    player = (x, y)
    return player

def get_moves(player):
    moves = ["RIGHT", "LEFT", "DOWN", "UP"]
    x = player[0]
    y = player[1]
    if y == 0:
        moves.pop()
    if y == 4:
        moves.pop(2)
    if x == 0:
        moves.pop(1)
    if x == 4:
        moves.pop(0)
    return moves

dragon, player, door = get_locations()

while True:
    print("Welcome to the Dundgen")
    print("You're currently in room {}".format(player))  #fill with player room
    print("You can move {}".format(", ".join(get_moves(player))))  #fill with available moves
    print("You can QUIT to quit")

    move = raw_input("> ")
    move = move.upper()

    if move == "QUIT":
        break

    player = move_player(player, move)

    #good move => change player position
    #bad move => alert player and don't change position
    #on the door, player wins
    #on the dragon, player loses
