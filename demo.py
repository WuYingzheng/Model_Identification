import numpy as np
import pandas
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
y = np.zeros(len(x))
y[10:20] = 1

fig, ax = plt.subplots()
ax.plot(x, y)

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()

"""
x = pandas.read_csv('http://pastebin.com/raw.php?i=ksM4FvZS', skiprows=2, header=None).values
y = pandas.read_csv('http://pastebin.com/raw.php?i=0WhjjMkb', skiprows=2, header=None).values
fig, ax = plt.subplots()
ax.plot(x, y)

N = len(x)
total = x[N-1] - x[0]
T = total/N

yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.show()
"""