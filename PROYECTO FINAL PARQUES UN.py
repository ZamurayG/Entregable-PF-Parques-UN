import random
import os
import sys
import time
from pygame import mixer

def limpiar():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
       
        
    
def dado_B():
    
    x=random.randint(1,6)
    #x=int(input("ingrese el valor del dado B"))
    
    time.sleep(1)
    if x==1:
        dado1=  [[" __","__","_"],
                 ["| ", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","__|"]]    
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)  
        input("presiona enter para continuar")
    elif x==2:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", "   ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)
        input("presiona enter para continuar")
    elif x==3:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)
        input("presiona enter para continuar")
    elif x==4:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", "   ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)
        input("presiona enter para continuar")
    elif x==5:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", " o ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)
        input("presiona enter para continuar")
    else:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["|o", "   ", "o|"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste",x)
        input("presiona enter para continuar")
    limpiar()
    salir_fichaB(x)
def salir_fichaB(x):
    if x==5 and mesa[11][11]== " B1 |" and mesa[11][12]==" B2 |" and mesa[16][10]=="____|" and mesa[16][16]=="*****"and mesa[16][15]=="*****":
        mesa[16][10]=" B1 |"
        mesa[11][11]="     " 
        print("true")
        mostrar2()
    elif x==5 and mesa[11][11]== " B1 |"   and mesa[16][10]=="____|" and mesa[16][16]=="*****"and mesa[16][15]=="*****":
        mesa[16][10]=" B1 |"
        mesa[11][11]="     "
        mostrar2()
    elif x==5 and mesa[11][11]== " B1 |"   and mesa[16][10]==" B2 |" and mesa[16][16]=="*****"and mesa[16][15]=="*****":
        ubicacion_ficha2B(x)
    
    elif x==5 and mesa[11][11]== " B1 |" and mesa[16][10]==" A1 |" and  mesa[16][16]=="*****" and mesa[16][15]=="*****":
        comer1(10,6,7,7,1,1)
    elif x==5 and mesa[11][11]== " B1 |" and mesa[16][10]==" A2 |" and  mesa[16][16]=="*****" and mesa[16][15]=="*****":
        comer1(10,6,7,7,1,2)
    elif x==5 and mesa[11][11]== " B1 |"  and mesa[16][10]==" C1 |" and  mesa[16][16]=="*****" and mesa[16][15]=="*****":
        comer1(10,6,7,7,1,3)
    elif x==5 and mesa[11][11]== " B1 |"  and mesa[16][10]==" C2 |" and  mesa[16][16]=="*****" and mesa[16][15]=="*****":
        comer1(10,6,7,7,1,4)    
    elif x!=5 and mesa[11][11]== " B1 |" and mesa[11][12]!=" B2 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
        ubicacion_ficha2B(x)    
        
    elif x==5 and mesa[11][11]!= " B1 |"and mesa[11][12]==" B2 |" and mesa[16][10]== "____|" and  mesa[16][16]=="*****" and mesa[16][15]=="*****":
        mesa[16][10]=" B2 |"
        mesa[11][12]="     "
        mostrar2()
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]== " B1 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
        ubicacion_ficha1B(x)
        
    elif x==5 and mesa[11][11]!= " B1 |" and mesa[11][12]==" B2 |" and mesa[16][10]== " A1 |" and mesa[16][16]=="*****"and mesa[16][15]=="*****":   
        comer1(10,6,7,8,2,1)
    elif x==5 and mesa[11][11]!= " B1 |" and mesa[11][12]==" B2 |" and mesa[16][10]== " A2 |" and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
        comer1(10,6,7,8,2,2)
   
    elif x==5 and mesa[11][11]!= " B1 |" and mesa[11][12]==" B2 |" and mesa[16][10]== " C1 |" and mesa[16][16]=="*****"and mesa[16][15]=="*****":
        comer1(10,6,7,8,2,3)
        
    elif x==5 and mesa[11][11]!= " B1 |" and mesa[11][12]==" B2 |" and mesa[16][10]== " C2 |" and mesa[16][16]=="*****"and mesa[16][15]=="*****":
        comer1(10,6,7,8,2,4)
    elif x!=5 and mesa[11][11]!=" B1 |" and mesa[11][12]==" B2 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
        
        ubicacion_ficha1B(x)  
    elif x==5 and mesa[11][11]!= " B1 |" and mesa[11][12]!=" B2 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
        
        seleccionar_fichaB(x)
    
    elif x!=5 and mesa[11][11]!= " B1 |" and mesa[11][12]!=" B2 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":
       
        seleccionar_fichaB(x)
    elif x!=5 and mesa[11][11]!= " B1 |" and mesa[11][12]==" A2 |"and  mesa[16][16]=="*****"and mesa[16][15]=="*****":     
        ubicacion_ficha1B(x)
        
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]=="____|" and mesa[16][16]=="1****":
        mesa[16][10]=" B2 |"
        mesa[11][12]="     "
        mostrar2()
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]==" A1 |" and mesa[16][16]=="1****":
        comer1(10,6,7,8,2,1)
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]==" A2 |" and mesa[16][16]=="1****":
        comer1(10,6,7,8,2,2)
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]==" C1 |" and mesa[16][16]=="1****":
        comer1(10,6,7,8,2,3)
    elif x==5 and mesa[11][12]==" B2 |" and mesa[16][10]==" C1 |" and mesa[16][16]=="1****":
        comer1(10,6,7,8,2,4)
    elif x!=5 and mesa[11][12]==" B2 |" and mesa[16][16]=="1****":
        mostrar2()
    elif x!=5 and mesa[11][12]!=" B2 |" and mesa[16][16]=="1****":
        ubicacion_ficha2B(x)
    elif x==5 and mesa[11][12]!=" B2 |" and mesa[16][16]=="1****":
        ubicacion_ficha2B(x)
    elif x==5 and mesa[11][11]==" B1 |" and mesa[16][10]=="____|" and mesa[16][15]=="2****":
        mesa[16][10]=" B1 |"
        mesa[11][11]="     "
        mostrar2()
    elif x==5 and mesa[11][11]==" B1 |" and mesa[16][10]==" A1 |" and mesa[16][15]=="2****":
        comer1(10,6,7,7,1,1)
    elif x==5 and mesa[11][11]==" B1 |" and mesa[16][10]==" A2 |" and mesa[16][15]=="2****":
        comer1(10,6,7,7,1,2)
    elif x==5 and mesa[11][11]==" B1 |" and mesa[16][10]==" C1 |" and mesa[16][15]=="2****":
        comer1(10,6,7,7,1,3)
    elif x==5 and mesa[11][11]==" B1 |" and mesa[16][10]==" C2 |" and mesa[16][15]=="2****":
        comer1(10,6,7,7,1,4)
    elif x!=5 and mesa[11][11]==" B1 |"  and mesa[16][15]=="2****":
        mostrar2()
    elif x!=5 and mesa[11][11]!=" B1 |"  and mesa[16][15]=="2****":
        ubicacion_ficha1B(x)
    elif x==5 and mesa[11][11]!=" B1 |"  and mesa[16][15]=="2****":
        ubicacion_ficha1B(x)    
    else:
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()  
        print("x es dierente de 5")
        
