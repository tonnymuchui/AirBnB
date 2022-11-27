class Pet:
    """Representation of Flower Class"""
    def __init__(self):
        """Initializes public attributes"""
        
        self.breed = "German"
        self.color = "Black"
        self.height = 0.5

    def description(self):
        print("This is description of my pet")

joe = Pet()
print(joe.__dict__)
print(Pet.__dict__)

