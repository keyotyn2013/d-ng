A=[]
k=0
def kiemtrasnt(n):
    if n==2 or n==3 :
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range (3,int(n**(0.5)+1),2):
            if(n%i==0):
                return False
        return True   

print('nhap n')
n=int(input())
if ((n>5) and (n<=5000)):
    for i in range (2,5000):
        if (kiemtrasnt(i)==True):
            A.append(i)
            k=k+1
B=[]
s=0
for x in A:
    for y in A:  
        z=n-x-y
        if z in A:
                B.append(x)
                B.append(y)
                B.append(z)
                s=s+1
min=0
d=0
for i in range (0,s*3,3):
    if(B[i]*25000000+B[i+1]*5000+B[i+2]) < min:
        min=B[i]*25000000+B[i+1]*5000+B[i+2]
        d=l
print('nghiem nguyen to cua phuong trinh la: ',B[d],' , ',B[d+1],' , ',B[d+2])


