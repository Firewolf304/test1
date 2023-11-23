from typing import List, Any
import src.errors
import copy
from src.constructor import MatrixCnstructor
n = int(input("Enter y size: "))
m = int(input("Enter x size: "))
mass = []
for i in range(n):
    text = list(map(int,input("Enter the numbers : ").strip().split()))[:m]
    mass.append(text)
format = list(map(int,input("Enter format : ").strip().split()))[:m]
equality = list(map(int,input("Enter equality : ").strip().split()))[:m]
matrix = MatrixCnstructor(n,m,mass,format,equality)
matrix.make_based()
print("based =", matrix.based, "notbased =", matrix.notbased)
matrix.makeMatrix()
matrix.iterator()