def seleccionar_fichaB(x):
    mostrar2()
    print("sacaste",x)
    print("seleciona que ficha quieres mover")
    f1=False
    while f1==False:
        f=input("si quieres mover la ficha B1 presiona 1, sino presiona 2")
        if f=="1":
            f1=True
            ubicacion_ficha1B(x)
            
        elif f=="2":
            ubicacion_ficha2B(x)
            f1=True
        else:
            print("no tienes esta ficha")
            f1=False
            limpiar()
            mostrar2()
           
    

    
def ubicacion_ficha1B(x):
    a=0
    b=0
    f=1
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" B1 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
    print(a,b)
    andar_B(x,a,b,f)
def ubicacion_ficha2B(x):
    a=0
    b=0
    f=2
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" B2 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
 
    andar_B(x,a,b,f)
global mesa
def andar_B(p,x,v,f):
    print(p)
    matriz_jugador1=[[0 , 0, 0, 0, 0, 0,33,32,31,30,29, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,34, 0, 0, 0,28, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,35, 0, 0, 0,27, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,36, 0, 0, 0,26, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,37, 0, 0, 0,25, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,38, 0, 0, 0,24, 0, 0, 0, 0, 0, 0],
                     [45,44,43,42,41,40,39, 0, 0, 0,23,22,21,20,19,18,17],
                     [46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,16],
                     [47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,15],
                     [48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14],
                     [49,50,51,52,53,54,55, 0, 0, 0, 7, 8, 9,10,11,12,13],
                     [0 , 0, 0, 0, 0, 0,56, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,57, 0,68, 0, 5, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,58, 0,67, 0, 4, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,59, 0,65, 0, 3, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,60, 0,64, 0, 2, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,61,62,63, 0, 1, 0, 0, 0, 0, 0, 0]]
    k=x
    t=v

    y=matriz_jugador1[x][v]
    print(y)
    contador=0
    u=0
    while contador<p:
        if y==matriz_jugador1[0][6] or y==matriz_jugador1[1][6] or y==matriz_jugador1[2][6] or y==matriz_jugador1[3][6] or y==matriz_jugador1[4][6] or y==matriz_jugador1[5][6]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
            
        elif y==matriz_jugador1[6][6] or y==matriz_jugador1[6][5] or y==matriz_jugador1[6][4] or y==matriz_jugador1[6][3] or y==matriz_jugador1[6][2] or y==matriz_jugador1[6][1]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[6][0] or y==matriz_jugador1[7][0] or y==matriz_jugador1[8][0] or y==matriz_jugador1[9][0]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[10][0] or y==matriz_jugador1[10][1] or y==matriz_jugador1[10][2] or y==matriz_jugador1[10][3] or y==matriz_jugador1[10][4] or y==matriz_jugador1[10][5]:
            y=matriz_jugador1[x][v+1]
           
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[10][6] or y==matriz_jugador1[11][6] or y==matriz_jugador1[12][6] or y==matriz_jugador1[13][6] or y==matriz_jugador1[14][6] or y==matriz_jugador1[15][6]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[16][6] or y==matriz_jugador1[16][7]:
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[16][8] or y==matriz_jugador1[15][8] or y==matriz_jugador1[14][8]or y==matriz_jugador1[13][8] or y==matriz_jugador1[12][8] or y==matriz_jugador1[11][8] :
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[16][10] or y==matriz_jugador1[15][10] or y==matriz_jugador1[14][10]or y==matriz_jugador1[13][10] or y==matriz_jugador1[12][10] or y==matriz_jugador1[11][10] :
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[10][10] or y==matriz_jugador1[10][11] or y==matriz_jugador1[10][12] or y==matriz_jugador1[10][13] or y==matriz_jugador1[10][14] or y==matriz_jugador1[10][15]:
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[10][16] or y==matriz_jugador1[9][16] or y==matriz_jugador1[8][16] or y==matriz_jugador1[7][16]:
            y=matriz_jugador1[x-1][v]
           
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[6][16] or y==matriz_jugador1[6][15] or y==matriz_jugador1[6][14] or y==matriz_jugador1[6][13] or y==matriz_jugador1[6][12] or y==matriz_jugador1[6][11]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[6][10] or y==matriz_jugador1[5][10] or y==matriz_jugador1[4][10] or y==matriz_jugador1[3][10] or y==matriz_jugador1[2][10] or y==matriz_jugador1[1][10]:
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[0][10] or y==matriz_jugador1[0][9] or y==matriz_jugador1[0][8] or y==matriz_jugador1[0][7]:
            y=matriz_jugador1[x][v-1]
            
            contador=contador+1
            v=v-1
            
            
        elif y==matriz_jugador1[10][0] and p==1 or p-contador==1:
            print("coronaste una ficha")
            mesa[k][t]="____|"
            u=1
            contador=7
            
            if f==1:
                mesa[16][16]="1****"
            else:
                mesa[16][15]="2****"
        elif y==matriz_jugador1[6][5] and p>1 or contador-p>1:
            g=p-contador-2
            y=matriz_jugador1[x+g][v]
            contador=7
            x=x+g
        else:
            print("algo anda mal")
            

         
    print("posicion final", x,v)
    if mesa[x][v]==" B2 |" and f==1:
        print("no puede estar en la misma posicion")
        seleccionar_fichaB(p)
    elif mesa[x][v]==" B1 |" and f==2:
        print("no puede estar en la misma posicion")
        seleccionar_fichaB(p)
    elif mesa[x][v]==" B1 |" and f==1:
        mesa [x][v]=" B1 |"
        mostrar2()
    elif mesa [x][v]==" B2 |" and f==2:
        mesa [x][v]=" B2 |"
        mostrar2()
        
    elif mesa[x][v]==" A1 |":
        print("te comiste una ficha")
        
        comer1(x,v,k,t,f,1)
    elif mesa[x][v]==" A2 |":
        print("te comiste una ficha")
        comer1(x,v,k,t,f,2)
    elif mesa[x][v]==" C1 |":
        print("te comiste una ficha")
        comer1(x,v,k,t,f,3)
    elif mesa[x][v]==" C2 |":
        print("te comiste una ficha")
        comer1(x,v,k,t,f,4)
    elif u==1:
        mostrar2()
        time.sleep(1)
    else:
    
        actualizar2(x,v,k,t,f)
      


