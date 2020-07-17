def Invert(tree):
    queue = [tree]
    while len(tree):
        current = queue.pop(0)
        if current is None:
            continue
        swap(current)
        queue.append(current.left)
        queue.append(current.right)