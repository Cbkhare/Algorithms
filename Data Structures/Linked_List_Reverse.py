class Node:
    def __init__(self,data,nxt=None):     #by default None 
        self.data = data
        self.nxt = None

    def __str__(self):
        return ('Node['+str(self.data)+']')
    
class Linked_List:
    def __init__(self):
        self.head = None                      #by default None

    def insert(self,data):
        if self.head==None:                   #i.e there is no element in the list
            self.head = Node(data)
        else:
            current = self.head               #point to begining
            while current.nxt != None :
                current = current.nxt
            current.nxt = Node(data)
        return (self.display())
    
    def delete(self,data):
        if self.head==None:
            return ('Linked List Empty')
        else:
            found = False
            current = self.head
            old_current = ''
            while current.nxt!= None and not found:
                if current.data==data:
                    found = True
                    break
                else:
                    old_current = current
                    current = current.nxt
            if found:
                old_current.nxt = current.nxt
                return(self.display())
            else:
                return ('Element does not exist')
            
                
    def display(self):
        if self.head==None:
            return ('Linked List Empty')
        else:
            current = self.head
            Link_list= str(current)     #instantiated with head
            while current.nxt!=None:
                current = current.nxt
                Link_list += str(current)
            return (Link_list)

    def reverse(self):
        if self.head==None:
            return ('Linked List Empty')
        else:
            current = self.head
            old = None
            while current.nxt !=None:
                temp = current.nxt
                current.nxt = old 
                old = current
                current = temp
            current.nxt = old
            Link_list= str(current)     #instantiated with head
            while current.nxt!=None:
                current = current.nxt
                Link_list += str(current)
            return (Link_list)
            
              
if __name__=='__main__':
    B = Linked_List()
    #n = int(input())
    print (B.display())
    print (B.delete(1))
    print (B.insert(1))
    print (B.insert(2))
    print (B.insert(3))
    print (B.insert(4))
    print (B.insert(5))
    print (B.delete(3))
    print (B.delete(6))
    print (B.reverse())   

'''
Reverse a linked list. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.
'''
