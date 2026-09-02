import random

class RandomizedSet:

    def __init__(self):
        self.vals = []            # list for O(1) random access
        self.val_to_idx = {}      # value -> index in self.vals

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        idx = self.val_to_idx[val]
        last_val = self.vals[-1]

        # Move the last element into the removed element's slot
        self.vals[idx] = last_val
        self.val_to_idx[last_val] = idx

        # Remove the now-duplicated last element
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)