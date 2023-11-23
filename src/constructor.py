class InputError(Exception):
    pass
import copy
from typing import List, Any
class MatrixCnstructor:
    def __init__(self, n:int, m:int, mass:list[list], format:list[Any], equality: list[Any]):
        self.based = []
        self.notbased = []
        self.format = format
        self.n = n
        self.m = m
        self.mass = mass
        self.equality = equality
        self.itermatrix: list[Any] = []
        self.old = None
        self.new = None
        self.bestIndexX = 0
        self.bestIndexY = 0
        if (len(mass[0]) != len(self.format)):
            raise InputError("Error input, this is size: " + str(len(mass[0])))
        pass
    def check(self, y:int, x:int) -> bool:
        """
        Проверка столбца на наличие единичной матрицы.
        Если есть что-то не 0 (не трогая строку (x,y)), то сброс
        :param y: рассмотр координаты относительно Y
        :param x: рассмотр координаты относительно X
        :return: успешность нахождения нулевого столбца
        """
        for Y in range(self.n):
            if (Y != y and self.mass[Y][x] != 0):
                return False
        return True
    def make_based(self):
        """
        Заполнение based и notbased переменных\n
        based - базисные переменные, что слева
        notbased - не базисные переменные, что сверху
        :return: None
        """
        for y in range(self.n):
            for x in range(self.m):
                if (self.mass[y][x] == 1 and self.check(y, x) and len(self.based) == y):
                    # based.insert(0,x)
                    self.based.append(x)
                if (len(self.based) == y or (self.mass[y][x] != 1 and not (self.check(y, x)))):
                    self.notbased.append(x)
        self.notbased = list(set([x for x in self.notbased if x not in self.based]))
    def makeMatrix(self):
        """
        Заполнение основной матрицы itermatrix (до make_based) \n
        А также заполнение new и old таблиц
        :return: None
        """
        for y in range(self.n):  # make start matrix
            self.itermatrix.append(list([]))
            for x in range(self.m):  # use Python methods!
                if (not (x in self.based)):
                    self.itermatrix[y].append(self.mass[y][x])
                    # summ[y] += mass[y][x] * format[based[y]]
            self.itermatrix[y].append(self.equality[y])
        self.itermatrix.append(list(map(lambda a, b: a - b, self.summ(), [self.format[x] for x in self.notbased] + [0])))
        # map(lambda a,b: a-b, summ, format[based[y]] )
        print("start = " + str(self.itermatrix))
        self.old = self.itermatrix
        self.new = [[ -1 for _ in range(len(self.itermatrix[0]))] for _ in range(len(self.itermatrix))]

    def summ(self) -> list[Any]:
        """
        Ищет сумму всех столбцов по формуле:          \n
        summ[x]+=itermatrix[y][x]*format[based[y]]    \n
        сумма      матрица        максимизация
        :return:
        """
        summ = [0] * (len(self.notbased) + 1)  # for F in end of matrix
        for x in range(len(summ)):
            for y in range(len(self.itermatrix)):
                summ[x] += self.itermatrix[y][x] * self.format[self.based[y]]
                # print(summ[x])
        return summ

    def changeBest(self):
        """
        Вычисление главных столбцов
        :return:
        """
        nig_mass = list(map(lambda a: abs(a), [x for x in self.old[-1][:-1] if x < 0]))  # all abs of negative values
        value = nig_mass.count(max(nig_mass))
        if (value > 1):  # if some values in the F
            listing: list[dict] = []
            def func(index: int) -> dict:
                bestIndY = 0
                val = 9999999
                for i in range(len(self.based)):
                    try:
                        if (val >= self.old[i][len(self.notbased)] / self.old[i][index] and self.old[i][index] > 0):
                            val = self.old[i][len(self.notbased)] / self.old[i][index]
                            bestIndY = i
                    except Exception:
                        pass
                return dict({'X': index, 'Y': bestIndY, 'val': val})

            # maximus = map( lambda a: a==max(nig_mass) ,  )
            save = 0
            for i in range(value):  # use python methods!
                save = nig_mass.index(max(nig_mass), save)
                listing.append(func(save))
            element = min(listing, key=lambda x: x['val'])
            self.bestIndexX = element['X']
            self.bestIndexX = element['Y']
            pass
        else:
            self.bestIndexX = self.old[-1].index(max(nig_mass) * -1)
            val = 9999999
            for i in range(len(self.based)):
                try:
                    if (val >= self.old[i][len(self.notbased)] / self.old[i][self.bestIndexX] and self.old[i][self.bestIndexX] > 0):
                        val = self.old[i][len(self.notbased)] / self.old[i][self.bestIndexX]
                        self.bestIndexY = i
                except Exception:
                    pass
        print('best coords (x y):', self.bestIndexX, self.bestIndexY)
    def iterator(self):
        while (not (all(map(lambda x: x >= 0, self.new[-1][:-1])))):
            self.new = [[0 for _ in range(len(self.itermatrix[0]))] for _ in range(len(self.itermatrix))]
            maxInd = 0
            val = 0
            self.bestIndexX = 0
            self.bestIndexY = 0

            self.changeBest()
            self.new[self.bestIndexY][self.bestIndexX] = float(1 / self.old[self.bestIndexY][self.bestIndexX])

            # заебали эти вумные методы, я в тупую
            for y in range(len(self.new)):
                if y != self.bestIndexY:
                    self.new[y][self.bestIndexX] = self.old[y][self.bestIndexX] * self.new[self.bestIndexY][self.bestIndexX] * (-1)
            for x in range(len(self.notbased) + 1):
                if x != self.bestIndexX:
                    self.new[self.bestIndexY][x] = float(self.old[self.bestIndexY][x] * self.new[self.bestIndexY][self.bestIndexX])

            for y in range(len(self.new)):
                for x in range(len(self.new[y])):
                    if (y != self.bestIndexY and x != self.bestIndexX):
                        self.new[y][x] = (self.old[y][x] * self.old[self.bestIndexY][self.bestIndexX] - self.old[self.bestIndexY][x] * self.old[y][
                            self.bestIndexX]) / self.old[self.bestIndexY][self.bestIndexX]

            self.old = copy.copy(self.new)
            print(self.new)
            # test +=1
            pass