# 128. Longest Consecutive Sequence

labels: Arrays, Hashing, Medium

Time Completed: N/A

Link to problem: [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Solutions

#### Use hashset and iterate through nums to find sequences
1. Create hashset from nums
2. Iterate through nums
3. Check if num is the start of a sequence by confirming num - 1 isnt in the set
4. if num is start of sequence, check num + 1 until it doesnt exist in the set. increment length
5. set longest length to max()
6. done

#### Time complexity: O(n)
#### Space Complexity: O(n)



## Biggest Takeaway

- Sometimes the solution calls for a simple hashmap but devising an algorithm that efficiently uses the properties of a hashmap. For example, in this problem we use a hashmap just to store the nums for O(1) lookup and devise an algorithm to check for sequences. Although we use a hashmap, the hard part was devising the algorithm


### VISUALIZE PROBLEM AND GO THROUGH SIMPLE STEPS

```python
def longestConsecutive(self, nums):
        hashmap = set(nums)
        longest = 0

        for num in nums:
            # check if its the start of a sequence
            if (num - 1) not in hashmap:
                length = 0
                while (num + length) in hashmap:
                    length += 1
                longest = max(length, longest)
        return longest
