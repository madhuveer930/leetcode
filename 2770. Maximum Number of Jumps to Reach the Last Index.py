@cache
def dfs(i):
    if i==0: return 0
    ans=-inf
    for j in range(i):
        if abs(nums[j]-nums[i])<=target:
            ans=max(ans, 1+dfs(j))
    return ans
        
