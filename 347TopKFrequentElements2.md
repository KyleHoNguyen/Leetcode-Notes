# 347. Top K Frequent Elements

labels: Arrays, Hashing, Medium

Time Completed: 22: 05 minutes

Link to problem: [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Solutions

### Bucket Sort with Hashmaps

This solution uses the "Bucketsort" concept where the buckets hold a list of nums with the same counts. By iterating a list of lists from the highest index, we can find the list of elements with K highest occurences

1. Initialize counts hashmap using nums
1. Declare frequency nested list of length N
1. Iterate through counts hashmap and populate frequency list
1. Iterate frequency list from last index
1. Iterate through the list of each index and add to result array. Return result array once size is equal to k. 

#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

Remember that iterating through the same sized list multiple times is still considered O(n)! Decide on Key and Value pair wisely!!

## Code 

```python
 def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = dict(Counter(nums))    
        freq = [[] for i in range(len(nums) + 1)]

        for key, value in counts.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res