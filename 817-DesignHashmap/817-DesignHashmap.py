# Last updated: 15/9/2026, 11:35:34 pm
class MyHashMap:
    def __init__(self):
        # Initialize with a fixed number of buckets
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        # Use modulo as a simple hash function
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """Inserts a (key, value) pair. Updates value if key exists."""
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))

    def get(self, key: int) -> int:
        """Returns the value for the key, or -1 if not found."""
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """Removes the key and its value if it exists."""
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h].pop(i)
                return
