def lenBesSum(arr, target):
	dp = [target+1]*(target+1)
	dp[0] = 0
	for e in arr:
		for i in range(1,target+1):
			if i < e:
				continue
			if i == e:
				dp[i] = 1
			else:
				dp[i] = 1 + dp[i-e]		
	return dp[target]
	
a = lenBesSum([2,3,5], 8)				
print(a)