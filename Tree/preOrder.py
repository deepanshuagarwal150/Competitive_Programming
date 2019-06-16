def preorder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated pre order Traversal of the given tree.
    {
        # Node Class:
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
        print(root.data , end = ' ')
        preorder(root.left)
        preorder(root.right)
