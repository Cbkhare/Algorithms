"""
Selection sort
"""

class SelectionSort(object):
    def __init__(self, arr):
        self.lst = arr

    def sort(self):
        l = len(self.lst)
        for i in range(l):
            marked_index = i
            for j in range(i+1, l):
                # find number less than self.lst[i]
                marked_index = j if self.lst[j] < self.lst[i] else marked_index
            # swap
            self.lst[i], self.lst[marked_index] = self.lst[marked_index], self.lst[i]
        return

    def print_lst(self):
        print(self.lst)


if __name__ == "__main__":
    S = SelectionSort([4,3,5,6,3,1,2,3])
    S.sort()
    S.print_lst()
