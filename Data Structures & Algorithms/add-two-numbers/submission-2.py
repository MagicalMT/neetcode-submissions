# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        l1_head = l1
        l2_head = l2
        plus_1 = 0
        while l1_head or l2_head:
            if l1_head:
                l1_num = l1_head.val
            else:
                l1_num = 0
            if l2_head:
                l2_num = l2_head.val
            else:
                l2_num = 0
            total = l1_num + l2_num + plus_1
            plus_1 = 0
            if total >= 10:
                plus_1 = 1
                total -= 10
            curr.next = ListNode(total)
            curr = curr.next
            if l1_head:
                l1_head = l1_head.next
            if l2_head:
                l2_head = l2_head.next

        if plus_1 == 1:
            curr.next = ListNode(1)

        return dummy.next