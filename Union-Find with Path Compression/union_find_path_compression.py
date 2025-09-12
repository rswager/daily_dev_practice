class UnionFind():
    def __init__(self, size_in):
        self.parent = list(range(size_in))

    def union(self, union_a, union_b):
        # Get the head of root_a
        root_a = self.find(union_a)
        # Get the head of root_b
        root_b = self.find(union_b)

        # If they are the same head then it is already a part of the graph
        if root_a != root_b:
            self.parent[root_b] = root_a

    def find(self, child):
        # If the parent is the child then we are at the head
        if self.parent[child] != child:
            # We will update the parent until any child in the graph will be pointing at the root.
            self.parent[child] = self.find(self.parent[child])
        return self.parent[child]

    def print_parent(self):
        for index, value in enumerate(self.parent):
            print(index, "-", value, end=', ')
        print()


if __name__ == '__main__':
    uf = UnionFind(10)
    # Make a graph with a Head of 9
    uf.union(9, 0)
    uf.union(9, 4)
    uf.union(9, 5)
    uf.union(9, 6)
    uf.union(6, 7)
    uf.union(6, 8)

    # Make a graph with a Head of 3
    uf.union(3, 1)
    uf.union(3, 2)
    uf.print_parent()

    # Is a component of Graph 9 a part of Graph 3 (NO)
    print("Are 1 and 4 in the same set:\n\tfind(1) = ", uf.find(1), "\n\tfind(4) = ", uf.find(4), "\n\tJudment: ", uf.find(1) == uf.find(4))
    # Union Graph 3 to Graph 9
    uf.union(9, 3)
    uf.print_parent()
    # Is a component of Graph 9 a part of Graph 3 (YES)
    print("Are 1 and 4 in the same set:\n\tfind(1) = ", uf.find(1), "\n\tfind(4) = ", uf.find(4), "\n\tJudment: ", uf.find(1) == uf.find(4))


