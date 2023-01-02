class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        result = [intervals[0]]

        for s, e in intervals[1:]:
            recentEnd = result[-1][1]

            if s <= recentEnd :
                result[-1][1] = max(recentEnd, e)
            else:
                result.append([s,e])
        return result
        
