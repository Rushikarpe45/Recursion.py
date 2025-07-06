#TO EXTRACT INT WHICH ARE MULTIPLE OF 5 AND 3 using recursion
def rushi(s,out=[],i=0):
    if i>=len(s):
        return out
    if type(s[i])==int:
        if s[i]%5==0 or s[i]%3==0:
            out.append(s[i])
    return rushi(s,out,i+1)
print(rushi(eval(input("enter your list:"))))
