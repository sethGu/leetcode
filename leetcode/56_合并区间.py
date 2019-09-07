class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i, res = 0, []
        while i < len(intervals) - 1:
            i += 1
            if max(intervals[i - 1]) >= min(intervals[i]):
                if max(intervals[i - 1]) >= max(intervals[i]):
                    intervals.remove(intervals[i])
                else:
                    intervals[i] = [min(intervals[i - 1]), max(intervals[i])]
                    intervals.remove(intervals[i - 1])
                # 重置i为-1，很关键
                i-=1
        return intervals
