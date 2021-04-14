X = int(input("Enter the value of X-axis: "))
Y = int(input("Enter the value of Y-axis: "))

if X == 0 and Y == 0:
    print(f"(0, 0) is the origin")
elif X > 0 and Y == 0:
    x = X
    print(f"({x}, 0) is on the X-axis")
elif X == 0 and Y < 0:
    y = Y
    print(f"(0, {y}) is on the Y-axis")
elif X < 0 and Y > 0:
    x = X
    y = Y
    print(f"({x}, {y}) is in the Second Quadrant")
elif X > 0 and Y < 0:
    x = X
    y = Y
    print(f"({x}, {y}) is in the Fourth Quadrant")