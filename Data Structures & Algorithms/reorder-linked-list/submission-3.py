# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        init_ptr = head.next
        to_reorder = []
        while init_ptr != None:
            to_reorder.append(init_ptr)
            init_ptr = init_ptr.next

        reorder_ptr = head
        left_turn = True
        while len(to_reorder) != 0:
            to_append = None
            if left_turn:
                to_append = to_reorder.pop()
            else:
                to_append = to_reorder.pop(0)
            
            reorder_ptr.next = to_append
            reorder_ptr = reorder_ptr.next
            left_turn = not left_turn
        
        reorder_ptr.next = None

            

        