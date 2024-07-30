class RandomizedSet:
    def __init__(self):
        self.hash = {}
        self.values = []
    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.hash[val] = len(self.values)
        self.values.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        right = self.values[-1]
        valIdx = self.hash[val]
        self.values[valIdx] = right
        self.hash[right] = valIdx
        self.values.pop()
        del self.hash[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()