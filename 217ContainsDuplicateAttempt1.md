# 217. Contains Duplicate

labels: Arrays, Hashing, Easy

Time Completed: 5:00 Minutes

Link to problem: [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/)

## Solutions

 - Brute Force: iterate through list and check rest of list for the same element (Time complexity: O(n^2))
 - Sort list then check pairs:  use any sorting algorithm then check an element and the one to the right of it and see if it matches ( Time complexity: O(nlogn))
 - Hashtable (Optimal Solution): able to check for duplicate keys by using if statement before entering key (Time Complexity: O(n))

 # Code 

```python
def containsDuplicate(self, nums):
        hashtable = {}
        for element in nums:
            if element in hashtable:
                return True
            hashtable[element] = True
        return False