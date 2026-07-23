class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memory = {}

        def recursive(word):

            if not word:
                return True
            
            if word in memory:
                return memory[word]

            memory[word] = any([recursive(word[len(prefix):]) for prefix in wordDict if word.startswith(prefix)])
            
            return memory[word]
            

        return recursive(s)
        