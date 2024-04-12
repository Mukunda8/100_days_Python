print("Welcome to the tresure island!!")
LR = input("Choose left or right")
lr = LR.lower()
if lr == "right":
    print("Game over!")
elif lr == "left":
    SW = input("Swim or wait")
    sw = SW.lower()
    if sw == "swim":
        print("Game over!")
    elif sw == "wait":
        DOOR = input("Which door? Red, Blue,Yellow?")
        door = DOOR.lower()
        if door == "red":
            print("Game over!")
        elif door == "blue":
            print("Game Over!")
        elif door == "yellow":
            print("You WIN")