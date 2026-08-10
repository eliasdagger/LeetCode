# LeetCode 104 - Maximum Depth of Binary Tree (Easy)
#
# Given the root of a binary tree, return its maximum depth: the number of nodes
# along the longest path from the root down to the farthest leaf.
#
# An empty tree has depth 0 and a single node has depth 1.
#
# Example: [3,9,20,null,null,15,7]  ->  3

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

        