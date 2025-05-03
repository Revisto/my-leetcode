class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        if len(intervals) <= 1:
            return intervals
        start = intervals[0][0]
        output_intervals = list()
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] > end:
                output_intervals.append([start, end])
                start = interval[0]
            end = max(end, interval[1])
        if [start, end] not in output_intervals:
            output_intervals.append([start, end])
        return output_intervals

print(Solution().merge([[1,4],[2,3]]))