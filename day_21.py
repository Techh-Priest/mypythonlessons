        # Class Inheritance and Slicing
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal): # This line of code allow for inheritance
    def __init__(self):
        super().__init__()  # This line of code allow for inheritance

    def swim(self):
        print("Moving in water")

    def breathe(self):
        super().breathe()
        print("Doing this under water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
