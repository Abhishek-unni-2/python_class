a=["stars","moon","escalate"]
count=0
if len(a)>1:
  for i in a:
    if i[0]==i[-1]:
      count+=1
    else:
      continue
print("the count:",count)