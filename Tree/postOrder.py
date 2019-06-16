class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def postOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated post order Traversal of the given tree.
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
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end = ' ')
