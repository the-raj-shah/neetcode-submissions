class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pos = [[[] for i in range(0,2)] for _ in range(0, 10)] 
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] != ".":
                    pos[int(board[i][j])][0].append((i))
                    pos[int(board[i][j])][1].append((j))
        for p in pos:
            rowHash = {}
            columnHash = {}
            subBoxHash = {}
            for i in range(0, len(p[0])):
                # for row
                if rowHash.get(p[0][i], 0) > 0:
                    return False
                rowHash[p[0][i]] = 1
                # for column
                if columnHash.get(p[1][i], 0):
                    return False
                columnHash[p[1][i]] = 1
                # for sub Box
                subBoxRow = math.floor(p[0][i]/3)
                subBoxColumn = math.floor(p[1][i]/3)
                if subBoxHash.get((subBoxRow, subBoxColumn), 0) > 0:
                    return False
                subBoxHash[(subBoxRow,subBoxColumn)] = 1
        return True

            