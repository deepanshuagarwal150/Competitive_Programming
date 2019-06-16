def height(root):
    '''
    :param root: root of the given tree.
    :return: Integer, height of the given binary tree
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
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1
    print(lheight)
