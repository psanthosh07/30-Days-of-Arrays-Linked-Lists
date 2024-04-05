class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
      b=A[0]
	maxp = 0
	for i in range(1, len(A):
		if (b > A[i]):
			b = A[i]
		elif (A[i] - b > maxp):
			maxp = A[i] - b
	return maxp
