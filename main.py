import numpy as np
import matplotlib.pyplot as plt


"""
s = a0 + a1*t + a2*t*t + a3*t*t*t + a4*t*t*t*t + a5*t*t*t*t*t
ds = a1 + 2*a2*t + 3*a3*t*t + 4*a4*t*t*t + 5*a5*t*t*t*t
dds = 2*a2 + 2*3*a3*t + 3*4*a4*t*t + 4*5*a5*t*t*t
ddds = 2*3*a3 + 2*3*4*a4*t + 3*4*5*a5*t*t
dddds = 2*3*4*a4 + 2*3*4*5*a5*t
ddddds = 2*3*4*5*a5

s_T = 1
s_0 = ds_0 = ds_T = dds_0 = dds_T = 0

s_0 = 0 => a0 = 0
ds_0 = 0 => a1 = 0
dds_0 = 0 => a2 = 0

dds_T = 0 => 2*3*a3*T + 3*4*a4*T*T + 4*5*a5*T*T*T = 0 => /
    2*3*a3 + 3*4*a4*T + 4*5*a5*T*T = 0 => /
    a3 = -(1/6) * (3*4*a4*T + 4*5*a5*T*T) (1)

ds_T = 0 => 3*a3*T*T + 4*a4*T*T*T + 5*a5*T*T*T*T = 0 => /
    3*a3 + 4*a4*T + 5*a5*T*T = 0 => /
    a3 = -(1/3) * (4*a4*T + 5*a5*T*T) (2)
    
1,2 => -(1/6) * (3*4*a4*T + 4*5*a5*T*T) = -(1/3) * (4*a4*T + 5*a5*T*T) => /
    3*4*a4*T + 4*5*a5*T*T = 2 * (4*a4*T + 5*a5*T*T) => /
    3*4*a4 - 2*4*a4 = 2*5*a5*T - 4*5*a5*T => /
    a4 = -(5/2)*a5*T (3)
    
2,3 => a3 = -1/3(4*(-(5/2)*a5*T)*T + 5*a5*T*T) => /
    a3 = (5/3)*a5*T*T (4)
    
s_T = 1 => a3*T*T*T + a4*T*T*T*T + a5*T*T*T*T*T = 1 => /
    a3 + a4*T + a5*T*T = 1/(T*T*T) (5)

3,4,5 => ((5/3)*a5*T*T) + (-(5/2)*a5*T)*T + a5*T*T = 1/(T*T*T) => /
    (5/3)*a5*T*T - (5/2)*a5*T*T + a5*T*T = 1/(T*T*T) => /
    (1/6)*a5*T*T = 1/(T*T*T) => /
    a5 = 6/(T*T*T*T*T) (6)
    
3,6 => a4 = -(5/2)*(6/(T*T*T*T*T))*T => /
    a4 = -15/(T*T*T*T)
    
4,6 => a3 = (5/3)*(6/(T*T*T*T*T))*T*T => /
    a3 = 10/(T*T*T)
"""


def get_params(T):
    a0 = a1 = a2 = 0
    a3 = 10 / (T * T * T)
    a4 = -15 / (T * T * T * T)
    a5 = 6 / (T * T * T * T * T)
    return a0, a1, a2, a3, a4, a5


def calculate(t, a0, a1, a2, a3, a4, a5):
    s = a0 + a1*t + a2*t*t + a3*t*t*t + a4*t*t*t*t + a5*t*t*t*t*t
    ds = a1 + 2*a2*t + 3*a3*t*t + 4*a4*t*t*t + 5*a5*t*t*t*t
    dds = 2*a2 + 2*3*a3*t + 3*4*a4*t*t + 4*5*a5*t*t*t
    ddds = 2*3*a3 + 2*3*4*a4*t + 3*4*5*a5*t*t
    dddds = 2*3*4*a4 + 2*3*4*5*a5*t
    ddddds = 2*3*4*5*a5
    return s, ds, dds, ddds, dddds, ddddds


def main():
    T = 100

    t = np.linspace(0, T + 1)
    a0, a1, a2, a3, a4, a5 = get_params(T)

    s, ds, dds, ddds, dddds, ddddds = calculate(t, a0, a1, a2, a3, a4, a5)

    plt.figure(figsize=(10, 12))

    plt.subplot(3, 1, 1)
    plt.plot(t, s)
    plt.xlabel('t')
    plt.ylabel('s(t)')
    plt.title('Траектория')

    plt.subplot(3, 1, 2)
    plt.plot(t, ds)
    plt.xlabel('t')
    plt.ylabel('ds(t)')
    plt.title('Скорость')

    plt.subplot(3, 1, 3)
    plt.plot(t, dds)
    plt.xlabel('t')
    plt.ylabel('dds(t)')
    plt.title('Ускорение')

    plt.show()


if __name__ == "__main__":
    main()