def solution(){
  A.sort(reverse=True)
  l=[]
  count=1
  for i in l:
    if i not in l:
      l.append(i)
    else:
      count+=1
    if(count==len(A)){
      return 0
    }
    n=l[1:]
    return max(n)
