"""
Bubble Sort
"""

class BubbleSort(object):
    def __init__(self, arr):
        self.lst = arr

    def sort(self):
        l = len(self.lst)
        for i in range(l):
            for j in range(0,l-i-1):
                # l-i-1 -> i elements would already sorted after iteration
                if self.lst[j] > self.lst[j+1]:
                    # swap
                    self.lst[j], self.lst[j+1] = self.lst[j+1], self.lst[j]
        return

    def print_lst(self):
        print(self.lst)

if __name__ == "__main__":
    B = BubbleSort([4,5,3,2,6,1,5,3])
    B.sort()
    B.print_lst()
