#Longest increasing subsequence
"""
def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
"""
#climbing stairs with cost, i to i+1,i+2,i+3
"""
def climbStairs(self, n: int, cost: List[int]) -> int:
        dp=[0]*(n+1)
        dp[0]=0
        
        dp[1]=cost[0]+1
            
        if n>=2:
            dp[2]=min(cost[1]+dp[0]+4,cost[1]+dp[1]+1)

        for i in range(3,n+1):
            
           
            
            dp[i]=min(cost[i-1]+dp[i-3]+9,cost[i-1]+dp[i-2]+4,cost[i-1]+dp[i-1]+1)

        print(len(cost),cost[0])
        return dp[-1]
"""
#Maximum subarray
"""
def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        ans=nums[0]
        i,n=1,len(nums)-1
        if n==0:
            return nums[0]
        dp[0]=nums[0]    
        while(i<=n):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
            ans=max(ans,dp[i])
            i+=1
        return ans
"""
"""
def maximumsubarray(nums):
        n=len(nums)-1
        dp=[0]*(n+1)
        dp[0]=nums[0]
        if n==0:
            return nums[0]
        i=1
        ans=nums[0]
        while (i<=n):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
            ans=max(ans,dp[i])
            i+=1
        return ans


"""
###LWK HARDEST PROBLEM
"""# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float("-inf")

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            # Maximum gain from left/right subtree
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Best path passing through current node
            ans = max(ans, node.val + left + right)

            # Return best one-sided path to parent
            return node.val + max(left, right)

        dfs(root)
        return ans"""

#equal partition subset
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        if sum1%2!=0:
            return False
        @lru_cache(None)
        def dfs(i,total):
            if i>=len(nums) or total>sum1//2:
                return False
            if total==sum1//2:
                return True
            
            return dfs(i+1,total+nums[i]) or dfs(i+1,total)
        
        return dfs(0,0)"""

#expression adding to target
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i,total):
            if i==len(nums):
                return 1 if total==target else 0
            return dfs(i+1,total+nums[i])+dfs(i+1,total-nums[i])

        return dfs(0,0)
"""
#minimum path sum in 2d matrix
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        dp=[[0]*n for i in range(m)]
        dp[0][0]=grid[0][0]

        for i in range(1,n):
            dp[0][i]=dp[0][i-1]+grid[0][i]

        for j in range(1,m):
            dp[j][0]=dp[j-1][0]+grid[j][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])

        return dp[m-1][n-1]

"""
#house robber adjacent houses cannot steal
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=nums.copy()
        if len(nums)==1:
            return nums[0]
        dp[1]=max(dp[0],dp[1])
        for i in range(2,len(nums)):
            
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])


        return dp[-1]
        """