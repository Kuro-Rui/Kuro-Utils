from collections import defaultdict

# For better format when debugging
class DefaultDict(defaultdict):
    def __str__(self):
        return str({key: value for key, value in self.items()})
