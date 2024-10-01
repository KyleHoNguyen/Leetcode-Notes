# 853. Car Fleet

labels: Stack, Medium

Time Completed: N/A Minutes

Link to problem: [853. Car Fleet](https://leetcode.com/problems/car-fleet/description/)

## Solutions

### Array with pairs and stack of pairs

The optimal solution calls for the use of a sorted array of pairs. The pairs are the position of the cars and the speed. It is then sorted by position for traversal. The algorithm traverses through this sorted array in reverse, adding the time the car would reach the target to the stack. if the stack was greater than or equal to 2 this means there are atleast two cars in the stack and can be compared if the most recent car and the car ahead of it collides, if it does then pop from stack to save the fleet. then return fleet. 


#### Time Complexity: O(nlogn)
#### Space Complexity: O(n)

## Biggest Takeaway

Some problems require a very mathy approach. 

## Code 

```python
 class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position, speed)]
        fleets = []

        for p,s in sorted(pair)[::-1]:
            fleets.append((target - p ) / s)
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop()
        return len(fleets)
            

                
             
        