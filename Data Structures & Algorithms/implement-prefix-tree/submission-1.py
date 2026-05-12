class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        last_node = self.root
        for i in range(len(word)):
            existing_child = last_node.children.get(word[i])
            if existing_child:
                last_node = existing_child
            else:
                new_node = PrefixNode()
                last_node.children[word[i]] = new_node
                last_node = new_node

            if i == len(word) - 1:
                last_node.is_end_of_word = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for i in range(len(word)):
            child = ptr.children.get(word[i])
            if not child:
                return False

            if i == len(word) - 1 and child.is_end_of_word:
                return True

            ptr = child

        return False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for i in range(len(prefix)):
            child = ptr.children.get(prefix[i])
            if not child:
                return False

            if i == len(prefix) - 1:
                return True

            ptr = child

        return False

class PrefixNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
        