# define the class
class Circle(object):

    # Constructor
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

# creating an object instance of the Class
RedCircle = Circle(10, "red")

# getting the attribue of the object instance
print(RedCircle.radius)

# changing the radius
RedCircle.add_radius(2)

# getting the attribue of the object instance
print(RedCircle.radius)

# listing out all data attributes/ mohods
for attribute in dir(RedCircle):
    print(attribute)