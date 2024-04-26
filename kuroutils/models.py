from collections import defaultdict

# For better format when debugging
class DefaultDict(defaultdict):
    def __repr__(self):
        return {key: value for key, value in self.items()}

    def __str__(self):
        return str(self.__repr__())
