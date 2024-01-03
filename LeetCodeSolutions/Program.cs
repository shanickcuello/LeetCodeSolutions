// See https://aka.ms/new-console-template for more information

using LeetCodeSolutions.Scripts;

Console.WriteLine("Hello, World!");

var result = LengthOfLongestSubstringSolution.LengthOfLongestSubstring("pwwkew");
var result2 = LengthOfLongestSubstringSolution.LengthOfLongestSubstring("abcabcbb");
var result3 = LengthOfLongestSubstringSolution.LengthOfLongestSubstring("bbbbb");

Console.WriteLine(result + result2.ToString() + result3);
Console.ReadLine();