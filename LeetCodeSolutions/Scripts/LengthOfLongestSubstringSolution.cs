namespace LeetCodeSolutions.Scripts;

public static class LengthOfLongestSubstringSolution
{
    public static int LengthOfLongestSubstring(string s)
    {
        Dictionary<char, int> amountOfCharsPerSubstring = new Dictionary<char, int>();
        int startIndexOfSubstrings = 0;
        int maxAmountOfCharsFromSubstringWithoutRepeating = 0;

        for (int i = 0; i < s.Length; i++)
        {
            var charEvalated = s[i];
            if (amountOfCharsPerSubstring.ContainsKey(charEvalated) && amountOfCharsPerSubstring[charEvalated] >= startIndexOfSubstrings)
            {
                startIndexOfSubstrings = amountOfCharsPerSubstring[charEvalated] + 1;
            }

            amountOfCharsPerSubstring[charEvalated] = i;
            int currentLength = i - startIndexOfSubstrings + 1;

            maxAmountOfCharsFromSubstringWithoutRepeating = Math.Max(maxAmountOfCharsFromSubstringWithoutRepeating, currentLength);
        }

        return maxAmountOfCharsFromSubstringWithoutRepeating;
    }
}