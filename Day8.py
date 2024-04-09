class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        l=len(A)
        dp=[0]* l
        
        dp[0]=A[0]
        
        ans=dp[0]
        
        for i in range(1,l):
            dp[i]=max(A[i],A[i]+dp[i-1])
            
            ans=max(ans,dp[i])
            
        return ans
