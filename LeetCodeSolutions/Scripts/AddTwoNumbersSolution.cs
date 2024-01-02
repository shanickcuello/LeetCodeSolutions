namespace LeetCodeSolutions.Scripts;
//https://leetcode.com/problems/add-two-numbers/

public class AddTwoNumbersSolution
{
    #region FirstSolution

//     public ListNode AddTwoNumbersSolution(ListNode l1, ListNode l2)
//     {
//         var treeDigitNumberFromList1 = GetNumbersRevertedAsA3DigitNumber(l1);
//         var treeDigitNumberFromList2 = GetNumbersRevertedAsA3DigitNumber(l2);
//
//         var sumOfDigits = int.Parse(treeDigitNumberFromList1) + int.Parse(treeDigitNumberFromList2);
//         var sumOfDigitsAsString = sumOfDigits.ToString();
//
//         var firstDigit = sumOfDigitsAsString.ToCharArray()[0].ToString();
//         var second = sumOfDigitsAsString.ToCharArray()[1].ToString();
//         var third = sumOfDigitsAsString.ToCharArray()[2].ToString();
//
//         var n1 = int.Parse(firstDigit);
//         var n2 = int.Parse(second);
//         var n3 = int.Parse(third);
//
//         var linkedListResult =
//             new ListNode(n1,
//                 new ListNode(n2, new ListNode(n3)));
//         return linkedListResult;
//     }
//
//     string GetNumbersRevertedAsA3DigitNumber(ListNode l1)
//     {
//         int[] numbersOfL1 = new[] { l1.next.next.val, l1.next.val, l1.val };
//         string numbersOfListInverted = "";
//         foreach (int number in numbersOfL1)
//         {
//             numbersOfListInverted += number.ToString();
//         }
//
//         return numbersOfListInverted;
//     }
// }

    #endregion

    //Good ms, bad memory
    #region SecondSolution
    //
    // public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    // {
    //     ListNode dummy = new ListNode(0);
    //     ListNode current = dummy;
    //     int carry = 0;
    //
    //     while (l1 != null || l2 != null || carry != 0)
    //     {
    //         int x = (l1 != null) ? l1.val : 0;
    //         int y = (l2 != null) ? l2.val : 0;
    //
    //         int sum = x + y + carry;
    //         carry = sum / 10;
    //
    //         current.next = new ListNode(sum % 10);
    //         current = current.next;
    //
    //         if (l1 != null) l1 = l1.next;
    //         if (l2 != null) l2 = l2.next;
    //     }
    //
    //     return dummy.next;
    // }

    #endregion

    //Good memory, bad ms
    #region ThirdSolution

    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) 
    {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0)
        {
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = x + y + carry;
            carry = sum / 10;

            if (current.next == null)
            {
                current.next = new ListNode(sum % 10);
            }
            else
            {
                current.next.val = sum % 10;
            }

            current = current.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return dummy.next;
    }

    #endregion
    
}

public class ListNode
{
    public int val;
    public ListNode next;

    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}