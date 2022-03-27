import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


from random import randint

#Parametre du Mersenne Twister MT 19937 sur 32bit:

#Base 10:
w,n,m,r=32,624,397,31

#Base 16 :
a=0x9908B0DF                    
u,d=0x11,0xFFFFFFFF             
s,b=0x7,0x9D2C5680
t,c=0x15,0xEFC60000
l=18
f=1812433253

index = n
MT=[0]*n
lower_mask = (1<<r)-1
upper_mask = 1<<r



def int_32(number):
        return int(0xFFFFFFFF & number)


def graine():
                return (int(time.time()))

def Initialisation(graine):
                global MT,n,f,w
                MT[0]=graine
                for i in range(1,n):
                                MT[i]=int_32(f*(MT[i-1]^(MT[i-1]>>(w-2)))+i)
                


def twist():
                global MT,a,n,upper_mask,lower_mask,index
     
                for i in range(n):
                                temp=int_32((MT[i]&upper_mask)+(MT[(i+1)%n]&lower_mask))
                                temp_shift = temp>>1
                                if temp%2 != 0:
                                                temp_shift = temp_shift^a
                                MT[i]=MT[(i+m)%n]^temp_shift
                index=0



def Selection_Nombre ():
                global index,n,MT,s,b,t,c,l
                if index >=n:
                                twist()
                y = MT[index]
                y = y^((y<<s)&b)
                y = y^((y<<t)&c)
                y = y^(y>>l)
                index+=1
                return int_32(y)



def NombreAleatoire(graine):
                Initialisation(graine)
                return (Selection_Nombre ())

def NA_intervalle(graine,m):#m=valeur max de l'intervalle
                global d
                Initialisation(graine)
                a=Selection_Nombre ()
                a=a/d
                return int(m*a)

def graph_random(n,m):#n=nombre de point , m=valeur max
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                X,Y,Z=[],[],[]
                for i in range (n):
                                X.append(randint(0,m))
                                Y.append(randint(0,m))
                                Z.append(randint(0,m))
                ax.scatter(X,Y,Z, c='b',marker='.')
                ax.set_xlabel('x axis')
                ax.set_ylabel('y axis')
                ax.set_zlabel('z axis')
                plt.show()

def graph(n,m): #n=nombre de point , m=valeur max
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                X,Y,Z=[],[],[]
                for i in range (n):
                                X.append(NA_intervalle(graine(),m))
                                Y.append(NA_intervalle(graine(),m))
                                Z.append(NA_intervalle(graine(),m))
                ax.scatter(X,Y,Z, c='b',marker='.')
                ax.set_xlabel('x axis')
                ax.set_ylabel('y axis')
                ax.set_zlabel('z axis')
                plt.show()
                
                
def Repartition(n,m):    #n=nombre de point , m=valeur max
    X,Y=[0]*m,[0]*m
    for i in range(m):
        X[i]=i
    for i in range(n):
        Y[NA_intervalle(graine(),m)]+=1
    fig, ax = plt.subplots()
    ax.bar(X, Y, align='center')
    plt.show()






     