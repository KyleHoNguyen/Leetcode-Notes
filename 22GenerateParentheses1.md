# 22. Generate Parentheses

labels: Stack, Medium

Time Completed: N/A minutes

Link to problem: [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)

## Solutions

### Stack + Recursion

The optimal solution is to think of the different cases in which you can add anopen or close parentheses and when you can return the statement.
You can only insert an open parentheses if there's less than n opens. you can only insert a closed parenthesis if there's more open parentheses.
you can only return the statement/ copmbination if the open and close parentheses is equal to n. 


#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

Sometimes you need to look at the facts before trying to figure out the solution. for example, in this problem you had to figure out that there are certain situations where you can insert a parenthesis and when you return the statement. 

## Code 

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # add open parenthesis if < n
        # add close parenthesis if < open
        # add to list if b oth = n
        stack = []
        result = []

        def backTrack(openP, closeP):
            if openP == closeP == n:
                result.append("".join(stack))
                return
            if openP < n:
                stack.append("(")
                backTrack(openP + 1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(")")
                backTrack(openP, closeP + 1)
                stack.pop()
        backTrack(0,0)
        return result

        
        
