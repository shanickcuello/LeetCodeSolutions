/*
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
    var count = 0;
    var map = [];
    for (var i = 0; i < s.length; i++) {
        var letter = s[i];
        if (map.includes(letter)) {
            var index = map.indexOf(letter);
            map.splice(index, 1);
            count++;
        } else {
            map.push(letter);
        }
    }
    count = count * 2;
    if (map.length) {
        count++;
    }

    return count;
};