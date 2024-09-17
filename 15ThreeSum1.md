# 15. 3Sum

labels: Two-Pointers, Medium

Time Completed: 47:06 minutes

Link to problem: [15. 3Sum](https://leetcode.com/problems/3sum/description/)

## Solutions

### Two Pointers 

This problem/solution is based on two sum and two sum 2. The difference is that there can be duplicates in the input array and that u dont wan't to have repeat sums. The thinking is that, once you sort the array, you can iterate through the list and perform two sum on the last two numbers. You can confirm the duplicate number won't produce a repeat sum by ordering the list and skipping the next number if the previous number is the same. 

1. sort nums using nums.sort() or sorted(nums)
1. iterate through nums using enumerate
1. initialize left and right pointer like two sum 2. ( l = i + 1, r = len(nums) - 1)
1. confirm the current number is not equal to the previous number
1. perform two sum solution
1. when solution found, add tuple to array, index left and right pointers. index left pointer until the previous isnt the same. This ensure no duplicate answers.


#### Time Complexity: O(n^2)
#### Space Complexity: O(1)

## Biggest Takeaway

Try to break down the provlem into smaller problems that is similar to problems you've done before. sometimes the same algorithms that solved previous smaller problems can be used to solve the bigger problem!!

## Code 

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all sets of 3 numbers that are distinct which add up to 0
        # order of the output/ sets do not matter
        # will there always be an answer? no
        # are there negatives? yes
        # will there only be numbers in the list? yes
        # what is the average length of the list? from 3 to 3000
        # can the numbers be repeated, but not the indices? yes
        # is the array sorted? no
        # so to confirm, the problem is asking to return all sets of 3 numbers, where the indices
        # are not repeated, that add up to zero? yes

        # Algorithm
        # sort the nums list
        # iterate through the list
        # set left and right pointer
        # do two sum 2 answer ( so while loop until you find answer or l < r is not true)
        # iterate left pointer until its not the same

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

     
            


                

