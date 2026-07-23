class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops=['+','-','*','/']
        for item in tokens:
            if(item in ops):
                a=int(stack.pop())
                b=int(stack.pop())
                if(item=='+'):
                    stack.append(str(b+a))
                elif(item=='-'):
                    stack.append(str(b-a))
                elif(item=='*'):
                    stack.append(str(b*a))
                elif(item=='/'):
                    stack.append(str(int(b/a)))
            else:
                stack.append(item)
            
        return int(stack[-1])