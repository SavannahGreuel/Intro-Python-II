# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items = []):
        self.name= name
        self.description= description
        self.items = items


    def roomItems(self):
        items = []
        for item in self.items:
            items.append(item.name)
            
        return f"{self.name} holds {items}"