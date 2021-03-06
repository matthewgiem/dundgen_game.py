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

def draw_map(player):
    print(" _"*5)
    line = []
    for cell in CELLS:
        x, y = cell
        if x < 4:
            if cell == player:
                line.append("|X")
            else:
                line.append("|_")
        else:
            if cell == player:
                line.append("|X|")
            else:
                line.append("|_|")
        if x == 4:
            print("".join(line))
            line = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x = player[0]
    y = player[1]
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1
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
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    return moves

dragon, player, door = get_locations()
wrong_move = 0

while True:
    print("Welcome to the Dundgen")
    print("You're currently in room {}".format(player))  #fill with player room
    print("You can move {}".format(", ".join(get_moves(player))))  #fill with available moves
    print("You can QUIT to quit")
    if wrong_move == 1:
        print("you cant move there!")
    if wrong_move == 2:
        print("that move isn't an option")
    draw_map(player)
    move = raw_input("> ")
    move = move.upper()

    if move == "QUIT":
        break
    if move in get_moves(player):
        wrong_move = 0
        player = move_player(player, move)
        if player == door:
            print("congradulations you fond the door and won!!")
            break
        if player == dragon:
            print("I'm sorry you ran in to the dragon!! you lost")
            break
        clear_screen()
    elif move in ["RIGHT", "LEFT", "DOWN", "UP"]:
        clear_screen()
        wrong_move = 1
    else:
        clear_screen()
        wrong_move = 2

    #good move => change player position
    #bad move => alert player and don't change position
    #on the door, player wins
    #on the dragon, player loses
