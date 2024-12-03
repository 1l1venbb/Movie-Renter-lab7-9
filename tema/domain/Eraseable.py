class Erase:
    def __init__(self, isDeleted):
        self.isDeleted = isDeleted

    def isErased(self):
        """
        Returns True if object is marked as deleted
        :return: bool
        """
        return self.isDeleted

    def delete(self):
        """
        Marks object as deleted
        :return:
        """
        self.isDeleted = True