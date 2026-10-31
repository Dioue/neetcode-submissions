class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mappedNums = new HashMap<>();
        int numsLen = nums.length;

        for (int i = 0; i < numsLen; i++) {
            int compliment = target - nums[i]; // 3, -4, 3  

            if (!mappedNums.containsKey(compliment)) {
                mappedNums.put(nums[i], i); // {-3:0, 4:1, }
                continue;
            }

            return new int[] {mappedNums.get(compliment), i};
        }

        return new int[] {0, 0};
    }
}
