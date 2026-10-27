#duplicate element in array
'''

#use floyds slow fast pointer, and linked list as index->value
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=nums[0],nums[0]
        k=True
        while(k):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                k=False
        slow=nums[0]
        while(slow!=fast):
            slow=nums[slow]
            fast=nums[fast]

        return slow
        
'''
#median from input stream
"""
Brute force-unoptimised

class MedianFinder:

    def __init__(self):
        self.l=[]

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()
    def findMedian(self) -> float:
        n=len(self.l)
        if n%2==0:
            return (self.l[int(n/2)-1]+self.l[int(n/2)])/2
        else:
            return self.l[n//2]
"""
#kth largest element in a stream
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap)>k:
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        



"""
#maximum product subarray
"""
def maxProduct(self, nums: List[int]) -> int:
        minprod,maxprod=1,1
        ans=nums[0]
        for x in nums:
            newmin=min(x,x*minprod,x*maxprod)
            newmax=max(x,x*minprod,x*maxprod)

            
            maxprod=newmax
            minprod=newmin
            ans=max(ans,maxprod)
        return ans
        
"""

#Tak scheduler code in c++
"""
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector <int> freq(26,0);

        for(char c:tasks){
            freq[c-'A']++;
        }

        int maxfreq= *max_element(freq.begin(),freq.end());
        int count=0;

        for (int fre:freq){
            if (fre==maxfreq){
                count++;
            }
        } 

        return max((int)tasks.size(),(maxfreq-1)*(n+1) + count);
        
    }
};
"""