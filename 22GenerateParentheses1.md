# 739. Daily Temperatures

labels: Stack, Medium

Time Completed: 60+ minutes

Link to problem: [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)

## Solutions

### Stack 

The optimal solution is to have a stack to keep track of previous days that don't have number of days before a warmer temp. This stack will hold the index and element of said day. The algorithm is as you iterate through temperatures, you iterate through the stack if there's an element in the stack and if the current element is grater than the temperature at the top of the stack. As you iterate, pop from stack and set the index in result to the number of days between current index and index of the day. Append the element after the while loop is over. return result once the for loop is done. 

1. create stack and result array. set result array to all zeroes for len of temperatures
1. iterate through temperatures using enumerate
    1. iterate through stack while current element is greater than top of stack
    1. pop from stack and set result to the number of days it took to find a warmer temp
1. append element and index to stack as a pair
1. return result



#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

Remember to try and create a more efficient solution after your initial solution

## Code 

```python
class Solution(object):

    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0 ] * len(temperatures)

        for index, element in enumerate(temperatures):
            while stack and element > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = index - stackI
            stack.append([element, index])
        return result
            
        
