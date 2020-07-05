def permutation(arr):
    perms = []
    permutationHelper(arr, [], perms)
    return perms
def permutationHelper(arr, currentPermutation, perms):
    if not len(arr) and len(currentPermutation):
        perms.append(currentPermutation)
    else:
        for i in range(len(arr)):
            newArr = arr[:i]+arr[i+1:]
            newPermutation = currentPermutation + [arr[i]]
            permutationHelper(arr, newPermutation, perms)