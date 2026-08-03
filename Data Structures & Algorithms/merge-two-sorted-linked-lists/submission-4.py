# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        curr = None
        l1 = list1
        l2 = list2
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        while l1 and l2:
            if l1.val <= l2.val:
                if start == None:
                    start = l1
                    curr = start
                else:
                    curr.next = l1
                    curr = curr.next
                l1 = l1.next
            else:
                if start == None:
                    start = l2
                    curr = start
                else:
                    curr.next = l2
                    curr = curr.next
                l2 = l2.next
        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1
        return start
        