# 36. Valid Sudoku

labels: Arrays, Hashing, Medium

Time Completed: 45:00 minutes

Link to problem: [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)

## Solutions

I came up with a solution that seemed like brute force but was actually quite similar to the optimal solution. This solution conceptually iterated through every coordinate of the sudoku matrix and checked if there was a duplicate in the row hashmap, column hashmap, and the "square" hashmap. The optimal solution was to use three hashmaps. The row hashmap had keys representing the row number and a list of numbers as the value, the column hashmap was essentially the same. The square hashmap key was a tuple which acted like the coordinate of the 3x3 square with the values being the list of numbers inside that square. Time complexity: O(9^2), space complexity: O(9^2)

## Biggest Takeaway

The biggest takeaway was that you can use an if statement to check if a number is in a value list in O(1) time! I didn't know that. Additionally, the best thing about hashmaps is cleverly designing the "key" to fit the current problem. In this problem the hardest part was trying to figure out how to check for duplicates in the 3x3 squares of the sudoku board. The optimal solution essentially said to use the fact that theres always 9 squares and that they can be used like coordinates by simply dividing the coordinate by 3! 

### THINK WISELY ABOUT WHAT TO DEFINE THE KEY/ VALUE AS!!!!!
## Code 

```python
def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
