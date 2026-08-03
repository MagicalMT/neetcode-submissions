# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        remove_index = length - n

        curr = head
        num = 0
        while num <= remove_index:
            if remove_index == 0:
                head = head.next
            elif num == remove_index - 1:
                curr.next = curr.next.next
                break
            curr = curr.next
            num += 1
        return head