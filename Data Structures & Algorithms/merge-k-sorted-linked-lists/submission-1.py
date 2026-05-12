# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        merged = lists[0]
        lists.pop(0)
        if not merged:
            return None

        while len(lists) > 0:
            to_merge = lists[0]
            merged_pointer = merged
            head = None
            prev = None
            while merged_pointer and to_merge:
                less = None
                if merged_pointer.val < to_merge.val:
                    less = merged_pointer
                    merged_pointer = merged_pointer.next
                else:
                    less = to_merge
                    to_merge = to_merge.next

                if not head:
                    merged = less
                    head = less

                if prev:
                    prev.next = less
                
                prev = less
            
            if merged_pointer:
                prev.next = merged_pointer

            if to_merge:
                prev.next = to_merge

            lists.pop(0)

        return merged


        