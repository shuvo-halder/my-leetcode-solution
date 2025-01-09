class Solution(object):
    def vowelStrings(self, words, queries):
        def isVowel(char):
            return char in "aeiou"
        
        def is_vowel_word(word):
            return isVowel(word[0]) and isVowel(word[-1])
        ans = []
        for li, ri in queries:
            count = sum(1 for word in words[li:ri+1] if is_vowel_word(word))
            ans.append(count)

        return ans
    