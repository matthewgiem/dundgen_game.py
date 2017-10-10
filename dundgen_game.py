import random

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

def move_player(player, direction):
    # get players location
    # if move == up y + 1
    # if move == down y - 1
    # if move == right x + 1
    # if move == left x - 1
    return player

def get_moves(player):
    moves = ["RIGHT", "LEFT", "UP", "DOWN"]
    # if players y == 0 can't move up
    # if players y == 4 can't move down
    # if players x == 0 can't move left
    # if players x == 4 can't move right
    return moves

while True:
    print("Welcome to the Dundgen")
    print("You're currently in room {}")  #fill with player room
    print("You can move {}")  #fill with available moves
    print("You can QUIT to quit")

    move = raw_input("> ")
    move = move.upper()

    if move == "QUIT":
        break

    #good move => change player position
    #bad move => alert player and don't change position
    #on the door, player wins
    #on the dragon, player loses
