class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    arithmetic_series_sum = n*(n+1) // 2
    array_actual_sum = sum(nums)
    return arithmetic_series_sum - array_actual_sum
