import datetime
import random

grid_length = 100
grid_width = 100

location_coordinates = []

for l in range(grid_length):
    for w in range(grid_width):
        coord = [w,l]
        location_coordinates.append(coord)

locations_count = len(location_coordinates)-1


class Player:

    def __init__(self, start_pos : object, name : object):

        self.start_pos = start_pos
        self.current_pos = start_pos
        self.name = name

        self.health = 100
        self.tagged = False
        self.alive = True

        print("Welcome to game, player",self.name,"spawned at",self.start_pos)

    def dirty_data(self):
        chance = random.randint(1,10)
        if chance == 5:
            self.tagged = True
            self.health = self.health - 5
            print("Oh no!",self.name,"has encountered some DIRTY DATA...")
            self.check_health()
        else:
            print("Seems there is nothing here...")

    def check_health(self):
        if self.health <= 0:
            print(self.name,"has perished at location",self.current_pos)
            self.alive = False
        else:
            print(self.name,"is alive, with",self.health,"points remaining.")

    def get_player_position(self):
        print(self.name,"is currently located at:",self.current_pos)

    def move_left(self, paces = 1):
        print("\nAttempting to move", self.name, "left", paces, "paces.")

        if self.alive == True:
            cloned_pos = self.current_pos
            new_pos = [cloned_pos[0] - paces, cloned_pos[1]]

            if new_pos in location_coordinates:
                self.current_pos = new_pos
                print(self.name, " successfully moved to position ", self.current_pos,".")
            else:
                print("Position is out of bounds, player cannot move there.")

            self.dirty_data()
        elif self.alive == False:
            print(self.name, "is dead and cannot be moved.")

    def move_right(self, paces = 1):
        print("\nAttempting to move", self.name, "right", paces, "paces.")
        if self.alive == True:

            cloned_pos = self.current_pos
            new_pos = [cloned_pos[0] + paces, cloned_pos[1]]

            if new_pos in location_coordinates:
                self.current_pos = new_pos
                print(self.name, " successfully moved to position ", self.current_pos,".")
            else:
                print("Position is out of bounds, player cannot move there.")
            self.dirty_data()
        elif self.alive == False:
            print(self.name, "is dead and cannot be moved.")

    def move_up(self, paces = 1):
        print("\nAttempting to move", self.name, "up", paces, "paces.")
        if self.alive == True:

            cloned_pos = self.current_pos
            new_pos = [cloned_pos[0], cloned_pos[1] + paces]

            if new_pos in location_coordinates:
                self.current_pos = new_pos
                print(self.name, " successfully moved to position ", self.current_pos,".")
            else:
                print("Position is out of bounds, player cannot move there.")
            self.dirty_data()
        elif self.alive == False:
            print(self.name, "is dead and cannot be moved.")

    def move_down(self, paces = 1):
        print("\nAttempting to move", self.name, "down", paces, "paces.")
        if self.alive == True:

            cloned_pos = self.current_pos
            new_pos = [cloned_pos[0], cloned_pos[1] - paces]

            if new_pos in location_coordinates:
                self.current_pos = new_pos
                print(self.name, " successfully moved to position ", self.current_pos,".")
            else:
                print("Position is out of bounds, player cannot move there.")
            self.dirty_data()
        elif self.alive == False:
            print(self.name, "is dead and cannot be moved.")

'''
Running Program
'''