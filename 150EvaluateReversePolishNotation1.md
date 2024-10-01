# 150. Evaluate Reverse Polish Notation

labels: Stack, Medium

Time Completed: 29:19 minutes

Link to problem: [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

## Solutions

### Stack 

The problem outlines the input as always having 2 numbers before an operator can be used. as you iterate through the list of tokens, if you come across a number then add it to the 
stack, else it's an operator and you need to pop the last two numbers to perform the operation. after performing the operation, add the result to the stack for later operations.

1. iterate through token list
1. have series of if statements for operators
1. if + or *, order doesn't matter. perform operation
1. if - or /, order does matter. pop both operands but the first popped is operand2 and the second popped is operand1. perform operation
1. append result of operation to the stack
1. return only element left in stack after for loop ends


#### Time Complexity: O(n)
#### Space Complexity: O(n)

## Biggest Takeaway

Sometimes the dumbest looking code can be the most comprehensible code.

## Code 

```python
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # use a stack to hold the operands
        # when met with a operator, pop twice. the first pop is the second operand, the second pop is the first operand
        # perform the calculation and return the result to the stack
        # once the for loop is over, there should only be one more element, return that

        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]
        
