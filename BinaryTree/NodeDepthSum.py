# first solution
def nodeDepth(root):
    sums=[]
    CalcDepth(root, 0, sums)
    return sum(sums)
def CalcDepth(node, depth, sums):
    if node is None:
        return
    CalcDepth(node.left, depth+1, sums)
    CalcDepth(node.right, depth+1, sums)
    sums.append(depth)

#second solution
def nodeDepth(root, depth=0):
    if node is None:
        return 0
    return depth + nodeDepth(node.left, depth + 1) + nodeDepth(node.right, depth+1)