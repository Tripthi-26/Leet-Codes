class Solution:
    def leftRightDifference(self, nums: List[int]) ->list[int]: 

        total = sum(nums)
        leftSum = 0
        answer = []

        for i in nums:
            rightSum = total - leftSum - i

            answer.append(abs(leftSum - rightSum))

            leftSum += i

        return answer