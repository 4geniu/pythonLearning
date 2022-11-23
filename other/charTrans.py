transNumber = 3

apper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

entered = input()
for c in entered:
    if c in apper:
      print(apper[apper.find(c)-transNumber],end="")
    elif c in lower:
       print(lower[lower.find(c)-transNumber],end="")
    else:
       print(c,end="")