def countLeaves(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)
