class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        answer = []
        small = collections.Counter()
        for y in changed:
            if y % 2 == 0 and y // 2  in small and small[y // 2] > 0:
                answer.append( y // 2)
                small[ y //2 ] -= 1
            else:
                small[y] += 1
        if len(answer) * 2 != len(changed):
            return []
        return answer 
