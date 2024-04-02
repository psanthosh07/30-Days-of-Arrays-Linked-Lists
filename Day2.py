class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count=0
        for i in range(len(A)):
            s,g=False,False
            for j in range(len(A)):
                if i!=j:
                    if A[j]<A[i]:
                        s=True
                    elif A[j]>A[i]:
                        g=True
            if s and g:
                    count+=1
        return count
