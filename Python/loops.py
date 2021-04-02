one_answer_1 = "left"
one_answer_2 = "right"
two_one_answer_1 = "take it"
two_one_answer_2 = "leave it"
two_two_answer_1 = "fight"
two_two_answer_2 = "flee"
a = "left"
b = "right"
d = "red"
e = "blue"
g = "up"
h = "down"
k = "gold"
l = "plain"
m = "rusty"

print("Journey")
print("You have begun your quest to the magic scythe.")
print("NOTE: ALL ANSWERS ARE LOWERCASE AND NO PUNCTUATION.")
print("On your way, you find a fork in the path.")

one = input("Should you go left or right?")
if one == one_answer_1:
    print("You go to the left path.")
    print("On the path, you find an iron sword.")
    two_one = input("Take it or leave it?")
    if two_one == two_one_answer_1:
        print("You take the sword.")
        print("Good idea!")
        print("On your way, you meet a giant fire-breathing venus flytrap.")
        print("You take it down with your sword and resume your journey.")
        print("After about 30 minutes of walking, you spot another fork.")
        three_one = input("Left or right?")
        if three_one == b:
            print("You go right.")
            print("Cool!")
            print("""On the path, you saw a sign that said: 'This path is safe.'""")
            print("That was true.")
            print("You keep walking.")
            print("As you walk you suddenly through some bushes spot the castle where the scythe lies.")
            print("Awesome! You move on.")
            print("Inside, there are two stairways. One leads up and the other leads down.")
            i = input("Up or down?")
            if i == g:
                print("You go up the stairs.")
                print("At the top lies a chest. Yessss!")
                print("But then you realize: You don't have the key!")
                print("Just then, three keys fall in front of you.")
                print("One is gold, another is plain, and the last one is rusty.")
                print("Then you see a sign.")
                print("""It says, "One of these keys unlocks the door. The second doesn't do anything. The last
one is a trap. Plus, when you pick the one that doesn't do anything, all the keys disappear." """)
                j = input("Should you pick the gold key, the plain key, or the rusty key?")
                if j == k:
                    print("You picked the gold key.")
                    print("It didn't do anything.")
                    print("Maybe you should use that as an april fool prank to someone!")
                elif j == l:
                    print("You picked the plain key.")
                    print("It's the key to the chest.")
                    print("Congratulations! You open it and find the scythe inside. And a note.")
                    print("It says the following:")
                    print(""" "WOW. Just WOW. You completed the quest to the magical scythe! It can slice through metal
and when you strike it on the ground, as much and whatever food you want appears right in front
of you! But don't put it back. You've earned it.""")
                    print("Man, you're lucky! You got the scythe.")
                    print("If you want to ply again, you'll have to restart this program again.")
                    print("Sorry, but if I continue to type like this, my fingers are going to be some black stubs.")
                    print("Bye!")
                elif j == m:
                    print("You pick the rusty key.")
                    print("That was the trap key!")
                    print("A trapdoor suddenly opens below you.")
                    print("You fall into a pit on snakes.")
                    print("The end!")
                else:
                    print("You have typed invalid syntax. Please try the project again.")
            elif i == h:
                print("You go down the stairs.")
                print("When you reach the last step, the doors behind and in front of you close locked shut.")
                print("Then the area you're in starts to flood.")
                print("You lose!")
            else:
                print("You have typed invalid syntax. Please try the project again.")
        elif three_one == a:
            print("You go left.")
            print("Sadly, on your way, you fall down an endless pit.")
            print("Wrong choice!")
        else:
            print("You have typed invalid syntax. Please try the project again.")
    elif two_one == two_one_answer_2:
        print("You leave the sword.")
        print("Wrong!")
        print("You meet a giant fire-breathing venus flytrap.")
        print("Long story short, it incinerates you into ashes.")
        print("Heh, heh.")
    else:
        print("You have typed invalvid syntax. Please try the project again.")
elif one == one_answer_2:
    print("You go to the right path.")
    print("When you go for a short time, a panther suddenly jumps in front of you!")
    two_two = input("Fight or flee?")
    if two_two == two_two_answer_1:
        print("You decide to fight the monster.")
        print("It actually works!")
        print("You try to make yourself look scary, frightening the panther and making it run away.")
        print("You continue on.")
        print("After a few minutes, you see two portals; red and blue.")
        c = input("Where should you go?")
        if c == d:
            print("You go through the red portal.")
            print("At the other end,the castle where the scythe is kept awaits you.")
            print("Great! You go in.")
            print("Inside, there are two stairways. One leads up and the other leads down.")
            f = input("Up or down?")
            if f == g:
                print("You go up the stairs.")
                print("At the top lies a chest. Yessss!")
                print("But then you realize: You don't have the key!")
                print("Just then, three keys fall in front of you.")
                print("One is gold, another is plain, and the last one is rusty.")
                print("Then you see a sign.")
                print("""It says, "One of these keys unlocks the door. The second doesn't do anything. The last
one is a trap. Plus, when you pick the one that doesn't do anything, all the keys disappear." """)
                j = input("Should you pick the gold key, the plain key, or the rusty key?")
                if j == k:
                    print("You picked the gold key.")
                    print("It didn't do anything.")
                    print("Maybe you should use that as an april fool prank to someone!")
                elif j == l:
                    print("You picked the plain key.")
                    print("It's the key to the chest.")
                    print("Congratulations! You open it and find the scythe inside. And a note.")
                    print("It says the following:")
                    print(""" "WOW. Just WOW. You completed the quest to the magical scythe! It can slice through metal
and when you strike it on the ground, as much and whatever food you want appears right in front
of you! But don't put it back. You've earned it.""")
                    print("Man, you're lucky! You got the scythe.")
                    print("If you want to play again, you'll have to restart this program again.")
                    print("Sorry, but if I continue to type like this, my fingers are going to be some black stubs.")
                    print("Bye!")
                elif j == m:
                    print("You pick the rusty key.")
                    print("That was the trap key!")
                    print("A trapdoor suddenly opens below you.")
                    print("You fall into a pit on snakes.")
                    print("The end!")
                else:
                    print("You have typed invalid syntax. Please try the project again.")
            elif f == h:
                print("You go down the stairs.")
                print("When you reach the last step, the doors behind and in front of you close locked shut.")
                print("Then the area you're in starts to flood.")
                print("You lose!")
            else:
                print("You have typed invalid syntax. Please try the project again.")
        elif c == e:
            print("You go through the blue portal.")
            print("The portal leads you to a dark room with many venomous spiders.")
            print("You can guess what happened next.")
        else:
            print("You have typed invalid syntax. Please try the project again.")
    elif two_two == two_two_answer_2:
        print("You decide to flee.")
        print("Bad choice! When you start to run down the path, the panther jumps on and bites you.")
        print("Plus, the panther's jaws are huge.")
        print("Better luck next time!")
    else:
        print("You have typed invalvid syntax. Please try the project again.")
else:
    print("You have typed invalid syntax. Please try the project again.")







    
