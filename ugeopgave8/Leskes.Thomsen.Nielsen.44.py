from csvImageRead import *

def f(x, y):
    return x ** 2 + y ** 2


def gradient(v):
    return gradientx(v), gradienty(v)


def gradientx(v):
    n = v.__len__()
    vDy = []
    for i in range(n):
        vDy.append([])
        for j in range(n):
            if j < n-1:
                vDy[i].append(v[i-1][j] - v[i][j])
            else:
                vDy[i].append(0.0)
    return vDy

def gradienty(v):
    n = v.__len__()
    vDy = []
    for i in range(n):
        vDy.append([])
        for j in range(n):
            print j, n-1
            if j < n-1:
                vDy[i].append(v[i][j-1] - v[i][j])
            else:
                print(j)
                vDy[i].append(0.0)
    return vDy

fig = plt.figure()
ax = fig.gca(projection="3d")
plt.hold(True)
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
#z = gradienty(f(x, y))
z = gradientx(f(x, y))
#z = f(x, y)
print z
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha=0.2)
plt.show()

if __name__ == "__main__":
    pass