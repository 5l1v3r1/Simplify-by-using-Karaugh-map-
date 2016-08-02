# -*- coding: cp936 -*-


"""def Denary2Binary(n):  
    '''''10进制转换为2进制字符串,位数不固定'''  
    bStr = ''  
    if n < 0:  raise ValueError, "must be a positive integer"  
    if n == 0: return '0'  
    while n > 0:  
        bStr = str(n % 2) + bStr  
        n = n >> 1  
    return bStr  """

def Denary2Binary(n,logic):  
    '''''10进制转换为2进制字符串,位数固定，为logic'''  
    bStr = ''  
    if n < 0:  raise ValueError, "must be a positive integer"   
    while n > 0:  
        bStr = str(n % 2) + bStr  
        n = n >> 1
    while len(bStr)<logic:
        bStr='0'+bStr
    return bStr

def KmapToLogicNumber(kmap,logic):#返回字符串二进制kmap
    for i in range(0,len(kmap)):
        kmap[i]=Denary2Binary(kmap[i],logic)
    return kmap

def deleteDuplicatedElementFromList2(u):#传递一个列表,删除列表内所有相同元素
        resultList = []
        for item in u:
            if not item in resultList:
                resultList.append(item)
        return resultList
#在Python中字符串是不可改变的对象(immutable)，因此无法直接修改字符串的某一位字符。
#一种可行的方式，是将字符串转换为列表，修改列表的元素后，在重新连接为字符串。
def stringchangeone(s,i,r):#将字符串i序号位改变为r字符
    l=list(s)
    l[i]=r
    return "".join(l)
    
    


def compareone(s1,s2):#比较字符串是否只有一个位不相同:
    flag=0
    p=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            flag=flag+1
            p=i
    if flag==1:
        return 1,p
    else:
        return 0,p
    
def KmapAdd(s1,s2):#传递二个同位的二进制数--字符串格式
    yn,p=compareone(s1,s2)
    if yn==1:
        s1=stringchangeone(s1,p,'x')   #字符串不支持s[p]='x'改变方式
        return 1,s1
    else:
        return 0,s1
    
    


def simple(kmap):
    u=[]
    flag=0
    for i in range(0,len(kmap)):
        flagi=0
        for j in range(0,len(kmap)):
            doadd,lin=KmapAdd(kmap[i],kmap[j])
            if doadd==1:
                u.append(lin)
                flagi=1
                flag=1
            else:
                pass
        if flagi==0:
            u.append(kmap[i])
    u=deleteDuplicatedElementFromList2(u)
    if flag==0:
        return u
    else:
        return simple(u)

def DelLastChar(s):#删除最后一个字符串
	str_list=list(s)
	str_list.pop()
	return "".join(str_list)


def ShowFexp(kmap,logic):
    K="A,B,C,D,E,F,G,H,I,J,K,L"#ABCDEF...从左到右依次为高位
    KL=K.split(',')
    UK=[]
    for i in range(0,logic):
        UK.append(KL[i])    #使用的变量字符串比如UK=["A","B"]
    F="F="
    for u in kmap:
        for j in range(0,len(u)):
            if u[j]=="1":
                F=F+UK[j]
            if u[j]=="0":
                F=F+UK[j]+"`"
        F=F+"+"
    print DelLastChar(F)
    
            
    

if __name__=="__main__":
    logic=6              #设置变量个数,最大不超过K里的变量数
    print "F=∑(...)"
    minnum=raw_input("Please input numbers in (...),eg~2,4,8,10:")
    kmap=minnum.split(',')
    
    for i in range(0,len(kmap)):
        kmap[i]=int(kmap[i])

    kmap=KmapToLogicNumber(kmap,logic)
    #kmap=["000110","011001"]这个样子
    #print kmap
    kmap=simple(kmap)
    ShowFexp(kmap,logic)
    

    
    
