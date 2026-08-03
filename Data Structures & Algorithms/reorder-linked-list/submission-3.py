# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None or head.next.next == None:
            return

        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            if curr.next == None:
                half_start = curr
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start = head
        while half_start:
            temp1 = start.next
            temp2 = half_start.next
            start.next = half_start
            half_start.next = temp1
            start = temp1
            half_start = temp2
