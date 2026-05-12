class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.is_leaf = False

    trie_root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.insert_words_into_trie(words)

        ROWS, COLS = len(board), len(board[0])
        result = []

        path = []

        def dfs(r, c, trie_curr, string):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in path:
                return

            letter = board[r][c]
            letter_index = ord(letter) - ord('a')
            if trie_curr.children[letter_index] == None:
                return

            string = string + letter
            trie_curr = trie_curr.children[letter_index]
            if trie_curr.is_leaf and string not in result:
                print(f"{string=}")
                result.append(string)

            path.append((r, c))

            dfs(r + 1, c, trie_curr, string)
            dfs(r - 1, c, trie_curr, string)
            dfs(r, c + 1, trie_curr, string)
            dfs(r, c - 1, trie_curr, string)

            path.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                path = []
                dfs(r, c, self.trie_root, "")

        return result

    def insert_words_into_trie(self, words: List[str]) -> None:
        for word in words:
            curr = self.trie_root
            for i in range(len(word)):
                child_index = ord(word[i]) - ord('a')
                if curr.children[child_index] == None:
                    curr.children[child_index] = self.TrieNode()

                if i == len(word) - 1:
                    curr.children[child_index].is_leaf = True

                curr = curr.children[child_index]