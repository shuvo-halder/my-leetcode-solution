from attr import s


class Solution:

    def lengthOfLongestSubstring(self, s: str):
        char_index_map = {}
        max_length = 0
        start = 0
        s = "abcabcbb"
        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1
            char_index_map[char] = i
            max_length = max(max_length, i - start + 1)
            print(max_length)
        return max_length
    

    