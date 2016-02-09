#############          TREES          ####################
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left=None
        self.right=None
        
    def insert(self,b):
        if self.val:    
            if b < self.val:
                if self.left is None:
                    self.left = TreeNode(b)
                else:
                    self.left.insert(b)
            elif b> self.val:
                if self.right is None:
                    self.right = TreeNode(b)
                else:
                    self.right.insert(b)
        else:
            self.val = b

class Solution:
    # @param root, a tree node
    # @return Level Order Traversed List
    def blahBlah(self,Q):
        if Q==[]:   return 
        else:
            self.result.append(Q[0].val)
            if Q[0].left:   Q.append(Q[0].left)
            if Q[0].right:  Q.append(Q[0].right)
            Q.pop(0)
            self.blahBlah(Q)
        
    def connectLevelOrder(self, root):
        self.result = []
        que = [root] 
        self.blahBlah(que)
        return self.result
        
        


if __name__=='__main__':
    n = int(input())
    
    def sinsert(c):
        for i in range(len(c)):
            if i==0:
                Tree=TreeNode(c[i])
            else:
                Tree.insert(c[i])
        return Tree
    
    for i in range(n):
        T1 = sinsert(list(map(int,input().split(' '))))
        S = Solution()
        print (S.connectLevelOrder(T1))




'''
Level Order Traversal of a BST
           4
          / \
         1   5
          \   \
           2   6
            \
             3


    result : [4, 1, 5, 2, 6, 3]
'''
