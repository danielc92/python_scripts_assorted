class Clothing():
    '''
    clothing class defines a piece of clothing in terms
    of its name and its cleanliness
    '''

    #CONSTRUCTOR
    def __init__(self, name: object, colour: object, clean: object = True, times_worn: object = 0, max_wears: object = 1) -> object:
        self.name = name
        self.colour = colour
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears

    #GETTER METHODS
    def getName(self):
        return self.name

    def getColour(self):
        return self.colour

    def getClean(self):
        return self.clean

    def getTimesWorn(self):
        return self.times_worn

    def getMaxWears(self):
        return self.max_wears

    #SETTER METHODS
    def setName(self, new_name):
        self.name = new_name

    def setColour(self, new_colour):
        self.colour = new_colour

    def setClean(self, new_clean):
        self.clean = new_clean

    def wear(self):
        self.times_worn = self.times_worn + 1
        if self.times_worn >= self.max_wears:
            self.clean = False

    def wash(self):
        self.times_worn = 0
        self.clean = True

def main():
    hat = Clothing("daniels hat", "blue", True, 2, 5)
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())
    hat.wear()
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())
    hat.wear()
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())
    hat.wear()
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())
    hat.wear()
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())
    hat.wash()
    print(hat.getClean())
    print(hat.getTimesWorn())
    print(hat.getMaxWears())

main()