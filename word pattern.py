class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        word = s.split(" ")
        if len(pattern) != len(word):
            return False
        char_to_word = {}
        word_to_char = {}

        for ch,wr in zip(pattern, word):
            if ch in char_to_word and char_to_word[ch] !=wr:
                return False 
            if wr in word_to_char and word_to_char[wr] != ch:
                return False
            char_to_word[ch] = wr
            word_to_char[wr] = ch
        return True

        
