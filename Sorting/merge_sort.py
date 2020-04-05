"""
Merge sort
"""

class MergeSort(object):

    def __init__(self, arr):
        self.lst = arr

    def sort_in_merge(self, i, n):
        if i == n:
            return
        elif i == n:
            if self.lst[i] > self.lst[n]:
                self.lst[i], self.lst[n] = self.lst[n], self.lst[i]
            return
        else:
            mid = i + (n-i)//2
            self.sort_in_merge(i, mid)
            self.sort_in_merge(mid+1, n)
            l1 = self.lst[i:mid+1]
            l2 = self.lst[mid+1:n+1]
            l1i = l2i = 0
            j = i
            # merge l1 and l2 at self.lst[i:n+1]
            # [0,4] [1,5] -- > [0,1,4,5]
            while l1i < len(l1) and l2i < len(l2):
                if l1[l1i] <= l2[l2i]:
                    self.lst[j] = l1[l1i]
                    l1i += 1
                else:
                    self.lst[j] = l2[l2i]
                    l2i += 1
                j += 1
            # any pending values
            while l1i < len(l1):
                self.lst[j] = l1[l1i]
                l1i += 1
                j += 1

            while l2i < len(l2):
                self.lst[j] = l2[l2i]
                l2i += 1
                j += 1
            return

    def sort(self):
        # sorting in place
        l = len(self.lst)
        self.sort_in_merge(0, l-1)
        return

    def print_list(self):
        print(self.lst)

if __name__ == "__main__":
    M = MergeSort([4, 3, 2, 1, 5, 4])
    M.sort()
    M.print_list()
