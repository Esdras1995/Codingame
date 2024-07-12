# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    move = ""
    if initial_ty<light_y:
        move = "S"
        initial_ty = initial_ty + 1
    elif initial_ty>light_y:
        move = "N"
        initial_ty = initial_ty - 1
    
    if initial_tx<light_x:
        move = move + "E"
        initial_tx = initial_tx + 1
    elif initial_tx>light_x:
        move = move + "W"
        initial_tx = initial_tx - 1
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move)