from typing import List


def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)
    dp = [0] * n

    for i in range(n):
        dp[i] = jobs[i][2]  # Initialize with the profit of the current job

    for i in range(1, n):
        for j in range(i):
            if jobs[i][0] >= jobs[j][1]:
                dp[i] = max(dp[i], dp[j] + jobs[i][2])

    return max(dp)

if __name__ == '__main__':
    result = jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
    print(result)
