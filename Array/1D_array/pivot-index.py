class Array:
	def pivotindex(self, nums):
		sum_l = 0
		sum_R = sum(nums)
		for i in range(len(nums)):
			sum_R1 -= nums[i]
			if sum_l == sum_R:
				return i
			sum_l += nums[i]
		return -1
