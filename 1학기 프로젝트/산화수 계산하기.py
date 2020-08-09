# -*- coding: utf-8 -*-
#화학 반응식을 입력받았을 때 특정 원소의 산화수 변화를 통해 산화/환원 여부를 알려 줌
#입력 예시_반응물:2S2O3(-2)+I2(0), 생성물:S4O6(-2)+2I(-1), O

print('='*50)
print('즐거운 산화 환원')
print('='*50)
sub=input('반응물 입력')
pro=input('생성물 입력')
A=input('어떤 원소를 알고 싶나요?')
substrate=sub.split('+')
product=pro.split('+')
befmat=[]
afmat=[]
before=[]
after=[]
mat=[]
temp=''
count=0
b=''
for i in substrate:
    if A in i: #필요한지 필요없는지
        pass
    else:
        continue
    if i[-2]==0: #전하량 검출
        mat.append(0)
        i=i[:-3]
    elif i[-2]!=0 and i[-3]=='(':
        mat.append(int(i[-2]))
        i=i[:-3]
    else:
        mat.append(int(i[-3:-1]))
        i=i[:-4]
    if i[0].isdigit():  #계수는 필요없으니까 제거
        if i[1].isdigit():
            i=i[2:]
        else:
            i=i[1:]
    for k in range(i.count('(')):   #원자단(괄호) 처리
        for j in range(i.index('(')+1,i.index(')')):
            if j==(i.index('(')+1):
                b=i[:i.index('(')]+i[i.index('(')+1]
            elif j==(i.index(')')-1):
                if i[j].islower():
                    b+=i[j]
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                elif i[j].isdigit():
                    if i[j-1].isalpha():
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=str(int(i[j])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                            elif not i[i.index(')')+2].isdigit():
                                b+=str(int(i[j])*int(i[i.index(')')+1]))
                        except IndexError:
                            b+=str(int(i[j])*int(i[i.index(')')+1]))
                            pass
                    else:
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=str(int(i[(j-1):(j+1)])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                            elif not i[i.index(')')+2].isdigit():
                                b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                        except IndexError:
                            b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                            pass
                elif i[j].isupper():
                    if i[j-1].isalpha():
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=i[(i.index(')')+1):(i.index(')')+3)]
                            elif not i[i.index(')')+2].isdigit():
                                b+=i[i.index(')')+1]
                        except IndexError:
                            b+=i[i.index(')')+1]
                            pass
                    b+=i[j]
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                try:
                    if i[i.index(')')+2].isdigit():
                        b+=i[(i.index(')')+3):]
                    elif not i[i.index(')')+2].isdigit():
                        b+=i[(i.index(')')+2):]
                except IndexError:
                    pass
            elif i[j].isupper():
                if i[j-1].isdigit():
                    b+=i[j]
                else:
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                    b+=i[j]
            elif i[j].islower():
                b+=i[j]
            elif i[j].isdigit():
                if i[j+1].isdigit():
                    continue
                elif i[j-1].isalpha():
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=str(int(i[j])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                        elif not i[i.index(')')+2].isdigit():
                            b+=str(int(i[j])*int(i[i.index(')')+1]))
                    except IndexError:
                        b+=str(int(i[j])*int(i[i.index(')')+1]))
                        pass
                elif i[j-1].isdigit():
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=str(int(i[(j-1):(j+1)])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                        elif not i[i.index(')')+2].isdigit():
                            b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                    except IndexError:
                        b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                        pass
        i=b
        b=''
    befmat.append(i)  #출력을 위해서
    for j in range(len(i)): #원소 종류, 개수 분리
        if i[j].isupper():
            if temp!='':
                mat.append(temp)
                mat.append(count)
            temp=i[j]
            count=1
        if i[j].islower():
            temp+=i[j]
        if i[j].isdigit():
            if i[j-1].isdigit():
                count=int(str(count)+i[j])
            else:
                count=int(i[j])
    mat.append(temp)
    mat.append(count)
    before.append(mat)
    mat=[]
    temp=''
for i in product:  #생성물에서도 똑같은 작업
    if A in i:
        pass
    else:
        continue
    if i[-2]==0:
        mat.append(0)
        i=i[:-3]
    elif i[-2]!=0 and i[-3]=='(':
        mat.append(int(i[-2]))
        i=i[:-3]
    else:
        mat.append(int(i[-3:-1]))
        i=i[:-4]
    if i[0].isdigit():
        if i[1].isdigit():
            i=i[2:]
        else:
            i=i[1:]
    for k in range(i.count('(')):
        for j in range(a.index('(')+1,i.index(')')):
            if j==(i.index('(')+1):
                b=i[:i.index('(')]+i[i.index('(')+1]
            elif j==(i.index(')')-1):
                if i[j].islower():
                    b+=i[j]
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                elif i[j].isdigit():
                    if i[j-1].isalpha():
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=str(int(i[j])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                            elif not i[i.index(')')+2].isdigit():
                                b+=str(int(i[j])*int(i[i.index(')')+1]))
                        except IndexError:
                            b+=str(int(i[j])*int(i[i.index(')')+1]))
                            pass
                    else:
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=str(int(i[(j-1):(j+1)])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                            elif not i[i.index(')')+2].isdigit():
                                b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                        except IndexError:
                            b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                            pass
                elif i[j].isupper():
                    if i[j-1].isalpha():
                        try:
                            if i[i.index(')')+2].isdigit():
                                b+=i[(i.index(')')+1):(i.index(')')+3)]
                            elif not i[i.index(')')+2].isdigit():
                                b+=i[i.index(')')+1]
                        except IndexError:
                            b+=i[i.index(')')+1]
                            pass
                    b+=i[j]
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                try:
                    if i[i.index(')')+2].isdigit():
                        b+=i[(i.index(')')+3):]
                    elif not i[i.index(')')+2].isdigit():
                        b+=i[(i.index(')')+2):]
                except IndexError:
                    pass
            elif i[j].isupper():
                if i[j-1].isdigit():
                    b+=i[j]
                else:
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=i[(i.index(')')+1):(i.index(')')+3)]
                        elif not i[i.index(')')+2].isdigit():
                            b+=i[i.index(')')+1]
                    except IndexError:
                        b+=i[i.index(')')+1]
                        pass
                    b+=i[j]
            elif i[j].islower():
                b+=i[j]
            elif i[j].isdigit():
                if i[j+1].isdigit():
                    continue
                elif i[j-1].isalpha():
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=str(int(i[j])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                        elif not i[i.index(')')+2].isdigit():
                            b+=str(int(i[j])*int(i[i.index(')')+1]))
                    except IndexError:
                        b+=str(int(i[j])*int(i[i.index(')')+1]))
                        pass
                elif i[j-1].isdigit():
                    try:
                        if i[i.index(')')+2].isdigit():
                            b+=str(int(i[(j-1):(j+1)])*int(i[(i.index(')')+1):(i.index(')')+3)]))
                        elif not i[i.index(')')+2].isdigit():
                            b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                    except IndexError:
                        b+=str(int(i[(j-1):(j+1)])*int(i[i.index(')')+1]))
                        pass
        i=b
        b=''
    afmat.append(i)
    for j in range(len(i)):
        if i[j].isupper():
            if temp!='':
                mat.append(temp)
                mat.append(count)
            temp=i[j]
            count=1
        if i[j].islower():
            temp+=i[j]
        if i[j].isdigit():
            if i[j-1].isdigit():
                count=int(str(count)+i[j])
            else:
                count=int(i[j])
    mat.append(temp)
    mat.append(count)
    after.append(mat)
    mat=[]
    temp=''

alkali_metal=['Li','Na','K','Rb','Cs','Fr']   #데이터베이스
alkaline_earth_metal=['Be','Mg','Ca','Sr','Ba','Ra']
halogen=['Cl','Br','I']
befsan=[]
afsan=[]
san=[]

def ele(a,b):     #멤버체크 in을 이용해서 공통원소 리턴하는 함수
    for p in a:
        if p in b:
            return p
        else:
            return False
def exc(a,b,c):     #산화수 규칙 분기문에서 예외 처리할 수 있게 만든 함수 ex)NaH
    for p in a:
        if (p+b) in c:
            return b
        else:
            return False
def sigma(a,b):     #따로 규칙이 정해지지 않은 원소의 산화수를 계산하기 위해 만든 함수
    count=0         #모르는 원소 빼고 나머지 원소들의 (산화수)*(개수)의 총합을 리턴함
    for j in range(len(a)):
        count+=a[j]*float(b[2*j+2])
    return count

for i in before:      #산화수 결정
    if len(i)==3 and i[0]==0:  #이원자분자/단원자분자 처리
        san.append(0.0)
        befsan.append(san)
        san=[]
    else:
        for k in range((len(i)-1)//2):   #원소 종류만큼 산화수 리스트에 0추가
            san.append(0.0)
        if 'F' in i:                     #산화수 규칙을 분기문으로 표현
            san[(i.index('F')-1)//2]=-1.0
        if ele(alkali_metal, i):
            san[(i.index('ele(alkali_metal, i)')-1)//2]=1.0
        if ele(alkaline_earth_metal,i):
            san[(i.index('ele(alkaline_earth_metal, i)')-1)//2]=2.0
        if 'H' in i:
            if exc(alkali_metal,'H',substrate) or 'BH3' in sub:
                san[(i.index('H')-1)//2]=-1.0
            else:
                san[(i.index('H')-1)//2]=1.0
        if 'O' in i:
            if 'H2O2' in sub:
                san[(i.index('O')-1)//2]=-1.0
            elif 'OF2' in sub:
                san[(i.index('O')-1)//2]=2.0
            elif 'O2F2' in sub:
                san[(i.index('O')-1)//2]=1.0
            else:
                san[(i.index('O')-1)//2]=-2.0
        if ele(halogen,i):
            san[(i.index('ele(halogen, i)')-1)//2]=-1.0
        if 0 in san:                                     #모르는 원소 처리
            san[san.index(0)]=(i[0]-sigma(san,i))/i[2*(san.index(0))+2]
        befsan.append(san)
        san=[]
for i in after:            #생성물에도 똑같은 작업
    if len(i)==3 and i[0]==0:
            san.append(0.0)
            afsan.append(san)
            san=[]
    else:
        for k in range((len(i)-1)//2):
            san.append(0.0)
        if 'F' in i:
            san[(i.index('F')-1)//2]=-1.0
        if ele(alkali_metal, i):
            san[(i.index('ele(alkali_metal, i)')-1)//2]=1.0
        if ele(alkaline_earth_metal,i):
            san[(i.index('ele(alkaline_earth_metal, i)')-1)//2]=2.0
        if 'H' in i:
            if exc(alkali_metal,'H',substrate) or 'BH3' in pro:
                san[(i.index('H')-1)//2]=-1.0
            else:
                san[(i.index('H')-1)//2]=1.0
        if 'O' in i:
            if 'H2O2' in pro:
                san[(i.index('O')-1)//2]=-1.0
            elif 'OF2' in pro:
                san[(i.index('O')-1)//2]=2.0
            elif 'O2F2' in pro:
                san[(i.index('O')-1)//2]=1.0
            else:
                san[(i.index('O')-1)//2]=-2.0
        if ele(halogen,i):
            san[(i.index('ele(halogen, i)')-1)//2]=-1.0
        if 0 in san:
            san[san.index(0)]=(i[0]-sigma(san,i))/i[2*(san.index(0))+2]
        afsan.append(san)
        san=[]

def sanhwan(a,b,c,d,e,f,g):      #결과 출력하는 함수. 반응물 1개, 생성물 여러개이거나 반응물 여러개, 생성물 1개일 때 포맷 이용해서 문장 여러개 출력함
    if len(b)==1 and len(d)!=1:#a=befsan, ,b=before c=afsan, d=after, e=A, f=befmat, g=afmat
        for i in range(len(d)):         #a[0][(b[0].index(e)-1)//2] 이렇게 되어 있는 것은 산화수를 나타내는 숫자들.
            if a[0][(b[0].index(e)-1)//2]==c[i][(d[i].index(e)-1)//2]:
                print(e,'은(는) %s 로 될 때 산화되지도 환원되지도 않음'%g[i],'(산화수:',a[0][(b[0].index(e)-1)//2],'->','%s'%c[i][(d[i].index(e)-1)//2],')',end='\n')
            elif a[0][(b[0].index(e)-1)//2]<c[i][(d[i].index(e)-1)//2]:
                print(e,'은(는) %s 로 될 때 산화됨'%g[i],'(산화수:',a[0][(b[0].index(e)-1)//2],'->','%s'%c[i][(d[i].index(e)-1)//2],')',end='\n')
            elif a[0][(b[0].index(e)-1)//2]>c[i][(d[i].index(e)-1)//2]:
                print(e,'은(는) %s 로 될 때 환원됨'%g[i],'(산화수:',a[0][(b[0].index(e)-1)//2],'->','%s'%c[i][(d[i].index(e)-1)//2],')',end='\n')
    elif len(b)!=1 and len(d)==1:
        for i in range(len(b)):
            if c[0][(d[0].index(e)-1)//2]==a[i][(b[i].index(e)-1)//2]:
                print(e,'은(는) %s 가 반응할 때 산화되지도 환원되지도 않음'%f[i],'(산화수:',c[0][(d[0].index(e)-1)//2],'->','%s'%a[i][(b[i].index(e)-1)//2],')',end='\n')
            elif c[0][(d[0].index(e)-1)//2]>a[i][(b[i].index(e)-1)//2]:
                print(e,'은(는) %s 가 반응할 때 산화됨'%f[i],'(산화수:','%s'%a[i][(b[i].index(e)-1)//2],'->',c[0][(d[0].index(e)-1)//2],')',end='\n')
            elif c[0][(d[0].index(e)-1)//2]<a[i][(b[i].index(e)-1)//2]:
                print(e,'은(는) %s 가 반응할 때 환원됨'%f[i],'(산화수:','%s'%a[i][(b[i].index(e)-1)//2],'->',c[0][(d[0].index(e)-1)//2],')',end='\n')
    else:             #반응물 여러개, 생성물 여러개일때
        print('부적절 입력')

if len(before)*len(after)==1:  #반응물 1개, 생성물 1개일때
    if befsan[0][(before[0].index(A)-1)//2]==afsan[0][(after[0].index(A)-1)//2]:
        print(A,'은(는) 산화되지도 환원되지도 않음','(산화수:',befsan[0][(before[0].index(A)-1)//2],'->',afsan[0][(after[0].index(A)-1)//2],')')
    elif befsan[0][(before[0].index(A)-1)//2]<afsan[0][(after[0].index(A)-1)//2]:
        print(A,'은(는) 산화됨','(산화수:',befsan[0][(before[0].index(A)-1)//2],'->',afsan[0][(after[0].index(A)-1)//2],')')
    elif befsan[0][(before[0].index(A)-1)//2]>afsan[0][(after[0].index(A)-1)//2]:
        print(A,'은(는) 환원됨','(산화수:',befsan[0][(before[0].index(A)-1)//2],'->',afsan[0][(after[0].index(A)-1)//2],')')
else:   #반응물 여러개이거나 생성물 여러개일때
    sanhwan(befsan,before,afsan,after,A,befmat,afmat)