def maxPathSum(tree):
    _,final = findMaxSum(tree)
    return final
def findMaxSum(tree):
    if tree is None:
        return (o, float("-inf"))
    leftSumBranch, leftSumPath = findMaxSum(tree.left)
    rightSumBranch, rightSumPath = findMaxSum(tree.right)
    maxSumBranch = max(leftSumBranch, rightSumBranch)

    value = tree.value
    maxSumPath = max(maxSumBranch+value, value)
    maxSumNode = max(leftSumPath + value + rightSumPath, maxSumPath)
    maxSum = max(leftSumPath, rightSumPath, maxSumNode)
    return (maxSumBranch, maxSum)