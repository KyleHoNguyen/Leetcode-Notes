# 11. Container With Most Water

labels: TwoPointers, Medium

Time Completed: 23:05 minutes

Link to problem: [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

## Solutions

### Two Pointers 

This solution uses two pointers. The algorithm devised is to set the first pointer to the beginning of the array and the second pointer to the last index of the array. As the goal is to return the maximum amount of water a container can store, you are trying to find the largest container.  This can be done by looking for the largest minimum height of lines, starting from both ends and iterating lines depending on which line is smaller. 

1. Create pointer1 and pointer2, set to first and last index of the array
1. Iterate until left is not less than right
1. Calculate the max water using min() height of container * (right - left) length.
1. Iterate the line thats smaller. so for example, if left height is smaller than right height, iterate the left line
1. return result after loop


#### Time Complexity: O(n)
#### Space Complexity: O(1)

## Biggest Takeaway

Finish implementing solution before trying to make it more efficient. Maybe your initial thought is the most efficient. 

## Code 

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        while(left < right):
            tempArea = min(height[left], height[right]) * (right - left)
            res = max(res, tempArea)
            if height[left] < height[right]:
                left +=1
                continue
            else:
                right -= 1
            
        return res
        
