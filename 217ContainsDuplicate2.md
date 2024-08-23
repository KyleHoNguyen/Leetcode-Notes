# 217. Contains Duplicate

labels: Arrays, Hashing, Easy

Time Completed: 1:12

Link to problem: [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

## Solutions

#### Use Hashmap properties
1. Loop through nums
2. Check if num is in hashmap, if it is return True, else add to hashmap

#### Time complexity: O(n)
#### Space Complexity: O(n)

#### Use Hashmap and check size
1. Use default python constructor for hashmap
2. Compare size of hashmap and size of nums. If it's the same size then that means all numbers are unique, no duplicate, return False. Otherwise return true

#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

- Super easy. Just use a hashmap and remember its properties. 


### HASHMAPS ARE SO COOLLLLLL

## Code: Use Hashmap and check size
```python
def containsDuplicate(self, nums):
        hashmap = set(nums)
        if len(hashmap) == len(nums):
            return False
        return True
