class Player:
    """Represents the controlled character and can pick up items
    """

    def __init__(self):
        """Creates an instance of the player class and applies a list to it as an attribute to store items in
        """
        self.backpack = []

    def appendItem(self, item):
        """Allows an item to be added to the backpack of the player instance

        :param item: the word key
        :type item: string
        """
        self.backpack.append(item)
