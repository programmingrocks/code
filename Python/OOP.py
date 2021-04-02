# Making Parent-Children classes
class animals:
    pass

class vertebrates(animals):
    pass

class Deer(vertebrates):
    def left_forward(self):
        print("left foot forward")
    def right_forward(self):
        print("right foot forward")
    def left_backward(self):
        print("left foot backward")
    def right_backward(self):
        print("right foot backward")
    def dab(self):
        print("dabbing")
        
    def dance_one(self):
        self.left_forward()
        self.right_forward()
        self.right_backward()
        self.dab()
        self.left_backward()
        
    def dance_two(self):
        self.right_forward()
        self.dab()
        self.right_backward()
        self.left_forward()
        self.dab()
        self.left_backward()

    def dance_three(self):
        self.dab()
        self.right_forward()
        self.left_forward()
        self.dab()
        self.right_backward()
        self.left_backward()
        self.dab()

    def dance_four(self):
        self.dab()
        self.dab()
        self.dab()
        self.left_forward()
        self.right_forward()

    def dance_five(self):
        self.left_forward()
        self.right_backward()
        self.dab()
        self.left_backward()
        
    
barry = Deer()
sydney = Deer()
kenny = Deer()

a = input("Would you like to see deer Barry, Sydney, or Kenny's moves?")

if a == """Barry's moves""":
    print("Barry's moves:")
    barry.dance_two()
    barry.dance_three()
    barry.dance_five()
    barry.dance_one()
    barry.dance_four()

elif a == """Sydney's moves""":
    print("Sydney's moves:")
    sydney.dance_one()
    sydney.dance_five()
    sydney.dance_four()
    sydney.dance_three()
    sydney.dance_two()

elif a == """Kenny's moves""":
    print("Kenny's moves:")
    kenny.dance_five()
    kenny.dance_one()
    kenny.dance_four()
    kenny.dance_two()
    kenny.dance_three()





















        
