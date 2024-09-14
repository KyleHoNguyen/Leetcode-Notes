# 167. Two Sum II - Input Array Is Sorted

labels: TwoPointers, Medium

Time Completed: 23:05 minutes

Link to problem: [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

## Solutions

### Two Pointers 

This solution uses two pointers. The algorithm devised is to set the first pointer to the beginning of the array and the second pointer to the last index of the array. Since the array is sorted, we can use two pointers to see which pointer to iterate to get the correct sum. 

1. Create pointer1 and pointer2, set to first and last index
1. Iterate through the array
1. Check if sum is equal to, less than, or larger than target sum. Iterate pointers or return indexes based on answer


#### Time Complexity: O(n)
#### Space Complexity: O(1)

## Biggest Takeaway

Always check the input. Constraints on the input can help figure out solutions

## Code 

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
    
        while index1 < index2:
            currentSum = numbers[index1] + numbers[index2]
            if currentSum == target:
                return index1 + 1, index2 + 1
            elif currentSum > target:
                index2 -= 1
            else:
                index1 += 1
