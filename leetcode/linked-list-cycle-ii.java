/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode current = head;
        ListNode fast = head;
        boolean found = false;
        while (fast != null && fast.next != null) {
                current = current.next;
                fast = fast.next.next; 
            if (current == fast) {
                found = true;
                break;
            }
        }
        if (found) {
                current = head;
                while (current != fast) {
                    current = current.next; 
                    fast = fast.next;
                }
            return current;
        }
        return null;
    }
}