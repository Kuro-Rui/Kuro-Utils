import collections

# For better format when debugging
class defaultdict(collections.defaultdict):
    def __str__(self):
        return str({key: item for key, item in self.items()})
