from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pseudo_palindromic_paths(root: Optional[TreeNode]) -> int:
    count = 0
    stack = [(root, 0)]

    while stack:
        node, path = stack.pop()

        if node:
            path ^= 1 << node.val

            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    count += 1
            else:
                stack.append((node.right, path))
                stack.append((node.left, path))

    return count


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(1)
    result = pseudo_palindromic_paths(root)
    assert result == 2