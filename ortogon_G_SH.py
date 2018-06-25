import numpy as np

scal = lambda x,y: np.sum([i_*j_ for i_,j_ in zip(x,y)])
norm2 = lambda x: np.sqrt(scal(x,x))
d_pr = lambda a,e,a0: [a[ii] - e[ii]*scal(a0,e)/scal(e,e) for ii in np.arange(len(a))]

n,m = map(int,input().split())
a_ = [[int(j) for j in input().split()] for _ in np.arange(n)]

a = np.array(a_,np.float128)
f = np.zeros(n,np.float128)
e = np.zeros((n,m),np.float128).T
e,f = a[:,:m].T,a[:,-1]
e0 = np.array(e,np.float128)

for i in np.arange(m):
    e[i] = e0[i]
    for j in np.arange(0,i):
        e[i] = d_pr(e[i],e[j],e0[i])
for i in np.arange(m):
    e[i] /= norm2(e[i])

for i in np.arange(m):
    print(e[i]), end=' ')