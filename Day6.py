class Solution:
    # @param A : integer
    # @return a list of strings
    def getRow(self, A):
      if A == 0:
            return [1]
        elif A == 1:
            return [1, 1]
        else:
            prev_row = self.get_pascal_row(A - 1)
            current_row = [1]
            for i in range(1, A):
                current_row.append(prev_row[i - 1] + prev_row[i])
            current_row.append(1)
            return current_row
      
