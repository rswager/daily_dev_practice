# Node class represents each entry in the doubly linked list
class Node():
    def __init__(self, key_in, value_in):
        self.key = key_in           # Key of the node
        self.value = value_in       # Value of the node
        self.next = None            # Pointer to the next node
        self.prev = None            # Pointer to the previous node

# LRUCache using a hashmap + doubly linked list for O(1) get/put
class LRUCache():
    def __init__(self):
        self.cache_capacity = 2              # Max number of items the cache can hold
        self.cache = {}                      # Dictionary for O(1) access: key -> node
        self.head = None                     # Most recently used node
        self.tail = None                     # Least recently used node

    def get(self, key_in):
        if key_in not in self.cache:
            return -1  # Key doesn't exist

        node = self.cache[key_in]
        # Move the accessed node to the front (most recently used)
        self.__remove(node)
        self.__add_to_front(node)
        return node.value

    def put(self, key_in, value_in):
        if key_in in self.cache:
            # Key already exists; update value and move to front
            node = self.cache[key_in]
            node.value = value_in
            self.__remove(node)
            self.__add_to_front(node)
        else:
            # Key doesn't exist
            if len(self.cache) >= self.cache_capacity:
                # Cache is full; remove the least recently used (tail)
                del self.cache[self.tail.key]
                self.__remove(self.tail)

            # Add new node to cache and list
            newNode = Node(key_in, value_in)
            self.__add_to_front(newNode)
            self.cache[key_in] = newNode

    def __remove(self, node):
        # Disconnect node from its neighbors
        if node.prev:
            node.prev.next = node.next  # Link previous node to next
        else:
            self.head = node.next       # Node was head; update head

        if node.next:
            node.next.prev = node.prev  # Link next node to previous
        else:
            self.tail = node.prev       # Node was tail; update tail

    def __add_to_front(self, node):
        # Insert node at the head (most recently used)
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            # If list was empty, this node is now also the tail
            self.tail = node

    def print(self):
        # Print list from head to tail (most to least recently used)
        current = self.head
        while current:
            print(f"{current.key}: {current.value}", end=" <-> ")
            current = current.next
        print("None")

# Demo usage
if __name__ == "__main__":
    example = LRUCache()
    example.put(1, 34)        # Cache: 1
    example.print()
    example.put(2, 90)        # Cache: 2 <-> 1
    example.print()
    example.put(3, 34)        # Cache: 3 <-> 2 (evicts 1)
    example.print()
    print(example.get(2))     # Access 2 → Cache: 2 <-> 3
    example.put(2, 50)        # Update 2's value → Cache: 2 <-> 3
    example.print()
    print(example.get(2))     # Should return 50