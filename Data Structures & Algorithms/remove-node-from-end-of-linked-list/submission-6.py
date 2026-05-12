# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        first_p = head
        second_p = head

        for _ in range(n):
            first_p = first_p.next

        prev = None
        while first_p:
            first_p = first_p.next
            prev = second_p
            second_p = second_p.next

        if prev:
            prev.next = second_p.next
        else:
            head = second_p.next

        second_p.next = None

        return head
        
        