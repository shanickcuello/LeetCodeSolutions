def climb_stairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]




if __name__ == '__main__':
    print(climb_stairs(2))
    print(climb_stairs(3))
    print(climb_stairs(4))
    print(climb_stairs(5))
    print(climb_stairs(6))
    print(climb_stairs(7))
    print(climb_stairs(8))
    print(climb_stairs(9))
    #fibonacci! eureka! ;)