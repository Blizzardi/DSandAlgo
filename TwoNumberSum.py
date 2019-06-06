# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers
# in the target the function should return them in an array in sorted order

Sample input: [3,1,2,4,5] 8
Sample output: [3,5]


# O(nlog(n)) | O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array)-1
	while left < right:
		if array[left] + array[right] == targetSum:
			return [array[left],array[right]]
		elif array[left] + array[right] < targetSum:
			left+=1
		elif array[left] + array[right] > targetSum:
			right-=1
	
  	return []

