# 1. Two Sum

labels: Arrays, Hashing, Easy

Time Completed: 4:33 minutes

Link to problem: [1. Two Sum](https://leetcode.com/problems/two-sum/description/)

## Solutions

#### Use Hashmap as fast lookup for difference

1. Iterate through nums
2. Find difference by subtracting number from target
3. See if difference can be found in hashmap
4. If difference not found, insert value, index pair into hashmap. Otherwise return index of the difference found and the current index


#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

- Know what Enumerate() does for lists and hashmaps!! It creates pairs of the value and index for lists while it creates pairs of keys and values for hashmaps. 
- Was really important for this problem as it simplified getting the index of the numbers from the array

### USE ENUMERATE() WHEN YOU CAN!!!!!

 # Code 

```python
 def twoSum(self, nums, target):
        hashmap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], index]
            else:
                hashmap[value] = index
        return []