# 49. Group Anagrams

labels: Arrays, Hashing, Medium

Time Completed: 31:05 minutes

Link to problem: [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Solutions

 - Brute Force: see if the Counter() of a word matches a key in the hashmap then add it to the list of anagrams if it does. This is particularly bad because the time complexity of looking through EVERY key in the hashmap AND finding the counter of every word. (Time complexity = O(m * n * k))
 - Slightly improved brute force:  create an array of counters and if the counter was found then finding it in the hashtable was possible, which reduces the time in case the hashtable doesn't contain the key yet ( Time complexity = O(m * n * k))
 - Hashtable with ASCII values (Optimal Solution): use the ASCII values to create a count array and use that as the key of the hashmap. To do that in python you must convert it to a tuple(). This allows the hashmap to work.  (Time Complexity: O(n))

 # Code 

```python
def groupAnagrams(self, strs):

        hashmap = defaultdict(list)
        # iterate through original input list
        # if the string matches the count pattern of the key of a hashmap, then add it to 
        # the list in the hashmap

        # then iterate through hashmap, adding list of strings to final list

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(word)
        
        return hashmap.values()