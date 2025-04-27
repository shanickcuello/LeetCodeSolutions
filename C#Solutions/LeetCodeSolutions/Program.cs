// See https://aka.ms/new-console-template for more information

using LeetCodeSolutions.Scripts;

Console.WriteLine("Hello, Universe!");

#region TwoSumWithHashTable
// int[] nums = { 2, 7, 11, 15 };
// int target = 9;
//
// int[] result = TwoSumWithHashTable.Program.TwoSumWithHashTable(nums, target);
//
// if (result.Length == 2)
// {
//     Console.WriteLine($"Indices found: {result[0]}, {result[1]}");
//     Console.WriteLine($"Numbers: {nums[result[0]]}, {nums[result[1]]}");
// }
// else
// {
//     Console.WriteLine("No two sum solution found.");
// }
#endregion

#region ReverseLinkedList

ListNode head = new ListNode(1, 
    new ListNode(2, 
        new ListNode(3, 
            new ListNode(4, 
                new ListNode(5)))));

Console.WriteLine("Original List:");
PrintList(head);

Solution solution = new Solution();
ListNode reversedHead = ReverseLinkedList.Solution.ReverseList(head);

Console.WriteLine("Reversed List:");
PrintList(reversedHead);
static void PrintList(ListNode head)
{
    ListNode current = head;
    while (current != null)
    {
        Console.Write(current.val + " -> ");
        current = current.next;
    }
    Console.WriteLine("null");
}
#endregion
Console.ReadLine();