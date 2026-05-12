# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        length = 0

        f_pointer = head
        while f_pointer:
            f_pointer = f_pointer.next
            length += 1

        to_remove = head
        to_remove_prev = None
        for _ in range(length - n):
            to_remove_prev = to_remove
            to_remove = to_remove.next

        if to_remove_prev:
            to_remove_prev.next = to_remove.next
        else:
            head = to_remove.next
        
        to_remove.next = None

        return head