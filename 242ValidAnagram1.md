# 242. Valid Anagram

labels: Arrays, Hashing, Easy

Time Completed: 12:23 Minutes

Link to problem: [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

## Solutions

 - Two hashtables: create two hashtables, one for each string and iterate through one to check if all elements are the same. Make sure the length of both strings are the same. ( Time: O(s + t) Space: O(s+t))
 - Sort then Compare: sort both strings then compare strings using equals operator (Time: O(nlogn) Space: O(1))
 - One Hashtable (Optimal Solution): create one hashtable for s. iterate through t and check if element exists and iterate count. if counts aren't the same then they're not anagrams (Time: O(s + t) Space: O(s))

 # Code 

```python
 def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        hashtable = {}
        for element in s:
            hashtable[element] = 1 + hashtable.get(element, 0)
        
        for element in t:
            if element not in hashtable:
                return False
            else:
                if hashtable[element] > 0:
                    hashtable[element] = hashtable[element] - 1
                else:
                    return False

        return True