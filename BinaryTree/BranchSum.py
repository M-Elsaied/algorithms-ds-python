class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    def BranchSum(root):
        sums = []
        CalcBranchSum(root, 0, sums)
        return sums
    def CalcBranchSum(node, RunSum, sums):
        if node is None:
            return
        RunSum+=node.value
        if node.right is None and node.left is None:
            sums.append(RunSum)
        CalcBranchSum(node.left, RunSum,  sums)
        CalcBranchSum(node.right, RunSum,  sums)
        