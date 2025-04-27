using LeetCodeSolutions.Scripts;

namespace ReverseLinkedList
{
    public static class Solution
    {
        public static ListNode ReverseList(ListNode head)
        {
            var current = head;
            ListNode previous = null;
            while (current != null)
            {
                var temporaryNext = current.next;
                current.next = previous;
                previous = current;
                current = temporaryNext;
            }

            return previous;
        }
    }
}