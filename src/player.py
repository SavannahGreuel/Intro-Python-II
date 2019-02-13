# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, inventory = []):
        self.name = name
        self.room = room
        self.inventory = inventory

    def playerInventory(self):
        inventory = []
        for item in self.inventory:
            inventory.append(item.name)

        return inventory
