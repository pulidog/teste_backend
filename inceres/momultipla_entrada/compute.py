
from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob


# crie a funçao que calcule a equação indicada, que receva 4 parametros: (t, A, b, w)
# e retorne o valor de y


def compute(A, b, w, T, resolution=500):
    """Return filename of plot """
    print os.getcwd()
    t = linspace(0, T, resolution+1)
    # y = função que vc vai criar encima
    y =
    plt.figure()
    plt.plot(t, y)
    # coloca o titulo da grafica plt.title

    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)

    plotfile = os.path.join('static', str(time.time()) + '.png')
    plt.savefig(plotfile)

    # complete o return ou resposta da função
    return

if __name__ == '__main__':
    print compute(1, 0.1, 1, 20)

