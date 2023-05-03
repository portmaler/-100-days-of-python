from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1,  TreeNode(3, TreeNode(2)))
    lis = sol.inorderTraversal(root)
    print(lis)