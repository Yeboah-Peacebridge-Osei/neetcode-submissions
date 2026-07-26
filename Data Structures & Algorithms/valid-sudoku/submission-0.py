from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        use hashtables to check for duplicates on each row,column and subgrid
        hashtable
        2*2 matrix

        iterate through matrix
            skip empty cells 

        check for duplicates in hashtable
            return false if there is
        if not store it.

        return true if no problem was found

        '''
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        subgridCheck = defaultdict(set)


        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if (board[row][col] in rowCheck[row] 
                or board[row][col] in colCheck[col] 
                or board[row][col] in subgridCheck[(row//3, col//3)]):
                    return False

                rowCheck[row].add(board[row][col])
                colCheck[col].add(board[row][col])
                subgridCheck[(row//3, col//3)].add(board[row][col])

        return True





















        