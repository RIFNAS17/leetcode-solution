class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        reverse_words=words[::-1]
        reversed_string=' '.join(reverse_words)
        return reversed_string