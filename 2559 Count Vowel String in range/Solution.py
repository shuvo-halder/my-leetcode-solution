class Solution(object):
    def vowelStrings(self, words, queries):
        def is_vowel(c):
            return c in "aeiou"
        def is_vowel_word(word):
            return is_vowel(word[0]) and is_vowel(word[-1])
        
        n = len(words)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_word(words[i]) else 0)

        ans = []

        for li, ri in queries:
            ans.append(prefix[ri + 1] - prefix[li])
        return ans