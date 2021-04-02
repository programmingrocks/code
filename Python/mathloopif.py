math = True
while math:
    a = input("""Do you want a calculator or a test score grader? Type "quit" to quit.""")
    if a == "calculator":
        calculator = True
        while calculator:
            x = input("""Type in a problem to solve. Type "quit" to quit. And PLEASE make sure to type an integer.""")
            if x == "quit":
                print("Bye!")
                break
                calculator = False
            else:
                y = eval(x)
                print(f"Your output is {y}.")
                calculator = True
    elif a == "test score grader":
            test_score = True
            while test_score:
                score = input("""What is your score? Type "quit" to quit. And PLEASE make sure to type an integer, not your
grade letter. No percentages!""")
                if score == "quit":
                    print("Bye!")
                    break
                    test_score = False
                else:
                    num1 = int(range(0, 40))
                    num2 = int(range(40, 70))
                    num3 = int(range(70, 80))
                    num4 = int(range(80, 90))
                    num5 = int(range(90, 100))
                    num6 = int(range(100, 120))
                    if score == num1:
                        print("You got an F.")
                        print("What happened to you?")
                        print("Why are you trying this program and not studying?")
                        test_score = True
                    elif score == num2:
                        print("You got a D.")
                        print("You have a long way... but I believe in you!")
                        test_score = True
                    elif score == num3:
                        print("You got a C.")    
                        print("If you have homework, try doing it first.")
                        print("If you can't do it, try using the calculator feature in this program.")
                        test_score = True
                    elif score == num4:
                        print("You got a B.")
                        print("Not bad... but you can certainly do better!")
                        test_score = True
                    elif score == num5:
                        print("You got an A.")
                        print(""" "Keep up. Get better. Win." -Anonymous """)
                        test_score = True
                    elif score == num6:
                        print("You got an A+.")
                        print("Go with the flow, continue the flow, stay with the flow.")
                        test_score = True
                    else:
                        print("You have either typed an overflowing number or typed a string. Please try again.")
                        test_score = True









