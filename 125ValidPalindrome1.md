# 125. Valid Palindrome

labels: TwoPointers, Easy

Time Completed: 18:22 minutes

Link to problem: [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)

## Solutions

### Two Pointers with re.sub()

This solution uses a function called re.sub() to replace all non-alphanumeric values with empty string before iterating through the string

1. Use re.sub() to substitute non-alphanumeric values with empty string for string s
1. Convert all letters of string s to lowercase using .lower()
1. Iterate through string
1. Check if letters at position i and i-1 is equal, if not return False
1. Break for loop if i and i-1 is equal
1. Return True if loop fully executes


#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

if it works it works

## Code 

```python
 def isPalindrome(self, s: str) -> bool:

        word =  re.sub(r'[^a-zA-Z0-9]', '', s)
        word = word.lower()
        for i in range(len(word)):
            # print(word[i])
            # print(word[len(word) - i - 1])
            if word[i] != word[len(word) - i - 1]:
                return False
            if i == (len(word) - i - 1):
                break
        return True