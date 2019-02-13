class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

#      * Hint: the name should be one word for ease in parsing later.
    def __repr__(self):
        return str(self.name)     