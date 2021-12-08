## show all possibilities how to create target number from provided arr with
## no duplicate
## For example: [2,3,5], 8 should return [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
## I used backtracking method
def targetSum_BT(arr, target , indx = 0, curTrack = [], combos = []):
	# curTrack to keep track the current combination
	# in this case is [2],[2,2],[2,2,2],[2,2,2,2] in first index
	if target < 0:
		return	# do nothing
	if target == 0:
		combos.append(curTrack[:]) # copy the curTrack and put into combos
		return # the curent
	if indx < len(arr): # traver the elements in arr
		value = arr[indx] # the element will be added into curTrack
		curTrack.append(value) # add current element into curTrack
		targetSum_BT(arr, target - value, indx, curTrack, combos)
		curTrack.pop() # move to next element once done with curent one 
		targetSum_BT(arr, target, indx+1, curTrack, combos)

	return combos
	
## use bottom up for this problem
# 	0		1				2			3				4				5
# 1	[]		[[1]]		[[1,1]]		[[1,1,1]]		[1,1,1,1]		[1,1,1,1,1]
# 2	[]		[[1]]	[[1,1], [2]]	[[1,1,1], 		[[1,1,1,1], 	[[1,1,1,1,1], 
# 									[2,1]]			[2,1,1],		[2,1,1,1],
# 													[2,2]]			[2,2,1],
# 3	[]		[[1]]	[[1,1], [2]]	[[1,1,1], 		[[1,1,1,1],		[3,1,1], [3,2]]
# 									[2,1], [3]]		[2,1,1],	
# 													[2,2], [3,1]]		 
													
# ex [1,2,3], 5						
def targetSum_BU(candidates, target):
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
    return dp[target] 	
a = targetSum_BU([1,2,3], 5)    	
print(a)

# recap: both way make no duplicate, but BU is fater than BT
		
	

			
