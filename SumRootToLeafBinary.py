"""
Sum of Root To Leaf Binary Numbers

Problem:
You are given the root of a binary tree where each node contains either 0 or 1.

Each root-to-leaf path represents a binary number:
- The root is the most significant bit.
- The leaf is the least significant bit.

Return the sum of all root-to-leaf binary numbers.

A leaf is a node with no children.

Example:

        1
       / \
      0   1
     / \ / \
    0  1 0  1

Root-to-leaf paths:
100 -> 4
101 -> 5
110 -> 6
111 -> 7

Output: 22
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------------------------
# Solution 1: Accumulator style (using nonlocal)
# -------------------------------------------------
class SolutionAccumulator:
    def sumRootToLeaf(self, root):
        total = 0

        def dfs(node, current_val):
            nonlocal total
            if not node:
                return

            current_val = current_val * 2 + node.val

            # If leaf node
            if not node.left and not node.right:
                total += current_val
                return

            dfs(node.left, current_val)
            dfs(node.right, current_val)

        dfs(root, 0)
        return total


# -------------------------------------------------
# Solution 2: Return-sum style (cleaner / preferred)
# -------------------------------------------------
class SolutionReturnStyle:
    def sumRootToLeaf(self, root):
        
        # Return the sum of all root-to-leaf paths in the subtree rooted at 'node',
        # where 'current_val' is the value formed by the path from the root to 'node'.
        def dfs(node, current_val):
            if not node:
                return 0

            current_val = current_val * 2 + node.val

            # If leaf node
            if not node.left and not node.right:
                return current_val

            return dfs(node.left, current_val) + dfs(node.right, current_val)

        return dfs(root, 0)


# -------------------------------------------------
# Helper Functions to Build Test Trees
# -------------------------------------------------
def build_example_tree():
    #         1
    #        / \
    #       0   1
    #      / \ / \
    #     0  1 0  1
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    return root


def build_single_node():
    return TreeNode(1)


def build_left_chain():
    # 1 -> 0 -> 1  (binary 101 = 5)
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.left.left = TreeNode(1)
    return root


# -------------------------------------------------
# Test Cases
# -------------------------------------------------
if __name__ == "__main__":
    sol1 = SolutionAccumulator()
    sol2 = SolutionReturnStyle()

    root1 = build_example_tree()
    root2 = build_single_node()
    root3 = build_left_chain()

    print("Using Accumulator Solution:")
    print("Test 1:", sol1.sumRootToLeaf(root1))  # Expected 22
    print("Test 2:", sol1.sumRootToLeaf(root2))  # Expected 1
    print("Test 3:", sol1.sumRootToLeaf(root3))  # Expected 5

    print("\nUsing Return-Style Solution:")
    print("Test 1:", sol2.sumRootToLeaf(root1))  # Expected 22
    print("Test 2:", sol2.sumRootToLeaf(root2))  # Expected 1
    print("Test 3:", sol2.sumRootToLeaf(root3))  # Expected 5
