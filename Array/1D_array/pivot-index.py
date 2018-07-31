class Array:
	def pivotindex(self, nums):
		sum_l = 0
		sum_R = sum(nums)
		for i in range(len(nums)):
			sum_R -= nums[i]
			if sum_l == sum_R:
				return i
			sum_l += nums[i]
		return -1

n = [1,2,3,5,6]
a = Array()
print a.pivotindex(n)

