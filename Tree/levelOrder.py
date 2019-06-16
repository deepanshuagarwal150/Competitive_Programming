"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree
def levelOrder( root ):
    h = height(root)
    for i in range(1,h+1):
        printlevelOrder(root,i)

def printlevelOrder(root,l):
    if root == None:
        return
    if l==1:
        print(root.data, end = ' ')
    else:
        printlevelOrder(root.left,l-1)
        printlevelOrder(root.right,l-1)
        
def height(root):
    if root ==None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight >rheight:
            return lheight +1
        else:
            return rheight+1
        
