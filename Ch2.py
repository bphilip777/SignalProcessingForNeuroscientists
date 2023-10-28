# py -m venv env_name
# "./venv_name/Scripts/activate"
import numpy as np
import matplotlib.pyplot as plt 


# Aliasing
# Idea that if you don't sample your signal sufficiently, you record different signal
f = 20
t = np.linspace(0, 1, 1001)
# print(t)
# print(t.shape)

signal = np.sin(2 * np.pi * f * t)

fig, axs = plt.subplots(11,1)
axs[0].plot(t, signal, 'r')
axs[0].set_xlim(t[0], t[-1])
axs[0].set_ylabel(f"{int((len(t)-1))}")
idx = 1
for skip in range(2, 50, 5):
    nt = t[::skip]
    ns = signal[::skip]
    # print(nt.shape)
    # print(ns.shape)
    axs[idx].plot(nt, ns, 'b')
    axs[idx].scatter(nt, ns)
    axs[idx].set_xlim(t[0], t[-1])
    axs[idx].set_ylabel(f"{int((len(t)-1) / skip)}")
    idx += 1
axs[idx-1].set_xlabel("Time, ms")
plt.show()

# print(nsignals)
