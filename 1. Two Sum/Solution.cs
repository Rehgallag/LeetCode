using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _1.Two_Sum
{
    public class Solution
    {
        private const int V = 2;

        static void Main(string[] args)
        {
            int[] nums = {3,2,4};
            int target = 6;
            Console.WriteLine($"Output: [{string.Join(", " , TwoSum(nums, target))}]");
        }

        public static int[] TwoSum(int[] nums, int target)
        {
            var d1 = new Dictionary<int, int>();

            for (int i = 0; i < nums.Length; i++)
            {
                int result = target - nums[i];
                if (d1.ContainsKey(result))
                {
                    return new int[] { d1[result], i };
                }
                else if (!d1.ContainsKey(nums[i])) // deals with dupes in the array
                {
                    d1.Add(nums[i], i);
                }
            }
            return null;
        }
    }
}
