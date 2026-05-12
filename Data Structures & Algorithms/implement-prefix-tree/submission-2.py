class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not current_node.children[i]:
                current_node.children[i] = PrefixNode()
            current_node = current_node.children[i]

        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True

class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False
        
        