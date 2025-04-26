class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        prev_end = intervals[0][1]
        remove_count = 0
        for interval in intervals[1:]:
            start, end = interval
            
            if prev_end > start:
                remove_count += 1
            
            else:
                prev_end = end
        
        return remove_count