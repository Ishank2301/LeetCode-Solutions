# Last updated: 27/10/2026, 9:02:46 pm
class Solution:
    def calculate(self, s):
        stack=[]; num=0; op='+'
        for c in s+'+':
            if c.isdigit(): num=num*10+int(c)
            elif c in '+-*/':
                if op=='+': stack.append(num)
                elif op=='-': stack.append(-num)
                elif op=='*': stack.append(stack.pop()*num)
                elif op=='/': stack.append(int(stack.pop()/num))
                op=c; num=0
        return sum(stack)