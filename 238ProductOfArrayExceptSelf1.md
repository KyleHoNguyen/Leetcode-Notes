# 238. Product of Array Except Self

labels: Arrays, Hashing, Medium

Time Completed: 45:00 Minutes

Link to problem: [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)

## Solutions
 - 3 arrays: Use one array to record all the prefix products. Find prefix by multiplying the previous numbers and record it at index i. Use another array to record all postfix number. Find postfix by multiplying all numbers after index and record it at index i. Multiply prefix and postfix product at indec i and record it in the answer array. (Time: O(n), Space: (O(n)))
 - One Array (Optimal Solution): Create one array to record results. Do a forward loop setting the array[i] to prefix product then set prefix product to nums[i] * prefix. Next do a backwords loop setting the array[i] to array[i] * postfix product and setting postfix to postfix* nums[i]. Doing this will allow less looping and only use one array instead of 3. (Time: O(n), Space: (O(n)))

 # Code 

```python
 def productExceptSelf(self, nums):

        res = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res