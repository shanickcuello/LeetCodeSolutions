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
            var charEvaluated = s[i];
            if (amountOfCharsPerSubstring.ContainsKey(charEvaluated) && amountOfCharsPerSubstring[charEvaluated] >= startIndexOfSubstrings)
            {
                startIndexOfSubstrings = amountOfCharsPerSubstring[charEvaluated] + 1;
            }

            amountOfCharsPerSubstring[charEvaluated] = i;
            int currentLength = i - startIndexOfSubstrings + 1;

            maxAmountOfCharsFromSubstringWithoutRepeating = Math.Max(maxAmountOfCharsFromSubstringWithoutRepeating, currentLength);
        }

        return maxAmountOfCharsFromSubstringWithoutRepeating;
    }
}