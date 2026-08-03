"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dummy = Node(0)
        temp = dummy
        random_dict = {}
        while curr:
            new_node = Node(curr.val)
            temp.next = new_node
            new_node.random = curr.random
            random_dict[curr] = new_node
            temp = temp.next
            curr = curr.next
        
        curr = dummy.next
        while curr:
            curr.random = random_dict.get(curr.random)
            curr = curr.next
        return dummy.next
        


