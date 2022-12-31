class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        sentence = s.split(" ")
        sentence_sort = ""
        for i in range(len(sentence)):
            min_va= i
            for j in range(i+1,len(sentence)):
                if sentence[j][-1] < sentence[min_va][-1]:
                    min_va = j
            if i != min_va:
                sentence[min_va],sentence[i] = sentence[i] ,sentence[min_va]
            sentence_sort += sentence[i][:-1] + " "
        return (sentence_sort[:-1])
