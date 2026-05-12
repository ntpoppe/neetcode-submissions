/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;

        var cur1 = list1;
        var cur2 = list2;
        ListNode head = null;
        ListNode prev = null;

        while (cur1 != null && cur2 != null)
        {
            ListNode less;
            if (cur1.val < cur2.val)
            {
                less = cur1;
                cur1 = cur1.next;
            }
            else
            {
                less = cur2;
                cur2 = cur2.next;
            }

            if (head == null)
                head = less;

            if (prev != null)
                prev.next = less;
            
            prev = less;
            
        }

        if (cur1 != null)
            prev.next = cur1;
        
        if (cur2 != null)
            prev.next = cur2;

        return head;
    }
}