class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A=list(A)
        l=len(A)
        r=[]
        for i in range(l):
            if A[abs(A[i])-1]>0:
                A[abs(A[i])-1]= -A[abs(A[i])-1]
            else:
                r.append(abs(A[i]))
        for i in range(l):
            if A[i]>0:
                r.append(i+1)
        return r
