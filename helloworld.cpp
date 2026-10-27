#include<bits/stdc++.h>
using namespace std;


int kthlargest(vector<int> &nums,int k){
    priority_queue<int,vector<int>,greater<int>> minHeap;
    
    for(int num:nums){
        minHeap.push(num);
        if(minHeap.size()>k){
            minHeap.pop();
        }
    }return minHeap.top();
}

int main(){
    vector <int> nums={3,2,1,4,5};
    int k=2;
    cout<<kthlargest(nums,k);}