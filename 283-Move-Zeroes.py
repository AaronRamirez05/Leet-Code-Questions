class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxLength = len(nums)
        temp = 0

        for i in range(maxLength):
            print(nums[i])
            if nums[i] == 0:
                for j in range(i+1,maxLength):
                    if nums[j] != 0:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
