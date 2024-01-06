from _bisect import bisect_right
from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(endTime, startTime, profit))

    number_of_jobs = len(profit)

    dp = [0] * (number_of_jobs + 1)

    for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
        index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
        dp[i + 1] = max(dp[i], dp[index] + current_profit)

    print(dp[number_of_jobs])
    return dp[number_of_jobs]

if __name__ == '__main__':
    jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
    jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
    jobScheduling([1,1,1], [2,3,4], [5,6,4])
