namespace LeetCodeSolutions.Scripts;
//https://leetcode.com/problems/two-sum
public class TwoSum
{
    public int[]? TwoSums(int[] nums, int target)
    {
        Dictionary<int, int> numIndexMap = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];
        
            if (numIndexMap.ContainsKey(complement))
            {
                return new int[] { numIndexMap[complement], i };
            }
            numIndexMap[nums[i]] = i;
        }
        throw new ArgumentException("No match was found");
    }
}