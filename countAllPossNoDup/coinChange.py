## apply for coin change problem
# find the min number of coin to change a certain amount
# this have no duplicate
def coinChange(scoins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    for c in coins:
        for i in range(1, amount+1):
            if i >= c:
                dp[i] = min(dp[i], dp[i-c] + 1)
    if dp[amount] == (amount+1):
        return -1
    return dp[amount]

# coinChange2 show the number of possibilities of way to change coins
def change(amount, coins):
    dp = [0] * (amount+1)
    dp[0] = 1
    for c in coins:
        for i in range(amount+1):
            if i >= c:
                dp[i] += dp[i-c]
    return dp[amount] 

a = change(5, [1,2,5])
print(a)