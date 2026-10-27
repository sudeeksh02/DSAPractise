#rotating array by 90 degree
"""
def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(n):
            left=0
            right=n-1
            while(left<=right):
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1
        
"""
#set col,row of zero elements to zero
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #check for rows
        m=len(matrix)
        n=len(matrix[0])

        row,col=0,0
        for i in range(n):
            if matrix[0][i]==0:
                row=1
        for j in range(m):
            if matrix[j][0]==0:
                col=1


        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0],matrix[0][j]=0,0

        for i in range(1,n):
            if matrix[0][i]==0:
                j=1
                while j<m:
                    matrix[j][i]=0
                    j+=1
        for i in range(1,m):
            if matrix[i][0]==0:
                j=1
                while j<n:
                    matrix[i][j]=0
                    j+=1
        if row:
            for i in range(n):
                matrix[0][i]=0
        if col:
            for i in range(m):
                matrix[i][0]=0

        
"""
#array num+1
"""
def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        digits[len(digits)-1]+=1
        for i in range(len(digits)-1,-1,-1):
            total=digits[i]+carry
            digits[i]=total%10
            carry=total//10
        if carry:
            digits.insert(0,carry)
        return digits
   
"""
#largest number
"""
 def compare(self,a,b):
        if a+b<b+a:
            return 1
        else:
            return -1
        return 0
    
    
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        nums.sort(key=cmp_to_key(self.compare))
        ans="".join(nums)
        return '0' if ans[0]=='0' else ans
        
"""
#maximum product by incrementing 1 k times
"""
ef maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=len(nums)
        i=0
    
        while k:
            
            small=heapq.heappop(nums)
            small+=1                             #take smallest element pop increment by 1 push it
            heapq.heappush(nums,small)
            k-=1
        
        prod=1
        for num in nums:
            prod=(prod*num)%(pow(10,9)+7)
        return prod

"""