def comer1(x,v,k,t,f,n):
    if f==1 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" B1 |"
        mesa[5][0]=" A1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" B2 |"
        mesa[5][0]=" A1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" B1 |"
        mesa[5][1]=" A2 |"
        
        
        
        mostrar2()
        time.sleep(1)
       
    elif f==2 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" B2 |"
        mesa[5][1]=" A2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" B1 |"
        mesa[11][0]=" C1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" B2 |"
        mesa[11][0]=" C2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" B1 |"
        mesa[11][0]=" C2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" B2 |"
        mesa[11][0]=" C1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    else:
        print("algo anda mal")
def mostrar2():
    limpiar()
    for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
    
def actualizar2(x,v,x0,v0,f):
    limpiar()
    if f==1:
        mesa[x0][v0]="____|"
        mesa[x][v]=" B1 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 1")
    else:
        mesa[x0][v0]="____|"
        mesa[x][v]=" B2 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 2")
global mesa

def dado():
   x=random.randint(1,6)
   #x=int(input("ingrese el valor del dado A"))
   
   
   
   time.sleep(1)
   if x==1:
        dado1=  [[" __","__","_"],
                 ["| ", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","__|"]]    
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==2:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", "   ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==3:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==4:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", "   ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==5:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", " o ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   else:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["|o", "   ", "o|"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
   
        print("sacaste", x)
        input("presiona enter para continuar")
   limpiar()
   salir_fichaA(x)
   
def salir_fichaA(x):
    
    if x==5 and mesa[5][0]== " A1 |" and mesa[5][1]==" A2 |" and mesa[0][6]=="____|"and mesa[0][0]=="*****"  and mesa[0][1]=="*****":
        mesa[0][6]=" A1 |"
        mesa[5][0]="     " 
        print("true")
        mostrar2()
    elif x==5 and mesa[5][0]== " A1 |"   and mesa[0][6]=="____|" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        mesa[0][6]=" A1 |"
        mesa[5][0]="     "
        mostrar2()
    elif x==5 and mesa[5][0]== " A1 |"   and mesa[0][6]==" A2 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        ubicacion_ficha2(x)
        
    elif x==5 and mesa[5][0]== " A1 |"  and mesa[0][6]==" B1 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,0,1,1)
    elif x==5 and mesa[5][0]== " A1 |"  and mesa[0][6]==" B2 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,0,1,2)
    elif x==5 and mesa[5][0]== " A1 |"  and mesa[0][6]==" C1 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,0,1,3)
    elif x==5 and mesa[5][0]== " A1 |"  and mesa[0][6]==" C2 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,0,1,4)
    elif x!=5 and mesa[5][0]== " A1 |"and mesa[5][1]!=" A2 |" and mesa[0][0]=="*****"  and mesa[0][1]=="*****":
        ubicacion_ficha2(x)
    elif x==5 and mesa[5][0]!= " A1 |"and mesa[5][1]==" A2 |"and mesa[0][6]== "____|"and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        mesa[0][6]=" A2 |"
        mesa[5][1]="     "
        mostrar2()
    elif x==5 and mesa[5][1]==" A2 |"and mesa[0][6]== " A1 |" and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        ubicacion_ficha1(x)
        
    elif x==5 and mesa[5][0]!= " A1 |" and mesa[5][1]==" A2 |" and mesa[0][6]== " B1 |"  and mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,1,2,1)
    elif x==5 and mesa[5][0]!= " A1 |" and mesa[5][1]==" A2 |" and mesa[0][6]== " B2 |"  and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,1,2,2)
    elif x==5 and mesa[5][0]!= " A1 |" and mesa[5][1]==" A2 |" and mesa[0][6]== " C1 |"  and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,1,2,3)
    elif x==5 and mesa[5][0]!= " A1 |" and mesa[5][1]==" A2 |" and mesa[0][6]== " C2 |"  and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        comer(0,4,3,1,2,4)
    elif x!=5 and mesa[5][0]!= " A1 |" and mesa[5][1]==" A2 |"and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        ubicacion_ficha1(x)
    elif x==5 and mesa[5][0]!= " A1 |" and mesa[5][1]!=" A2 |"and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        seleccionar_ficha(x)
    elif x!=5 and mesa[5][0]!= " A1 |" and mesa[5][1]!=" A2 |"and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        seleccionar_ficha(x)    
        
    elif x!=5 and mesa[5][0]!=" A1 |" and mesa[5][1]==" A2 |"and  mesa[0][0]=="*****"and mesa[0][1]=="*****":
        ubicacion_ficha1(x)
        
    elif x==5  and mesa[5][1]==" A2 |" and mesa[0][6]== "____|"  and  mesa[0][0]=="1****":
        mesa[0][6]=" A2 |"
        mesa[5][1]="     "
        mostrar2()
    elif x==5  and mesa[5][1]==" A2 |" and mesa[0][6]== " B1 |" and mesa[0][0]=="1****":
        comer(0,4,3,1,2,1)
    elif x==5  and mesa[5][1]==" A2 |" and mesa[0][6]== " B2 |" and mesa[0][0]=="1****":
        comer(0,4,3,1,2,2)
    elif x==5  and mesa[5][1]==" A2 |" and mesa[0][6]== " C1 |" and mesa[0][0]=="1****":
        comer(0,4,3,1,2,3)
    elif x==5  and mesa[5][1]==" A2 |" and mesa[0][6]== " C2 |" and mesa[0][0]=="1****":
        comer(0,4,3,1,2,4)
        
    elif x!=5  and mesa[5][1]==" A2 |"  and  mesa[0][0]=="1****":
         mostrar2()
    elif x!=5  and mesa[5][1]!=" A2 |"  and mesa[0][0]=="1****":
        ubicacion_ficha2(x)
    elif x==5  and mesa[5][1]!=" A2 |"  and  mesa[0][0]=="1****":
        ubicacion_ficha2(x)
       
    elif x==5  and mesa[5][0]==" A1 |" and mesa[0][6]== "____|"  and  mesa[0][1]=="2****":
        mesa[0][6]=" A1 |"
        mesa[5][0]="     "
        mostrar2()
    elif x==5  and mesa[5][0]==" A1 |" and mesa[0][6]== " B1 |"  and  mesa[0][1]=="2****":
        comer(0,4,3,0,1,1)
        
    elif x==5  and mesa[5][0]==" A1 |" and mesa[0][6]== " B2 |"  and  mesa[0][1]=="2****":
        comer(0,4,3,0,1,2)
    elif x==5  and mesa[5][0]==" A1 |" and mesa[0][6]== " C1 |"  and  mesa[0][1]=="2****":
        comer(0,4,3,0,1,3)
    elif x==5  and mesa[5][0]==" A1 |" and mesa[0][6]== " C2 |"  and  mesa[0][1]=="2****":
        comer(0,4,3,0,1,4)
    elif x!=5  and mesa[5][0]==" A1 |"  and  mesa[0][1]=="2****":
        mostrar2()
    elif x!=5  and mesa[5][0]!=" A1 |"  and  mesa[0][1]=="2****":
        ubicacion_ficha1(x)
    elif x==5  and mesa[5][0]!=" A1 |"  and  mesa[0][1]=="2****":
        ubicacion_ficha1(x)
    else:
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()  
        print("x es dierente de 5")
   
   
