class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        l, res = 0, -float('inf')
        curr_sum = 0

        for r in range(len(nums)):
            #sumtingright
            curr_sum += nums[r]
            counter[nums[r]] += 1
            #sumtingwonf
            while (r-l+1) > k or counter[nums[r]] > 1:
                counter[nums[l]] -= 1
                curr_sum -= nums[l]
                l += 1

            if (r-l+1) == k:
                res = max(res, curr_sum)
        
        return res if res != -float('inf') else 0
