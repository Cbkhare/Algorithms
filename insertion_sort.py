"""
Insertion sort
"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None


class LinkedList(object):
    def __init__(self):
        self.first = True
        self.curr = None
        self.head = None

    def insert(self, val):
        if self.first:
            self. head = self.curr = Node(val)
            self.first = False
        else:
            node = Node(val)
            self.curr.next = node
            node.previous = self.curr
            self.curr = node

        return

    def print_list(self):
        temp = self.head
        while temp:
            print (temp.val)
            temp = temp.next

        return


class InsertionSort(object):

    def __init__(self, lst):
        # head of the linked list
        self.lst = lst

    def sort_with_linked_list(self):
        l = len(self.lst)
        L = LinkedList()
        for i in range(l):
            L.insert(self.lst[i])
        temp1 = L.head
        for i in range(1,l):
            selected_node = temp1.next   # we will start from second node
            temp2 = temp1
            while temp2 and selected_node.val < temp2.val:
                selected_node.val, temp2.val = temp2.val, selected_node.val
                temp2 = temp2.previous
                selected_node = selected_node.previous
            temp1 = temp1.next
        self.lst = []
        while L.head:
            self.lst.append(L.head.val)
            L.head = L.head.next

        return

    def sort(self):
        l = len(self.lst)
        for i in range(l):
            j = i
            k = self.lst[j]
            while j-1 >= 0 and k < self.lst[j-1]:
                self.lst[j-1], self.lst[j] = self.lst[j], self.lst[j-1]
                j -= 1
        return

    def print_lst(self):
        print(self.lst)
        return


if __name__ == "__main__":

    I = InsertionSort([4, 3, 5, 1, 2, 4])
    I.sort_with_linked_list()
    I.print_lst()
    I.lst = [4, 3, 5, 1, 2, 4]
    I.sort()
    I.print_lst()