global mesa

def seleccionar_ficha(x):
    mostrar2()
    print("sacaste", x)
    print("seleciona que ficha quieres mover")
    f1=False
    while f1==False:
        f=input("si quieres mover la ficha A1 presiona 1, sino presiona 2")
        if f=="1":
            f1=True
            ubicacion_ficha1(x)
            
        elif f=="2":
            ubicacion_ficha2(x)
            f1=True
        else:
            print("no tienes esta ficha")
            f1=False
            limpiar()
            mostrar2()
    
def ubicacion_ficha1(x):
    a=0
    b=0
    f=1
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" A1 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
    print(a,b)
    andar(x,a,b,f)
def ubicacion_ficha2(x):
    a=0
    b=0
    f=2
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" A2 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
    
    andar(x,a,b,f)
global mesa
def andar(p,x,v,f):
   
    matriz_jugador1=[[0 , 0, 0, 0, 0, 0, 1, 0,63,62,61, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0, 2, 0,64, 0,60, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0, 3, 0,65, 0,59, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0, 4, 0,66, 0,58, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0, 5, 0,67, 0,57, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0, 6, 0,68, 0,65, 0, 0, 0, 0, 0, 0],
                     [13,12,11,10, 9, 8, 7, 0, 0, 0,55,54,53,52,51,50,49],
                     [14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,48],
                     [15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,47],
                     [16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,46],
                     [17,18,19,20,21,22,23, 0, 0, 0,39,40,41,42,43,44,45],
                     [0 , 0, 0, 0, 0, 0,24, 0, 0, 0,38, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,25, 0, 0, 0,37, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,26, 0, 0, 0,36, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,27, 0, 0, 0,35, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,28, 0, 0, 0,34, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0, 0, 0, 0,29,30,31,32,33, 0, 0, 0, 0, 0, 0]]
    k=x
    t=v
    u=0
    y=matriz_jugador1[x][v]
    #pasos=p
    
    contador=0
    while contador<p:
        if y==matriz_jugador1[0][6] or y==matriz_jugador1[1][6] or y==matriz_jugador1[2][6] or y==matriz_jugador1[3][6] or y==matriz_jugador1[4][6] or y==matriz_jugador1[5][6]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
            
        elif y==matriz_jugador1[6][6] or y==matriz_jugador1[6][5] or y==matriz_jugador1[6][4] or y==matriz_jugador1[6][3] or y==matriz_jugador1[6][2] or y==matriz_jugador1[6][1]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[6][0] or y==matriz_jugador1[7][0] or y==matriz_jugador1[8][0] or y==matriz_jugador1[9][0]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[10][0] or y==matriz_jugador1[10][1] or y==matriz_jugador1[10][2] or y==matriz_jugador1[10][3] or y==matriz_jugador1[10][4] or y==matriz_jugador1[10][5]:
            y=matriz_jugador1[x][v+1]
           
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[10][6] or y==matriz_jugador1[11][6] or y==matriz_jugador1[12][6] or y==matriz_jugador1[13][6] or y==matriz_jugador1[14][6] or y==matriz_jugador1[15][6]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[16][6] or y==matriz_jugador1[16][7] or y==matriz_jugador1[16][8] or y==matriz_jugador1[16][9]:
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[16][10] or y==matriz_jugador1[15][10] or y==matriz_jugador1[14][10]or y==matriz_jugador1[13][10] or y==matriz_jugador1[12][10] or y==matriz_jugador1[11][10] :
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[10][10] or y==matriz_jugador1[10][11] or y==matriz_jugador1[10][12] or y==matriz_jugador1[10][13] or y==matriz_jugador1[10][14] or y==matriz_jugador1[10][15]:
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[10][16] or y==matriz_jugador1[9][16] or y==matriz_jugador1[8][16] or y==matriz_jugador1[7][16]:
            y=matriz_jugador1[x-1][v]
           
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[6][16] or y==matriz_jugador1[6][15] or y==matriz_jugador1[6][14] or y==matriz_jugador1[6][13] or y==matriz_jugador1[6][12] or y==matriz_jugador1[6][11]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[6][10] or y==matriz_jugador1[5][10] or y==matriz_jugador1[4][10] or y==matriz_jugador1[3][10] or y==matriz_jugador1[2][10] or y==matriz_jugador1[1][10]:
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[0][10] or y==matriz_jugador1[0][9]:
            y=matriz_jugador1[x][v-1]
            
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[0][8] or y==matriz_jugador1[1][8] or y==matriz_jugador1[2][8] or y==matriz_jugador1[3][8]:
            y=matriz_jugador1[x+1][v]
           
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[4][8] and p==1 or p-contador==1:
            print("coronaste una ficha")
            mesa[k][t]="____|"
            u=1
            contador=7
            if f==1:
                mesa[0][0]="1****"
            else:
                mesa[0][1]="2****"
         
        elif y==matriz_jugador1[4][9] and p>1 or p-contador>1:
            g=p-contador
            y=matriz_jugador1[x-g][v]
            contador=7
            x=x-g+2
        else:
            contador=7

          
    print("posicion final", x,v)
    if mesa[x][v]==" A2 |" and f==1:
        print("no puede estar en la misma posicion")
        seleccionar_ficha(p)
    elif mesa [x][v]==" A1 |"and f==2:
        print("no puede estar en la misma posicion")
        seleccionar_ficha(p)
    
    elif mesa [x][v]==" A1 |" and f==1:
        mesa [x][v]=" A1 |"
    
    elif mesa [x][v]==" A2 |" and f==2:
        mesa [x][v]=" A2 |"
        mostrar2()
    elif mesa[x][v]==" B1 |":
        print("te comiste una ficha")
        comer(x,v,k,t,f,1)
    elif u==1:
        
        
        mostrar2()
        time.sleep(1)

    elif mesa[x][v]==" B2 |":
        print("te comiste una ficha")
        comer(x,v,k,t,f,2)    
    elif mesa[x][v]==" C1 |":
        print("te comiste una ficha")
        comer(x,v,k,t,f,3)
    elif mesa[x][v]==" C2 |":
        print("te comiste una ficha")
        comer(x,v,k,t,f,4)  
    else:
    
        actualizar1(x,v,k,t,f)

