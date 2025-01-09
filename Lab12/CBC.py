
import math

def xor(n1, n2):
    xor=''
    for i in range(len(n1)):
        xor+=str(int(n1[i])^int(n2[i]))
    return xor


def Ek(x_i, key, perm):
    
    y_i = xor(x_i, key)
    if perm>len(y_i):
        perm=perm%len(y_i)
    y_i=y_i[-perm:]+y_i[:-perm]
    return y_i

def Dk(y_i, key,perm):
    if perm>len(y_i):
        perm=perm%len(y_i)
    y_i=y_i[perm:]+y_i[:perm]
    x_i=xor(y_i,key)
    return x_i

#X jest listą bloków !! IV jest jakims blokiem inicjalizacyjnym
def CBC(X, key, IV,perm):
    Y=[IV]
    for i in range(len(X)):
        x_i = xor(X[i], Y[i]) 
        #print(x_i)
        Y.append(Ek(x_i, key,perm))
    Y=Y[1:]
    return Y

perm=9
X=['0101', '1000', '0000', '1011']
key='1110'
IV= '0110'

print(CBC(X,key, IV,perm))

# X_i=['0011', '0110', '0100','1110']
#y_i=['1101', '1000', '1010', '0000']
# Y=['1110', '0100','0101','0000']