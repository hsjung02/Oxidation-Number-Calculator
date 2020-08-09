mat=[]
temp=''
count=0
for j in range(0,len(i)):
    for i[j].isupper():
        if temp!='':
            mat.append(temp)
            mat.append(count)
        temp=i[j]
        count=1
    elif i[j].islower():
        temp+=i[j]
    elif i[j].isdigit():
        if i[j+1].isdigit():
            count=10*i[j]
        else:
            count=i[j]



mat=[]
temp=''
count=0
for j in range(len(i)):
    if i[j].isupper():
        if temp!='':
            mat.append(temp)
            mat.append(count)
        ele=i[j]
        count=1
    if i[j].islower():
        ele+=i[j]
    if i[j].isdigit():
        if i[j-1].isdigit():
            count=int(str(count)+i[j])
        else:
            count=int(i[j])
mat.append(temp)
mat.append(count)