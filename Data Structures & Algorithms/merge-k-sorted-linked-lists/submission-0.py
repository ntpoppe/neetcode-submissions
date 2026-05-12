# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        res_head = lists[0]
        if not res_head:
            return None

        arr = []

        for i in range(len(lists)):
            iter_head = lists[i]
            while iter_head:
                arr.append(iter_head)
                iter_head = iter_head.next

        arr = sorted(arr, key=lambda node: node.val)
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]

        return arr[0]
        


        