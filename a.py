import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

class Palet:
    __L = 10
    __W = 10
    __H = 10
    __place = np.zeros((__L, __W, __H))
    __box = 1

    def palet_show(self):

        # print(self.__place)
        return self.__place

    def check_place(self, a, b, c):
        empty_space = 0
        full = False
        for e in range(self.__H):
            for i in range(self.__W):
                for j in range(self.__L):
                    if self.__place[i][j][e] == 0:
                        for z in range(a):
                            for q in range(b):
                                for t in range(c):
                                    if i + a <= self.__L and j + b <= self.__W and e + c <= self.__H:
                                        if self.__place[i + z][j + q][e + t] != 0:
                                            full = True
                                    else:
                                        full = True
                        if not full:
                            for m in range(e):
                                for n in range(b):
                                    for v in range(a):
                                        if e > 0:
                                            if self.__place[i + v][j + n][e - m - 1] == 0:
                                                empty_space += 1

                                        else:
                                            empty_space = 0

                            return i, j, e, empty_space

                full = False
        return 0, 0, 0, 10 * 10 * 10

    def add_box(self, x, y, z, a, b, c):

        self.__place[int(x):int(x + a), int(y):int(y + b), int(z):int(z + c)] = self.__box
        self.__box += 1
        return x, y, z


if __name__ == '__main__':
    box_param = np.zeros((6, 4))
    Z = np.matrix('0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0')
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k',]
    V = 0
    empty_space = 0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    P = Palet()
    try:
        file = open('dataa.txt', 'r')
        file.close()
    except IOError:
        nums = ['1 1 1']
        file = open('dataa.txt', 'w')
        for i in nums:
            file.write(str(i) + '\n')
        file.close()

    file = open('dataa.txt', 'r')
    box_data = file.read()
    box_data = box_data.split('\n')
    random.shuffle(box_data)
    print(box_data)
    box_number = len(box_data)
    for box in range(int(box_number)):

        box_size = box_data[box].split()
        a = int(box_size[0])
        b = int(box_size[1])
        c = int(box_size[2])
        V = V + a * b * c
        max_val = 10 * 10 * 10
        min_x = 0
        box_placed = False

        abc = [[a, b, c], [b, a, c], [a, c, b], [b, c, a], [c, a, b], [c, b, a]]
        for l in range(1):
            a, b, c = abc[l][:]
            box_param[l][:] = P.check_place(a, b, c)
            if box_param[l][3] == 0:
                x, y, z = P.add_box(box_param[l][0], box_param[l][1], box_param[l][2], a, b, c)
                box_placed = True
                break
            elif box_param[l][3] < max_val:
                min_x = l
                max_val = box_param[l][3]

        if not box_placed:

            if max_val >= 10 * 10 * 10:
                raise ValueError("Нет места для размещения")
            a, b, c = abc[min_x][:]
            x, y, z = P.add_box(box_param[min_x][0], box_param[min_x][1], box_param[min_x][2], a, b, c)
        if not (max_val >= 10 * 10 * 10):
            empty_space = empty_space + max_val

        Z[0, :] = x, y, z
        Z[1, :] = x + a, y, z
        Z[2, :] = x + a, y + b, z
        Z[3, :] = x, y + b, z
        Z[4, :] = x, y + b, z + c
        Z[5, :] = x + a, y, z + c
        Z[6, :] = x + a, y + b, z + c
        Z[7, :] = x, y, z + c

        ax.scatter(Z[:, 0], Z[:, 1], Z[:, 2])
        ax.plot_wireframe(Z[:, 0], Z[1, 1], Z[:, 2], color=colors[box])
        ax.plot_wireframe(Z[1, 0], Z[:, 1], Z[:, 2], color=colors[box])
        ax.plot_wireframe(Z[0, 0], Z[:, 1], Z[:, 2], color=colors[box])
        ax.plot_wireframe(Z[:, 0], Z[2, 1], Z[:, 2], color=colors[box])
        ax.plot_wireframe(Z[2, 0], Z[0, 1], Z[:, 2], color=colors[box])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    print(empty_space)
    print(V/1000)
    print(empty_space/(1000 - V))
    plt.show()

