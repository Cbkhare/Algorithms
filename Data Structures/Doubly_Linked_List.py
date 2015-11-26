class Node:
    def __init__(self,data=None,nxt=None,prv=None):     #by default None 
        self.data = data
        self.nxt = nxt
        self.prv = prv
    def __str__(self):
        return ('Node[Data='+str(self.data)+']')
    
class Linked_List:
    def __init__(self):
        self.head = None                      #by default None
        self.tail = None 

    def insert(self,data):
        if self.head==None:                   #i.e there is no element in the list
            self.head = Node(data)
        else:
            if self.head.nxt == None:         #for insertion of second element 
                self.tail = Node(data,None,self.head)
                self.head.nxt = self.tail
            else:
                old_tail = self.tail          #for insertion of 3rd and so forth 
                self.tail = Node(data,None,old_tail)
                old_tail.nxt = self.tail
            
        return (self.display())

    def delete(self,data):
        if self.head==None:
            return ('Doubly Linked List Empty')
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
                current.nxt.prv = current.prv
                return(self.display())
            else:
                return ('Element does not exist')
                
    def display(self):
        if self.head==None:
            return ('Double Linked List Empty')
        else:
            current = self.head
            Link_list= str(current)     #instantiated with head
            while current.nxt !=None:
                current = current.nxt
                Link_list += str(current)
            return (Link_list)
        
    def display_reverse(self):
        if self.head==None:
            return ('Double Linked List Empty')
        else:
            current = self.tail
            Link_list= str(current)     #instantiated with tail
            while current.prv != None:
                current = current.prv
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
    print (B.display_reverse())
    
    
    

'''
>>> 
Double Linked List Empty
Doubly Linked List Empty
Node[Data=1]
Node[Data=1]Node[Data=2]
Node[Data=1]Node[Data=2]Node[Data=3]
Node[Data=1]Node[Data=2]Node[Data=3]Node[Data=4]
Node[Data=1]Node[Data=2]Node[Data=3]Node[Data=4]Node[Data=5]
Node[Data=1]Node[Data=2]Node[Data=4]Node[Data=5]
Element does not exist
Node[Data=5]Node[Data=4]Node[Data=2]Node[Data=1]
'''
