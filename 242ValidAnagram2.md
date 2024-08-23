# 242. Valid Anagram

labels: Arrays, Hashing, Easy

Time Completed: 18:38 Minutes

Link to problem: [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

## Solutions

#### One Hashtable, use counts
1. Confirm length of s and t are equal, else return False 
1. Create hashtable from s where the key is the letter and the value is the counts of the letter
1. Iterate through t, check if letter is in hashmap and the count isn't 0. if letter isnt in hashmap OR count is 0 then words arent anagrams

#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

- Make sure to think about edge cases. Was an edgecase if the strings weren't the same size or both words had the same letters but different number of letters. 

### VALUES JUST AS IMPORTANT AS KEY
 # Code 

```python
def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        hashmap = {}
        for letter in s:
            if letter in hashmap:
                hashmap[letter] += 1
            else:
                hashmap[letter] = 1
            

        for letter in t:
            if letter not in hashmap:
                return False
            else:
                if hashmap[letter] > 0:
                    hashmap[letter] = hashmap[letter] - 1
                else:
                    return False
        
        return True
        