
# coding: utf-8

# # Binomial Expansion
# ## Erick David Rodriguez O. & Jose Ramon Valdes B.

# In[1]:

def Pascal(n):
 
    lista = [[1],[1,1]]
    for i in range(1,n):
        linea = [1]
     
        for j in range(0,len(lista[i])-1):
 
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        
        linea += [1]
         
        lista.append(linea)
  
    return lista
 
try:
    n = int(input("(X +Y)^ "))
    resultado = Pascal(n)
    print('Coeficientes (Triangulo de pascal)')
    for i in resultado:
        
        print (i)
except:
    print ("\n Ingresa un valor")
    
    
x = []
y = []
v=1
k=0
z=n
for v in range(0,n+1):

    x.append(z)
    y.append(k)
    k=k+1
    z=z-1
    

print('\n \n \n')
print('Exponentes de X & Y')
print(x)
print(y)




print('\n \n \n')
v=1
j=0
i=0
for v in range(0,n+1):
    print(resultado[n][j],'* X ^',x[i],'* Y ^',y[i],'+')
    i=i+1
    j=j+1 


# In[ ]:



