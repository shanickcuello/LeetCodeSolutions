namespace TwoSumWithHashTable
{
    class Program
    {
        public static int[] TwoSumWithHashTable(int[] nums, int target)
        {
            var map = new Dictionary<int, int>();

            for (var i = 0; i < nums.Length; i++)
            {
                var complement = target - nums[i];

                Console.WriteLine($"Checking number: {nums[i]}, looking for complement: {complement}");

                if (map.TryGetValue(complement, out var value))
                {
                    Console.WriteLine($"Complement {complement} found at index {value}");
                    return new int[] { value, i };
                }

                map[nums[i]] = i;
            }

            return Array.Empty<int>();
        }
    }
}