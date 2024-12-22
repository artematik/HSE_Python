"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque()
        l = deque()
        result = []

        previous = 0
        aux = []

        q.append(root)
        l.append(0)

        while q and l:
            node = q.popleft()
            level = l.popleft()

            if level == previous + 1:
                if level % 2 == 0:
                    aux.reverse()

                result.append(aux)
                aux = []

            aux.append(node.val)

            if node.left:
                q.append(node.left)
                l.append(level + 1)

            if node.right:
                q.append(node.right)
                l.append(level + 1)

            previous = level

        if (previous + 1) % 2 == 0:
            aux.reverse()

        result.append(aux)

        return result