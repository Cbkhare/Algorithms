class SegmentTree(object):

    def __init__(self, arr):
        self.lst = arr
        self.s = [0 for _ in range(4*len(self.lst))] # segment

    def build(self, i, l, r):
        """
        Builds the segment tree
        :param i: Index of segment tree
        :param l: range start
        :param r: range end
        :return: None
        """
        if l == r:
            self.s[i] = self.lst[l]
            return
        mid = l + (r-l)//2
        self.build(i*2+1, l, mid)
        self.build(i*2+2, mid+1, r)
        self.s[i] = self.s[i*2+1] + self.s[i*2+2]
        return

    def modify(self, p, x, i, l, r):
        """
        Modify the segment tree
        :param p: position in array, modified with
        :param x: value x
        :param i: index of segment tree
        :param l: range start
        :param r: range end
        :return: None
        """
        self.s[i] += x - self.lst[p]
        if l == r:
            self.s[i] = x
            self.lst[p] = x
            return
        mid = l + (r-l)//2
        if p < mid:
            self.modify(p, x, i*2+1, l, mid)
        else:
            self.modify(p, x, i*2+2, mid+1, r)
        return

    def query(self, x, y, i, l, r):
        """
        Query the result of range
        :param x: search range start
        :param y: search range end
        :param i: index of segment
        :param l: range start
        :param r: range end
        :return: None
        """
        if x > r or l > y:
            return 0
        elif x <= l and r <= y:
            return self.s[i]
        else:
            mid = l + (r-l)//2
            return self.query(x, y, i*2+1, l, mid) + self.query(x, y, i*2+2, mid+1, r)

if __name__ == "__main__":
    S = SegmentTree([1, 2, 3, 4])
    S.build(0, 0, 3)
    print(S.s)
    S.modify(0, 4, 0, 0, 3)
    print(S.lst, S.s)
    print (S.query(0, 2, 0, 0, 3))

