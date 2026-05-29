class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        result = []
        adj_list: Dict[str, List[str]] = {c: set() for w in words for c in w}

        # Build adj_list
        i = 0
        while i < len(words) - 1:
            minLen = min(len(words[i]), len(words[i + 1]))
            if len(words[i]) > len(words[i + 1]) and words[i][:minLen] == words[i + 1][:minLen]:
                return ""

            letter_ptr = 0
            while letter_ptr < len(words[i]) and letter_ptr < len(words[i + 1]):
                cur_word_letter = words[i][letter_ptr]
                next_word_letter = words[i + 1][letter_ptr]
                letter_ptr += 1
                if cur_word_letter != next_word_letter:
                    adj_list[cur_word_letter].add(next_word_letter)
                    break;

            i += 1
        
        # Traverse adjacency list and add to result
        visited = {}

        def dfs(letter):
            nonlocal result
            if letter in visited:
                return visited[letter]

            visited[letter] = True

            if letter in adj_list:
                for neighbor in adj_list[letter]:
                    print(f"evaluating {neighbor=}")
                    if dfs(neighbor):
                        return True

            visited[letter] = False
            result.append(letter)

        for char in adj_list:
            if dfs(char):
                return ""

        result.reverse()

        return "".join(result)