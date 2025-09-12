from collections import Counter

class TopK():
    def __init__(self, list_in):
        self.list = Counter(list_in)

    def get_top_k(self, k_in):
        return self.list.most_common(k_in)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    tpK = TopK(nums)
    print(tpK.get_top_k(k))