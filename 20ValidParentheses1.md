# 20. Valid Parentheses

labels: Stack, Easy

Time Completed: 17:14 minutes

Link to problem: [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)

## Solutions

### Stack and Hashmap

The optimal solution uses a stack to determine the order of open/close parentheses and a hashmap for fast retrieval of matching parentheses.
The algorithm basically is if you find an open parentheses then append it to the stack. if its a closing parentheses, check if the stack is not empty, 
check if the top of the stack is equal to the matching closing parenthesis. you can make this check easier by utilizing a hashmap. 

1. initialize stack and define hashmap for matching close open parentheses. The key is close parenthesis and the value is the open.
2. iterate through string
3. if parenthesis not in the map then append to stack
4. if stack not empty and top of stack not equal to matching parenthesis in map, return false. else pop
5. return true if stack empty 

#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

Remember to think about how you can utilize multiple data structures for a problem

## Code 

```python
class Solution(object):
    def isValid(self, s):
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
        
