# find the best way to create the target number form a given array
# for example: [2,3,5], 8, output [3,5]
def bestSum_TD(arr, target):
	if target < 0:
		return # do nothing
	if target == 0:
		return [] # empty arr to store current combo
	bestCombo = None
	for e in arr: # traver all element in arr
		remain = target-e # the current remain
		combo = bestSum_TD(arr, remain) # [2,2,2] if remain = 6
		if combo != None: # 6 != None
			combo_copy = combo[:] # make copy of combo, which is immutable
			combo_copy.append(e) # add current element (2 is this case)
			if bestCombo == None or len(combo_copy) < len(bestCombo): 
				bestCombo = combo_copy # assign new bestCombo
				# print(bestCombo)
	return bestCombo
	
def bestSum_BU(candidates, target):
    dp = [[] for i in range(target+1)]
    for c in candidates:
        for i in range(target+1):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])
            else:
                for l in dp[i-c]:
                    dp[i].append([c] + l)
    lenList = []
    for i,e in enumerate(dp[target]):
    	lenList.append(len(e))
    m = min(lenList)	
    r = lenList.index(m)
    return dp[target][r]

a = bestSum_BU([2,3,5], 8)    	
print(a)