import numpy as np
import matplotlib.pyplot as plt
class Palet:
    __place = np.zeros((30, 40))
    __box = 1
    def palet_show(self):
        print(self.__place)
        return self.__place
    def add_box(self, a, b):
        full = False
        for i in range(30):
            for j in range(40):
                if self.__place[i][j] == 0:
                    for z in range(a):
                        for q in range(b):
                            if i + a <= 30 and j + b <= 40:
                                if self.__place[i + z][j + q] != 0:
                                    full = True
                            else:
                                full = True
                    if not full:
                        self.__place[i:i+a, j:j+b] = self.__box
                        self.__box += 1
                        coordx = i
                        coordy = j
                        return coordx, coordy


                full = False
        return 666, 666






if __name__ == '__main__':
    P = Palet()
    P.add_box(4, 15)
    P.add_box(3, 25)
    P.add_box(2, 24)
    P.add_box(6, 20)
    P.add_box(4, 30)
    P.add_box(2, 10)
    P.add_box(5, 15)
    P.add_box(4, 25)
    P.add_box(7, 8)
    P.add_box(8, 14)
    P.add_box(3, 7)
    P.add_box(7, 4)
    P.add_box(3, 6)
    P.add_box(8, 5)
    P.add_box(7, 6)
    file = open('data.txt', 'w')

    file.write(str(P.palet_show()))
    file.close()

    box = P.palet_show()
    np.save('box', box)
    plt.imshow(P.palet_show())
    plt.show()