#Remove Duplicates from List using Recursion
def Dupli(s,out=[],i=0):
    if i>=len(s):
        return out
    if s[i] not in out:
        out.append(s[i])
    return Dupli(s,out,i+1)
print(Dupli(eval(input("enter your list:"))))
