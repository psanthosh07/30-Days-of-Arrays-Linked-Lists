class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    stack=[]
	    n=len(A)
	    ans=0
	    for i in range(n):
	        while(len(stack)!=0 and (A[stack[-1]]<A[i])):
	            pop_height=A[stack[-1]]
	            stack.pop()
	            
	            if(len(stack)==0):
	                break
	            distance=i-stack[-1]-1
	            min_height=min(A[stack[-1]],A[i])-pop_height
	            ans+=distance*min_height
            stack.append(i)
        return ans
	                
	    
