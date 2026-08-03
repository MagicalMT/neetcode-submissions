# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        s = set()
        l = []
        while curr:
            s.add(curr)
            l.append(curr)
            if len(s) != len(l):
                return True
            curr = curr.next
        return False