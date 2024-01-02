// See https://aka.ms/new-console-template for more information

using LeetCodeSolutions.Scripts;

Console.WriteLine("Hello, World!");


ListNode listNode1 = new ListNode(2,
    new ListNode(4, new ListNode(3)));

ListNode listNode2 = new ListNode(5,
    new ListNode(6, new ListNode(4)));

AddTwoNumbersSolution addTwoNumbersSolution = new AddTwoNumbersSolution();

var result = addTwoNumbersSolution.AddTwoNumbers(listNode1, listNode2);

Console.WriteLine(result);
Console.ReadLine();