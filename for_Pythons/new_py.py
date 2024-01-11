import numpy as np
import matplotlib.pyplot as plt
ps=int(input())
h=int
i=int
j=int
k=int
b=int
#Julia fractal for lab_1
def julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    x, y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))
    z = x + 1j * y
    img = np.zeros(z.shape, dtype=float)
    
    for i in range(max_iter):
        z = z**2 + c
        mask = np.abs(z) < 1000
        img += mask
    
    img = np.log(img + 1)  # Добавляем логарифм для визуализации (imported numpy and matplotlib)
    return img

def plot_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    img = julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)
    
    plt.imshow(img, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.title(f'Julia Set with c = {c}')
    plt.show()

# Пример фрактала
width, height = 800, 800
xmin, xmax = -2, 2
ymin, ymax = -2, 2
c = complex(-0.777, 0.25016)
max_iter = 300

plot_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)
#Factorial code for lab_1
def fact(b):
    if b==0 or b==1: return 1
    else:
        
        return b*fact(b-1)
    
   
def fact2(h):
    if h==0 or h==1: return 1
    else:
        
        return h*fact2(h-1)
    
def fact3(i):
    if i==0 or i==1: return 1
    else:
        
        return i*fact3(i-1)
    
def fact4(j):
    if j==0 or j==1: return 1
    else:
        
        return j*fact4(j-1)
    
def fact5(k):
    if k==0 or k==1: return 1
    else:
        
        return k*fact5(k-1)
 
    

s=fact(ps)   
p=s+s
s=fact2(ps)
p=p+s
s=fact3(ps)
p=p+s     
s=fact4(ps)
p=p+s
s=fact5(ps)
p=p+s
print('summ of 5 factorials is:',p)
    

