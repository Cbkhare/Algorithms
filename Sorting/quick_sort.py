"""
Quick sort
"""

class QuickSort(object):

    def __init__(self, arr):
        self.lst = arr

    def quick_sort(self, A):
        n = len(A)
        if n==0:
            return []
        pivot = A[n-1]  # last elements as the pivot
        # all elements less than pivot
        lss_elements = [A[j] for j in range(n) if A[j] < pivot]
        # all elements equal to pivot
        eq_elements = [A[j] for j in range(n) if A[j] == pivot]
        # all elements greater than pivot
        gtr_elements = [A[j] for j in range(n) if A[j] > pivot]
        # performing quick sort
        lss_elements = self.quick_sort(lss_elements)
        gtr_elements = self.quick_sort(gtr_elements)
        # combine result
        return lss_elements + eq_elements + gtr_elements

    def sort(self):
        self.lst = self.quick_sort(self.lst)
        return

    def print_list(self):
        print(self.lst)


if __name__ == "__main__":
    Q = QuickSort([4,3,5,2,1,2,4])
    Q.sort()
    Q.print_list()