def comer(x,v,k,t,f,n):
    if f==1 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" A1 |"
        mesa[11][11]=" B1 |"
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" A2 |"
        mesa[11][11]=" B1 |"
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" A1 |"
        mesa[11][12]=" B2 |"
        
        
        
        mostrar2()
        time.sleep(1)
       
    elif f==2 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" A2 |"
        mesa[11][12]=" B2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" A1 |"
        mesa[11][0]=" C1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" A2 |"
        mesa[11][1]=" C2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" A1 |"
        mesa[11][1]=" C2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" A2 |"
        mesa[11][0]=" C1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    else:
        print("Algo anda mal")
        
def actualizar1(x,v,x0,v0,f):
    limpiar()
    if f==1:
        mesa[x0][v0]="____|"
        mesa[x][v]=" A1 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 1")
    else:
        mesa[x0][v0]="____|"
        mesa[x][v]=" A2 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 2")
global mesa 

def dado_C():
   x=random.randint(1,6)
   time.sleep(1)
   if x==1:
        dado1=  [[" __","__","_"],
                 ["| ", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","__|"]]    
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==2:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", "   ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==3:
        dado1= [[" __","__","_"],
                 ["|o", "  ", "  |"],
                 ["| ", " o ", " |"],
                 ["|_","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==4:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", "   ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   elif x==5:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["| ", " o ", " |"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
        print("sacaste", x)
        input("presiona enter para continuar")
   else:
        dado1= [[" __","__","_"],
                 ["|o", "  ", " o|"],
                 ["|o", "   ", "o|"],
                 ["|o","__","_o|"]]
        for i in range (4):
            for j in range (3):
                print(dado1[i][j], end="")
            print()
   
        print("sacaste", x)
        input("presiona enter para continuar")
   limpiar()
   salir_fichaC(x)

def salir_fichaC(x):
    
    if x==5 and mesa[11][0]== " C1 |" and mesa[11][1]==" C2 |" and mesa[10][0]=="____|"and mesa[16][0]=="*****"  and mesa[16][1]=="*****":
        mesa[10][0]=" C1 |"
        mesa[11][0]="     " 
        mostrar2()
    elif x==5 and mesa[11][0]== " C1 |"   and mesa[10][0]=="____|" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        mesa[10][0]=" C1 |"
        mesa[11][0]="     "
        mostrar2()
    elif x==5 and mesa[11][0]== " C1 |"   and mesa[10][0]==" C2 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        ubicacion_ficha2C(x)
        
    elif x==5 and mesa[11][0]== " C1 |"  and mesa[10][0]==" B1 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,0,1,1)
    elif x==5 and mesa[11][0]== " C1 |"  and mesa[10][0]==" B2 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,0,1,2)
    elif x==5 and mesa[11][0]== " C1 |"  and mesa[10][0]==" A1 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,0,1,3)
    elif x==5 and mesa[11][0]== " C1 |"  and mesa[10][0]==" A2 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,0,1,4)
    elif x!=5 and mesa[11][0]== " C1 |"and mesa[11][0]!=" C2 |" and mesa[16][0]=="*****"  and mesa[16][1]=="*****":
        ubicacion_ficha2C(x)
    elif x==5 and mesa[11][0]!= " C1 |"and mesa[11][0]==" C2 |"and mesa[10][0]== "____|"and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        mesa[10][0]=" C2 |"
        mesa[11][0]="     "
        mostrar2()
    elif x==5 and mesa[11][0]==" C2 |"and mesa[10][0]== " C1 |" and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        ubicacion_ficha1C(x)
        
    elif x==5 and mesa[11][0]!= " C1 |" and mesa[11][0]==" C2 |" and mesa[10][0]== " B1 |"  and mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,1,2,1)
    elif x==5 and mesa[11][0]!= " C1 |" and mesa[11][0]==" C2 |" and mesa[10][0]== " B2 |"  and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,1,2,2)
    elif x==5 and mesa[11][0]!= " C1 |" and mesa[11][0]==" C2 |" and mesa[10][0]== " A1 |"  and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,1,2,3)
    elif x==5 and mesa[11][0]!= " C1 |" and mesa[11][0]==" C2 |" and mesa[10][0]== " A2 |"  and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        comer3(6,0,7,1,2,4)
    elif x!=5 and mesa[11][0]!= " C1 |" and mesa[11][0]==" C2 |"and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        ubicacion_ficha1C(x)
    elif x==5 and mesa[11][0]!= " C1 |" and mesa[11][0]!=" C2 |"and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        seleccionar_fichaC(x)
    elif x!=5 and mesa[11][0]!= " C1 |" and mesa[11][0]!=" C2 |"and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        seleccionar_fichaC(x)    
        
    elif x!=5 and mesa[11][0]!=" C1 |" and mesa[11][0]==" C2 |"and  mesa[16][0]=="*****"and mesa[16][1]=="*****":
        ubicacion_ficha1C(x)
        
    elif x==5  and mesa[11][0]==" C2 |" and mesa[10][0]== "____|"  and  mesa[16][0]=="1****":
        mesa[10][0]=" C2 |"
        mesa[11][0]="     "
        mostrar2()
    elif x==5  and mesa[11][0]==" C2 |" and mesa[10][0]== " B1 |" and mesa[16][0]=="1****":
        comer3(6,0,7,1,2,1)
    elif x==5  and mesa[11][0]==" C2 |" and mesa[10][0]== " B2 |" and mesa[16][0]=="1****":
        comer3(6,0,7,1,2,2)
    elif x==5  and mesa[11][0]==" C2 |" and mesa[10][0]== " A1 |" and mesa[16][0]=="1****":
        comer3(6,0,7,1,2,3)
    elif x==5  and mesa[11][0]==" C2 |" and mesa[10][0]== " A2 |" and mesa[16][0]=="1****":
        comer3(6,0,7,1,2,4)
        
    elif x!=5  and mesa[11][0]==" C2 |"  and  mesa[16][0]=="1****":
         mostrar2()
    elif x!=5  and mesa[11][0]!=" C2 |"  and mesa[16][0]=="1****":
        ubicacion_ficha2C(x)
    elif x==5  and mesa[11][0]!=" C2 |"  and  mesa[16][0]=="1****":
        ubicacion_ficha2C(x)
       
    elif x==5  and mesa[11][0]==" C1 |" and mesa[10][0]== "____|"  and  mesa[16][1]=="2****":
        mesa[10][0]=" C1 |"
        mesa[11][0]="     "
        mostrar2()
    elif x==5  and mesa[11][0]==" C1 |" and mesa[10][0]== " B1 |"  and  mesa[16][1]=="2****":
        comer3(6,0,7,0,1,1)
        
    elif x==5  and mesa[11][0]==" C1 |" and mesa[10][0]== " B2 |"  and  mesa[16][1]=="2****":
        comer3(6,0,7,0,1,2)
    elif x==5  and mesa[11][0]==" C1 |" and mesa[10][0]== " A1 |"  and  mesa[16][1]=="2****":
        comer3(6,0,7,0,1,3)
    elif x==5  and mesa[11][0]==" C1 |" and mesa[10][0]== " A2 |"  and  mesa[16][1]=="2****":
        comer3(6,0,7,0,1,4)
    elif x!=5  and mesa[11][0]==" C1 |"  and  mesa[16][1]=="2****":
        mostrar2()
    elif x!=5  and mesa[11][0]!=" C1 |"  and  mesa[16][1]=="2****":
        ubicacion_ficha1C(x)
    elif x==5  and mesa[11][0]!=" C1 |"  and  mesa[16][1]=="2****":
        ubicacion_ficha1C(x)
    else:
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()  
        print("x es dierente de 5")

def comer3(x,v,k,t,f,n):
    
    if f==1 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" C1 |"
        mesa[11][11]=" B1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==1:
        mesa[k][t]="____|"
        mesa[x][v]=" C2 |"
        mesa[11][11]=" B1 |"
        mostrar2()
    elif f==1 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" C1 |"
        mesa[11][12]=" B2 |"
        
        
        
        mostrar2()
        time.sleep(1)
       
    elif f==2 and n==2:
        mesa[k][t]="____|"
        mesa[x][v]=" C2 |"
        mesa[11][12]=" B2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" C1 |"
        mesa[5][0]=" A1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" C2 |"
        mesa[5][1]=" A2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==1 and n==4:
        mesa[k][t]="____|"
        mesa[x][v]=" C1 |"
        mesa[5][1]=" A2 |"
        
        
        
        mostrar2()
        time.sleep(1)
    elif f==2 and n==3:
        mesa[k][t]="____|"
        mesa[x][v]=" C2 |"
        mesa[5][0]=" A1 |"
        
        
        
        mostrar2()
        time.sleep(1)
    else:
        print("Algo anda mal")
def seleccionar_fichaC(x):
    mostrar2()
    print("sacaste", x)
    print("seleciona que ficha quieres mover")
    f1=False
    while f1==False:
        f=input("si quieres mover la ficha C1 presiona 1, sino presiona 2")
        if f=="1":
            f1=True
            ubicacion_ficha1C(x)
            
        elif f=="2":
            ubicacion_ficha2C(x)
            f1=True
        else:
            print("no tienes esta ficha")
            f1=False
            limpiar()
            mostrar2()
    

   
def ubicacion_ficha1C(x):
    a=0
    b=0
    f=1
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" C1 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
    print(a,b)
    andarC(x,a,b,f)
def ubicacion_ficha2C(x):
    a=0
    b=0
    f=2
    for i in range(17):
        for j in range(17):
           if mesa[i][j]==" C2 |":
               print("ubicacion es",i,j)
               a=i
               b=j
               break
           else:
               pass
    
    andarC(x,a,b,f)
    
def andarC(p,x,v,f):
   
    matriz_jugador1=[[0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0 , 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    k=x
    t=v
    u=0
    y=matriz_jugador1[x][v]
    #pasos=p
    
    contador=0
    while contador<p:
        if y==matriz_jugador1[0][6] or y==matriz_jugador1[1][4] or y==matriz_jugador1[2][4] or y==matriz_jugador1[3][4]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
            
        elif y==matriz_jugador1[4][4] or y==matriz_jugador1[4][3] or y==matriz_jugador1[4][2] or y==matriz_jugador1[4][1]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[4][0]  :
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[10][0] or y==matriz_jugador1[6][1] or y==matriz_jugador1[6][2] or y==matriz_jugador1[6][3]:
            y=matriz_jugador1[x][v+1]
           
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[6][4] or y==matriz_jugador1[7][4] or y==matriz_jugador1[8][4] or y==matriz_jugador1[9][4]:
            y=matriz_jugador1[x+1][v]
            
            contador=contador+1
            x=x+1
        elif y==matriz_jugador1[10][4] or y==matriz_jugador1[10][5] :
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[16][10] or y==matriz_jugador1[9][6] or y==matriz_jugador1[8][6]or y==matriz_jugador1[7][6] :
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[6][6] or y==matriz_jugador1[6][7] or y==matriz_jugador1[6][8] or y==matriz_jugador1[6][9]:
            y=matriz_jugador1[x][v+1]
            
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[6][10] or y==matriz_jugador1[5][10]  :
            y=matriz_jugador1[x-1][v]
           
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[4][10] or y==matriz_jugador1[4][9] or y==matriz_jugador1[4][8] or y==matriz_jugador1[4][7]:
            y=matriz_jugador1[x][v-1]
           
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[4][6] or y==matriz_jugador1[3][6] or y==matriz_jugador1[2][6]or y==matriz_jugador1[1][6] :
            y=matriz_jugador1[x-1][v]
            
            contador=contador+1
            x=x-1
        elif y==matriz_jugador1[0][6] or y==matriz_jugador1[0][5]:
            y=matriz_jugador1[x][v-1]
            
            contador=contador+1
            v=v-1
        elif y==matriz_jugador1[5][0] or y==matriz_jugador1[5][1] or y==matriz_jugador1[5][2] or y==matriz_jugador1[5][3]:
            y=matriz_jugador1[x][v+1]
           
            contador=contador+1
            v=v+1
        elif y==matriz_jugador1[5][4] and p==1 or p-contador==1:
            print("coronaste una ficha")
            mesa[k][t]="____|"
            u=1
            contador=7
            if f==1:
                mesa[16][0]="1****"
            else:
                mesa[16][1]="2****"
         
        elif y==matriz_jugador1[5][4] and p>1 or p-contador>1:
            g=p-contador
            y=matriz_jugador1[x][v-g]
            contador=7
            v=v-g+2
        else:
            contador=7
         
    print("posicion final", x,v)
    if mesa[x][v]==" C2 |" and f==1:
        print("no puede estar en la misma posicion")
        seleccionar_fichaC(p)
    elif mesa [x][v]==" C1 |"and f==2:
        print("no puede estar en la misma posicion")
        seleccionar_fichaC(p)
    
    elif mesa [x][v]==" C1 |" and f==1:
        mesa [x][v]=" C1 |"
    
    elif mesa [x][v]==" C2 |" and f==2:
        mesa [x][v]=" C2 |"
        mostrar2()
    elif mesa[x][v]==" B1 |":
        print("te comiste una ficha")
        comer3(x,v,k,t,f,1)
    elif u==1:
        
        
        mostrar2()
        time.sleep(1)

    elif mesa[x][v]==" B2 |":
        print("te comiste una ficha")
        comer3(x,v,k,t,f,2)    
    elif mesa[x][v]==" A1 |":
        print("te comiste una ficha")
        comer3(x,v,k,t,f,3)
    elif mesa[x][v]==" A2 |":
        print("te comiste una ficha")
        comer3(x,v,k,t,f,4)  
    else:
    
        actualizar3(x,v,k,t,f)
        
def actualizar3(x,v,x0,v0,f):
    limpiar()
    if f==1:
        mesa[x0][v0]="____|"
        mesa[x][v]=" C1 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 1")
    else:
        mesa[x0][v0]="____|"
        mesa[x][v]=" C2 |"
        for i in range (17):
            for j in range (17):
                print(mesa[i][j], end="")
            print()
        print("movio ficha 2")

def inicio():
    limpiar()
    j1=input("Ingresa el nombre del jugador 1: ")
    print()
    j2=input("Ingresa el nombre del jugador 2: ")

    for i in range (17):
        for j in range (17):
           print(mesa[i][j], end="")
        print()  
    q=0
    while q==0:
       
        if mesa[0][0]=="1****" and mesa[0][1]=="2****":
            print("Gano",j1, "Felicitaciones")
            
            time.sleep(1)
            input("Presiona enter para continuar")
            salir()
        elif mesa[16][16]=="1****" and mesa[16][15]=="2****":
            print("Gano",j2, "Felicitaciones")
            
            time.sleep(1)
            input("Presiona enter para continuar")
            salir()
        else:
            print("Juega ", j1)
            input("presione enter para continuar") 
            dado()
            mostrar2()
            print("Juega ", j2)
            input("presione enter para continuar")
            dado_B() 
  
    print("gracias")
global mesa

def inicio2():
    limpiar()
    j1=input("Ingresa el nombre del jugador 1: ")
    print()
    j2=input("Ingresa el nombre del jugador 2: ")
    print()
    j3=input("Ingresa el nombre del jugador 3: ")
    mesa[11][0]=" C1 |"
    mesa[11][0]=" C2 |"
    for i in range (17):
        for j in range (17):
           print(mesa[i][j], end="")
        print()  
    q=0
    while q==0:
       
        if mesa[0][0]=="1****" and mesa[0][1]=="2****":
            print("Gano",j1, "Felicitaciones")
            
            time.sleep(1)
            input("Presiona enter para continuar")
            salir()
        elif mesa[16][16]=="1****" and mesa[16][15]=="2****":
            print("Gano",j2, "Felicitaciones")
            
            time.sleep(1)
            input("Presiona enter para continuar")
            salir()
        elif mesa[16][0]=="1****" and mesa[16][1]=="2****":
            print("Gano",j3, "Felicitaciones")
            
            time.sleep(1)
            input("Presiona enter para continuar")
            salir()
        else:
            print("Juega ", j1)
            input("presione enter para continuar") 
            dado()
            mostrar2()
            print("Juega ", j3)
            input("presione enter para continuar") 
            dado_C()
            mostrar2()
            print("Juega ", j2)
            input("presione enter para continuar")
            dado_B() 
            
def jugadores():
    limpiar()
    print("¿Cuantos jugadores? ")
    print()
    print("Presiona 2 para dos jugadores")
    print()
    print("Prsiona 3 para 3 jugadores ")
    print()
    print("Presiona otra tecla para regresar al menu")
    a=input("Respuesta: ")
    if a=="2":
        inicio()
    elif a=="3":
        inicio2()
    else:
        limpiar()
        menu()
def salir():
    limpiar()
    print("Gracias por jugar")
    input("Presione enter para cerrar")
    sys.exit()
    
def instrucciones():
    print("Estas son las instrucciones del juego:")
    print()
    print("1)Solo hay un dado ")
    print("2)Siempre empieza la ficha A y despues por derecha")
    print("3)La ficha sale de la carcel si sale 5")
    print("4)Las fichas de la misma letra no pueden estar en la misma casilla ")
    print("5)Si caes en una casilla donde habia una ficha de otra letra, esta vuelve a la carcel")
    print("6)Al momento de la llegaba, la ficha debe caer exactamente, sino, los movimientos de mas comenzara a retroceder")
    print("7)El juego termina cuando un jugador corone sus dos fichas")
    print()
    input("Presiona enter para regresar al menu")
    limpiar()
    menu()
    
def menu():
    print("Bienvenido ")
    print()
    print("Presiona 1 si quieres jugar")
    print()
    print("Presiona 2 si quieres ver las instrucciones")
    print()
    print("Presiona otra tecla si quieres salir")
    a=input("Respuesta: ")
    if a=="1":
        jugadores()
    elif a=="2":
        instrucciones()
    else:
        salir()
    
mesa=        [["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              [" A1 |"," A2 |","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|"],
              ["____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|"],
              ["____|","____|","____|","____|","____|","____|","____|","____|","Meta ","____|","____|","____|","____|","____|","____|","____|","____|"],
              ["____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|"],
              ["____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|","____|"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|"," B1 |"," B2 |","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"],
              ["*****","*****","*****","*****","*****","*****","____|","____|","____|","____|","____|","*****","*****","*****","*****","*****","*****"]]

menu()