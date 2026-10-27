#min stack
"""

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack)==1:
            self.minstack.append(val)

        elif self.minstack[-1]<val:
            self.minstack.append(self.minstack[-1])
        else:
            self.minstack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

"""
#car fleet
"""
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=sorted(zip(position,speed),reverse=True)
        for pos,speed in cars:
            time=(target-pos)/speed
            if not stack or time>stack[-1]:
                stack.append(time)
            
        return len(stack)
"""
#implementing stacks using 2 queues
"""
class MyStack:

    def __init__(self):
        self.q1=dequeue()
        self.q2=dequeue()        

    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q2,self.q1=self.q1,self.q2
        

    def pop(self) -> int:
        return self.q1.popleft()
        

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1)==0
        
THE TRICK IS EVERYTIME, A NEW ELEMENT IS PUSHED ITS ADDED TO Q2 WHICH IS INITIALLY ALWAYS A EMPTY ONE AND THEN 
CONTENTS OF Q1 PUSHED TO Q2, MAKING IT REVERSE ORDER, FINALLY Q1 N Q2 SWAPPED


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""

#queue using 2 stacks
"""
class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        self.inStack.append(x)

    def pop(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()

    def peek(self) -> int:
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self) -> bool:
        return not self.inStack and not self.outStack
"""