class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count=0
        for i in A:
            if i%2==0:
                count+=1
        return min(count,len(A)-count)
