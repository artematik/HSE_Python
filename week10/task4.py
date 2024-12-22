"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        answer = []

        q = deque([root])

        while q:
            new_q = deque([])
            cur_lvl = []
            for node in q:
                cur_lvl.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
            answer.append(cur_lvl)

        return answer[::-1]