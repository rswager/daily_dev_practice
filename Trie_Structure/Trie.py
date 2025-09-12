class Node():
    def __init__(self, value_in):
        self.value = value_in       # Value of the node
        self.children = {}            # Pointer to the children node(s)
        self.parent = None            # Pointer to the parent node
        self.is_end = False

class Trie():
    def __init__(self):
        self.tree = {}

    def insert(self, string_in):
        # If we don't have a place for the first character let's make it
        if string_in[0] not in self.tree:
            self.tree[string_in[0]] = Node(string_in[0])
        start_node = self.tree[string_in[0]]
        for index, char in enumerate(string_in):
            if index > 0:
                # if the char is in the children then we change
                if char not in start_node.children:
                    # add the children char
                    start_node.children[char] = Node(char)
                    # set the parent value to the cur char
                    start_node.children[char].parent = start_node
                # Move to next node
                start_node = start_node.children[char]
        # since we are at the end we can set IS_END to true
        start_node.is_end = True

    def search(self, string_in):
        # If the lead char isn't found then we quit
        if string_in[0] not in self.tree:
            return False
        start_node = self.tree[string_in[0]]
        for index, char in enumerate(string_in):
            if index > 0:
                # check the for the next char
                if char not in start_node.children.keys():
                    return False
                start_node = start_node.children[char]

        # we should be at the end of the word now
        return start_node.is_end

    def delete(self, string_in):
        if string_in[0] not in self.tree.keys():
            return
        start_node = self.tree[string_in[0]]
        # We want to iterate to the end of the word
        for index, char in enumerate(string_in):
            if index > 0:
                start_node = start_node.children[char]
        start_node.is_end = False
        # While we have a parent node
        while (start_node.parent):
            remove_child = start_node.value
            # Move to parent
            start_node = start_node.parent
            # Check if we have children and are the end of a word
            if not start_node.children[remove_child].children and not start_node.children[remove_child].is_end:
                del start_node.children[remove_child]
            else:
                break

        # If we get back to the root and it has no children we delete it
        if not start_node.children:
            del self.tree[start_node.value]


if __name__ == '__main__':
    trie = Trie()
    trie.insert("cat")
    trie.insert("cap")
    trie.insert("can")

    print(trie.search("cat"))  # True
    print(trie.search("car"))  # False

    trie.delete("cat")

    print(trie.search("cat"))  # False
    print(trie.search("cap"))  # True
