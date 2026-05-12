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
    public bool HasCycle(ListNode head) {
        var steps = 0;
        var trail = head;
        var ahead = head.next;

        while (ahead != null)
        {
            if (ahead == trail)
                return true;

            ahead = ahead.next;

            if (steps % 2 == 1)
                trail = trail.next;

            steps++;        
        }

        return false;
    }
}
