class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                num_boxes = (i//3)*3 + j//3

                if num in rows[i] or num in cols[j] or num in boxes[num_boxes]:
                    return False
                
                rows[i].update(num)
                cols[j].update(num)
                boxes[num_boxes].update(num)
        return True
                
        



            