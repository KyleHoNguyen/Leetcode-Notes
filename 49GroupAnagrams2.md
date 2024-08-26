# 49. Group Anagrams

labels: Arrays, Hashing, Medium

Time Completed: 14:14 minutes

Link to problem: [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)

## Solutions

### Sorted Word for Hashtable
One solution uses the fact that anagrams will always have the same number of the same characters, so sorting the word as the "key" of the hashtable will work.

1. intiialize defaultDict(list)
1. Iterate through each word of strs
2. Sort word and join the letters by ''
3. Add it to list in hashmap
4. Return values of hashmap

#### Time complexity: O(n * k log k) 
#### Space Complexity: O(n)


### ASCII Array for Hashtable

Same intuition as the last solution, but uses ASCII values as the key instead of the sorted word.

1. Initialize defaultDict(list)
1. Iterate through each word of strs
1. Iterate through each letter of word. Initialize the array of ASCII values
1. Convert ASCII array to a tuple
1. Add word to list in hashmap
1. Return values of hashmap

#### Time Complexity: O(n * k)
#### Space Complexity: O(n)

Although the ASCII Array solution is theoretically faster, the sorted solution is faster due to Python's built in sort() method and the average size of the words. 

## Biggest Takeaway

There are multiple solutions to a problem. Remember that input is VERY important to the problem. Although the theoretical speed of one solution is faster than the other, the faster solution is better BC of the language used and the INPUT. 

 # Code 

```python
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # SORTED KEY
        hashmap = defaultdict(list) #sorted string: []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            hashmap[sorted_str].append(s)
        return hashmap.values()

def groupAnagrams(self, strs):

        # ASCII KEY
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(word)
        
        return hashmap.values()