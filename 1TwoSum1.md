# 1. Two Sum

labels: Arrays, Hashing, Easy

Time Completed: 15:31 minutes

Link to problem: [1. Two Sum](https://leetcode.com/problems/two-sum/description/)

## Solutions

 - Brute Force: Try every possible comparison/ sum ( Time: O(n^2) Space: IDK)
 - Hashtable (Optimal Solution): use enumerate() while traversing through nums list to obtain the index and num from the array. find the complement of the sum and look for that number in the existing hashtable, if it exists return the indices, if not then add the num and index pair into the hashtable.(Time: O(n) and Space: O(n))

 # Code 

```python
 def twoSum(self, nums, target):

        nums_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in nums_index:
                return [nums_index[complement], index]

            nums_index[num] = index
        
        return []