# 347. Top K Frequent Elements

labels: Arrays, Hashing, Medium

Time Completed: 35:00 minutes

Link to problem: [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

## Solutions

 - Sorting Hashmap: I used a hashmap to get counts of all the distinct numbers, sorted the key, values by the values, then only returned the k greatest keys. ( Time: O(nlogn) Space: O(n))
 - BucketSort with Hashtable and array (Optimal Solution): use a hashtable for the counts and a frequency array (which holds a list) to check the frequency of each item. This frequency array will be of size n where n is the length of numbers. Iterate through the hashtable and append the key to the count bucket. Next iterate through all the buckets and append the number in decreasing order, so start from the bucket of largest count. (Time: O(n) Space: O(n))

 # Code 

```python
 def topKFrequent(self, nums, k):

        hashtable = {}
        frequencyArray = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashtable[num] = 1 + hashtable.get(num, 0)
        
        for key, value in hashtable.items():
            frequencyArray[value].append(key)
        
        res = []

        for i in range(len(frequencyArray) - 1, 0, -1):
            for num in frequencyArray[i]:
                res.append(num)
                if(len(res) == k):
                    return res