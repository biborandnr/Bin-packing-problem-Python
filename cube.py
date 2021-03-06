import numpy as np
import matplotlib.pyplot as plt
import math
import random
class Palet:
    __L = 60
    __W = 40
    __H = 100
    __place = np.zeros((__L, __W, __H))
    __box = 1

    def palet_show(self):


        return self.__place

    def check_place(self, a, b, c):

        full = False
        empty_space = 0
        for e in range(self.__H):
            for i in range(self.__L):
                for j in range(self.__W):
                    if i + a - 1 < self.__L and j + b - 1 < self.__W and e + c - 1 < self.__H:
                        if self.__place[i][j][e] == 0 and self.__place[i + a - 1][j][e] == 0 and self.__place[i][j + b - 1][e] == 0 and self.__place[i + a - 1][j + b - 1][e] == 0:
                            for z in range(a):
                                for q in range(b):
                                    for t in range(c):
                                        if self.__place[i + z][j + q][e + t] != 0:
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
        return 0, 0, 0, 60 * 40 * 100

    def add_box(self, x, y, z, a, b, c):

        self.__place[int(x):int(x + a), int(y):int(y + b), int(z):int(z + c)] = self.__box
        self.__box += 1
        return x, y, z


if __name__ == '__main__':
    box_param = np.zeros((6, 4))
    Z = np.matrix('0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0 ; 0 0 0')
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c','r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c', 'm', 'y', 'k','b', 'c', 'm', 'y', 'k', 'r', 'g', 'b', 'c']
    V = 0
    empty_space = 0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    P = Palet()
    try:
        file = open('data.txt', 'r')
        file.close()
    except IOError:
        nums = ['1 1 1']
        file = open('data.txt', 'w')
        for i in nums:
            file.write(str(i) + '\n')
        file.close()

    file = open('data.txt', 'r')
    box_data = file.read()
    box_data = box_data.split('\n')
    random.shuffle(box_data)
    print(box_data)
    box_number = len(box_data)



    for box in range(int(box_number)):

        box_size = box_data[box].split()
        a = math.ceil(int(box_size[0])/20)
        b = math.ceil(int(box_size[1])/20)
        c = math.ceil(int(box_size[2])/20)
        V = V + a * b * c
        max_val = 60 * 40 * 100
        min_x = 0
        box_placed = False

        abc = [[a, b, c], [b, a, c], [a, c, b], [b, c, a], [c, a, b], [c, b, a]]
        for l in range(2):
            a, b, c = abc[l][:]
            box_param[l][:] = P.check_place(a, b, c)
            if box_param[l][3] == 0:
                x, y, z = P.add_box(box_param[l][0], box_param[l][1], box_param[l][2], a, b, c)
                box_placed = True
                break
            elif box_param[l][3] != 0 and box_param[l][3] < max_val:
                min_x = l
                max_val = box_param[l][3]

        if not box_placed:

            if max_val >= 60 * 40 * 100:
                raise ValueError("?????? ?????????? ?????? ????????????????????")
            a, b, c = abc[min_x][:]
            x, y, z = P.add_box(box_param[min_x][0], box_param[min_x][1], box_param[min_x][2], a, b, c)
        if not (max_val >= 60 * 40 * 100):
            empty_space = empty_space + max_val
        print(str(x) + ' ' + str(y) + ' ' + str(z))

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
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_zlim(0, 100)
    print(empty_space)
    print(V/(60 * 40 * 100))
    print(empty_space/(60*40*100 - V))

    plt.show()