from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=2):
        # Set the maximum number of items the cache can hold
        self.capacity = capacity
        # Use an OrderedDict to maintain the order of insertion/access
        self.cache = OrderedDict()  # key -> value

    def get(self, key):
        # Return -1 if the key is not in the cache
        if key not in self.cache:
            return -1

        # Retrieve the value and mark the item as recently used
        value = self.cache[key]
        # Move the accessed key to the front (most recently used)
        self.cache.move_to_end(key, last=False)
        return value

    def put(self, key, value):
        if key in self.cache:
            # If key exists, update the value
            self.cache[key] = value
            # Move the key to the front (most recently used)
            self.cache.move_to_end(key, last=False)
        else:
            # If the cache is at capacity, remove the least recently used item
            if len(self.cache) >= self.capacity:
                # Pop the last item (least recently used)
                self.cache.popitem(last=True)

            # Insert the new key-value pair
            self.cache[key] = value
            # Move it to the front (most recently used)
            self.cache.move_to_end(key, last=False)

    def print(self):
        # Print the cache in order from most to least recently used
        for key, value in self.cache.items():
            print(f"{key}: {value}", end=" <-> ")
        print("None")

# Demo
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 34)        # Cache: 1
    cache.print()
    cache.put(2, 90)        # Cache: 2 <-> 1
    cache.print()
    cache.put(3, 100)       # Cache: 3 <-> 2 (evicts 1)
    cache.print()
    print(cache.get(2))     # Access 2 → Cache: 2 <-> 3
    cache.put(2, 50)        # Update 2's value → Cache: 2 <-> 3
    cache.print()
    print(cache.get(2))     # Should return 50