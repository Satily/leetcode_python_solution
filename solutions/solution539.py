class Solution:
    def findMinDifference(self, timePoints: 'List[str]') -> int:
        def to_minutes(time_point):            
            t = list(map(lambda x: int(x), time_point.split(':', 1)))
            return t[0] * 60 + t[1]                
        
        time_points_minutes = list(sorted(map(to_minutes, timePoints)))
        time_points_minutes.append(time_points_minutes[0] + 24 * 60)
        
        result = 24 * 60 + 1
        for index in range(len(time_points_minutes) - 1):
            result = min(result, time_points_minutes[index + 1] - time_points_minutes[index])
        return result

if __name__ == "__main__":
    print(Solution().findMinDifference(["23:59","00:00"]))