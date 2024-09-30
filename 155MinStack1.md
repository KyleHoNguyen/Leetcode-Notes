# 155. Min Stack

labels: Stack, Medium

Time Completed: 20:23 minutes

Link to problem: [155. Min Stack](https://leetcode.com/problems/min-stack/description/)

## Solutions

### Two Arrays

The problem is asking to design a minimum stack class, where it has normal stack operations but also can return the minimum value from the stack. To do this, I have two arrays. One is holding the values as they're pushed/popped and the other is holding the minimum value at every stage of the other array. This allows for all operations of a normal stack, but also be able to keep track of the minimum element in the stack.

1. Initialize two stacks in the constructor
1. append value to normal stack and append the minimum value in minStack
1. set both arrays to beginning to one index 
1. return last index of both arrays


#### Time Complexity: O(1)
#### Space Complexity: O(1)

## Biggest Takeaway

Read problem first. 

## Code 

```python
class MinStack:

    # have two stacks, one recoridng the elements being pushed/popped
    # the other recording the minimum value at each "stage"
    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack[-1] > val:
            self.minStack.append(val)

        else:
            self.minStack.append(self.minStack[-1])
        

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minStack = self.minStack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

     
            


                

