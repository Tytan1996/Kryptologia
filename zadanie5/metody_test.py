from matplotlib import pyplot as plt
from time import time_ns
from metody import potega


def potega_test():
    P = [491, 4523, 30011, 144773] 
    g=13
    fig, ax =plt.subplots(2,2)
    e=[]
    for i in range(4):
        p=P[i]
        x=[]
        y1=[]
        y2=[]
        step=10**i
        print(p)
        for a in range(1,p,step):
            x.append(a)
            t1=time_ns()
            w=(g**a)%p
            y1.append(time_ns()-t1)
            
            t1=time_ns()
            w2=potega(g, a, p)
            y2.append(time_ns()-t1)

            if w!=w2:
                e.append({'p':p, 'a':a, 'correct':w, 'result':w2})
            
         

        if i<2:
            ax[0,i].plot(x, y2, 'b', label='potega(g, a, p)')
            ax[0,i].plot(x, y1, 'r', label='$g^a (mod\ p)$', lw=0.5)
            
            ax[0,i].set_ylabel('time [ns]')
            ax[0,i].set_xlabel('a')
            ax[0, i].set_title(f'g={g}, p={p}')
            ax[0,i].legend()
            
        else:
            ax[1,i%2].plot(x, y2, 'b', label='potega(g, a, p)')
            ax[1,i%2].plot(x, y1, 'r', label='$g^a (mod p)$', lw=0.5)
            
            ax[1,i%2].set_ylabel('time [ns]')
            ax[1,i%2].set_xlabel('a')
            ax[1, i%2].set_title(f'g={g}, p={p}')

    
    plt.show()
    print(len(e))
    return e

e=potega_test()
print(e)


