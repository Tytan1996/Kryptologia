
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
def CBC(X, key, IV,perm, mode="szyfr"):
    if mode=='szyfr':
        Y=[IV]
        for i in range(len(X)):
            x_i = xor(X[i], Y[i]) 
            #print(x_i)
            Y.append(Ek(x_i, key,perm))
        Y=Y[1:]
    if mode=='deszyfr':
        X.insert(0, IV)
        Y=[]
        for i in range(1, len(X)):
            x_i=Dk(X[i], key,perm)
            Y.append(xor(x_i, X[i-1])) 
    return Y
'''
perm=9
X=['1100001011011001110000100100000011011010110000100100000011010110', '1101111111101001110000100000000000000000000000000000000000000000']
key='1111000011110000111100001111000011110000111100001111000011110000'
IV= '1101011100111011001100100101110011001011110011100101011101111000'
#Zaszyfrowane bloki:  ['1010111101110010100010010000000001110110011100001111111001110011', '0100000111000000001101011101110111111000010000110100000000000111']

print('X', X)
Y= CBC(X,key, IV,perm)
print('szyfr', Y)
print('deszyfr', CBC(Y,key, IV,perm, mode="deszyfr"))
'''
# X_i=['0011', '0110', '0100','1110']
#y_i=['1101', '1000', '1010', '0000']
# Y=['1110', '0100','0101','0000']