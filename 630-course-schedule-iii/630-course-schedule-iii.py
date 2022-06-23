class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort by Last Day Time
        courses.sort(key=lambda x: x[1])
        arr = []
        total_time = 0
        for dur, last_time in courses:
            # Creating Max-Heap
            heappush(arr, -dur)
            total_time += dur
            if total_time > last_time:
                # Pop max course duration and remove that
                val = heappop(arr)
                total_time += val
        return len(arr)