#same binary tree
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1,root2):
            if not root1 and not root2:
                return True
            
            if (root1 and root2) and root1.val==root2.val:
                
            
                return dfs(root1.left,root2.left) and dfs(root1.right,root2.right)
            else:
                return False
        return dfs(p,q)
'''
#bst tree iterator-inorder
"""
 def __init__(self, root: Optional[TreeNode]):
        self.l=[]
        self.i=0
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.l.append(root.val)
            inorder(root.right)
        inorder(root)
        self.sz=len(self.l)

    def next(self) -> int:
        self.i+=1
        return self.l[self.i-1]
        

    def hasNext(self) -> bool:
        if self.i<self.sz:
            return True
        else:
            return False
        
"""
#inorder successor
"""class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        succ = None

        while root:
            if root.val > p.val:
                succ = root
                root = root.left
            else:
                root = root.right

        return succ"""

#delete node in bst
"""
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            succ=root.right
            while succ.left:
                succ=succ.left
            root.val=succ.val
            root.right=self.deleteNode(root.right,succ.val)
        return root
"""
#level order search
"""
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result=[]
        queue=deque([root])

        while queue:
            lists=[]
            for i in range(len(queue)):
                node=queue.popleft()
                lists.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(lists)
        return result
"""
#Count good nodes in binary tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good=0
        
        max=root.val

        def dfs(root,max):
            nonlocal good
            if not root:
                return
            if root.val>max:
                max=root.val
                good+=1
            dfs(root.left,max)
            dfs(root.right,max)
        dfs(root,max)
        return good
"""
def findRelativeRanks(shata: List[int]):
        if not shata:
            return []
        score=shata.copy()
        score.sort(reverse=True)
        
        map={}
        n=len(score)
        if n==3:
            score[0],score[1],score[2]="Gold Medal","Silver Medal","Bronze Medal"
            return score
        elif n==2:
            score[0],score[1]="Gold Medal","Silver Medal"
            return score
        elif n==1:
            score[0]=="Gold Medal"
            return score
        elif n>3:
            map[score[0]],map[score[1]],map[score[2]]="Gold Medal","Silver Medal","Bronze Medal"
        
            for i in range(3,len(score)):

                map[score[i]]=str(i+1)

        for i in range(len(shata)):
            shata[i]=map[shata[i]]


        return shata


print(findRelativeRanks([1]))