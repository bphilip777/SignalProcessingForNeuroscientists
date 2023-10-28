import matplotlib.pyplot as plt 
import numpy as np 

s1 = np.random.randn(1000)
s2 = np.random.randn(1000)
st = s1 + s2

# Mean of joint = sum of mean of individual
m1 = np.mean(s1)
m2 = np.mean(s2)
mt = np.mean(st)

# Variance of joint = sum of var of individual
v1 = np.var(s1)
v2 = np.var(s2)
vt = np.var(st)

print(f"{m1} {m2} {mt}")
print(f"{v1} {v2} {vt}")
