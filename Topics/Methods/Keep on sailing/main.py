# our class Ship
class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = destination

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {} has sailed for {}!".format(self.name, self.destination)


dest = input()
black_pearl = Ship("Black Pearl", 800, dest)
print(black_pearl.sail())
