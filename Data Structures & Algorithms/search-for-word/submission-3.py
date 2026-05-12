class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        match = False
        visited_board = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def search(i, j, curr_index):
            nonlocal match
            nonlocal visited_board

            if board[i][j] != word[curr_index]:
                return

            visited_board[i][j] = True
            
            if curr_index == len(word) - 1:
                match = True
                return
            
            if i - 1 >= 0 and visited_board[i - 1][j] == False:
                search(i - 1, j, curr_index + 1)

            if j + 1 < COLS and visited_board[i][j + 1] == False:
                search(i, j + 1, curr_index + 1)

            if i + 1 < ROWS and visited_board[i + 1][j] == False:
                search(i + 1, j, curr_index + 1)

            if j - 1 >= 0 and visited_board[i][j - 1] == False:
                search(i, j - 1, curr_index + 1)

            visited_board[i][j] = False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if match:
                    return True

                search(i, j, 0)

        return match
