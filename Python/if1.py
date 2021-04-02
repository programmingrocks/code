correct = "The people were married."
number = True

while number:
    n = str(input("""You see many people on a boat which
never sinks, but when you look again,
there isn't a single person on the boat.
How is that?"""))
    if n == correct:
        print("Correct!")
        break
        number = False
    elif n != correct:
        print("WrOnG")
        number = True
