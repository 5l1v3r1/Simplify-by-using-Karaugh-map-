# -*- coding: cp936 -*-


"""def Denary2Binary(n):  
    '''''10����ת��Ϊ2�����ַ���,λ�����̶�'''  
    bStr = ''  
    if n < 0:  raise ValueError, "must be a positive integer"  
    if n == 0: return '0'  
    while n > 0:  
        bStr = str(n % 2) + bStr  
        n = n >> 1  
    return bStr  """

def Denary2Binary(n,logic):  
    '''''10����ת��Ϊ2�����ַ���,λ���̶���Ϊlogic'''  
    bStr = ''  
    if n < 0:  raise ValueError, "must be a positive integer"   
    while n > 0:  
        bStr = str(n % 2) + bStr  
        n = n >> 1
    while len(bStr)<logic:
        bStr='0'+bStr
    return bStr

def KmapToLogicNumber(kmap,logic):#�����ַ���������kmap
    for i in range(0,len(kmap)):
        kmap[i]=Denary2Binary(kmap[i],logic)
    return kmap

def deleteDuplicatedElementFromList2(u):#����һ���б�,ɾ���б���������ͬԪ��
        resultList = []
        for item in u:
            if not item in resultList:
                resultList.append(item)
        return resultList
#��Python���ַ����ǲ��ɸı�Ķ���(immutable)������޷�ֱ���޸��ַ�����ĳһλ�ַ���
#һ�ֿ��еķ�ʽ���ǽ��ַ���ת��Ϊ�б��޸��б��Ԫ�غ�����������Ϊ�ַ�����
def stringchangeone(s,i,r):#���ַ���i���λ�ı�Ϊr�ַ�
    l=list(s)
    l[i]=r
    return "".join(l)
    
    


def compareone(s1,s2):#�Ƚ��ַ����Ƿ�ֻ��һ��λ����ͬ:
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
    
def KmapAdd(s1,s2):#���ݶ���ͬλ�Ķ�������--�ַ�����ʽ
    yn,p=compareone(s1,s2)
    if yn==1:
        s1=stringchangeone(s1,p,'x')   #�ַ�����֧��s[p]='x'�ı䷽ʽ
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

def DelLastChar(s):#ɾ�����һ���ַ���
	str_list=list(s)
	str_list.pop()
	return "".join(str_list)


def ShowFexp(kmap,logic):
    K="A,B,C,D,E,F,G,H,I,J,K,L"#ABCDEF...����������Ϊ��λ
    KL=K.split(',')
    UK=[]
    for i in range(0,logic):
        UK.append(KL[i])    #ʹ�õı����ַ�������UK=["A","B"]
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
    logic=6              #���ñ�������,��󲻳���K��ı�����
    print "F=��(...)"
    minnum=raw_input("Please input numbers in (...),eg~2,4,8,10:")
    kmap=minnum.split(',')
    
    for i in range(0,len(kmap)):
        kmap[i]=int(kmap[i])

    kmap=KmapToLogicNumber(kmap,logic)
    #kmap=["000110","011001"]�������
    #print kmap
    kmap=simple(kmap)
    ShowFexp(kmap,logic)
    

    
    
