#first check

"""def check_balanced(expri):
    stack=[]
    char_exp=["(","[","{"]
    for i in expri:
        if i in char_exp:
            stack.append(i)
        else:
            if not stack:
                return False
            char1=stack.pop()
            if char1!=')':
                return False
            if char1!=']':
                return False
            if char1!='}':
                return False
    if stack:
        return False
    else:
        return True

expri="{()}"
obj=check_balanced(expri)
print(obj)
"""

def check_balanced(expri):
    stack=[]
    char_expr=["[","{","("]
    closing_expr=["]","}",")"]
    for i in expri:
        if i in char_expr:
            stack.append(i)
        else:
            if not stack:
                return "not balanced"
            char1=stack.pop()
            if char_expr.index(char1)!=closing_expr.index(i):
                return "not balanced"
    if stack:
        return "not balanced"
    else:
        return "balanced"

expri="{()}"
obj=check_balanced(expri)
print(obj)
