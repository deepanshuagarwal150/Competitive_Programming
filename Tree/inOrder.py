# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def InOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated in order Traversal of the given tree.
    {
        class Node:
        def __init__(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    if root == None:
        return
    else:
        InOrder(root.left)
        print(root.data, end = ' ')
        InOrder(root.right)
