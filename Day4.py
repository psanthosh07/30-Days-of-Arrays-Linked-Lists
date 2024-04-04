class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        a=0
        for i in range(n-1):
            if A[i]%2== A[i+1]%2:
                a+=1
        
        return n-a
