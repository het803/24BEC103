def hrs():
    for hr in range(24):
        if hr == 0:
            print("It's 12 Midnight")
        elif hr < 12:
            print(f"It is {hr} AM")
        elif hr == 12:
            print("12 Noon")
        else:
            print(f"It is {hr - 12} PM")

hrs()