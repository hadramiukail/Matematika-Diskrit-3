#Studi Kasus 1
import numpy as np

#Diberikan Matriks:
M1 =np.array([[1, 3, 2],[4, 1, 6]])
M2 =np.array([[2, 1, 3],[0, 5, 2]])

#Penjumlahan Matriks
M_tambah = M1 + M2
print("pemjumlahan matriks:")
print(M_tambah)

#Pengurangan Matriks
M_kurang = M1-M2
print("pengurangan matris:")
print(M_kurang)

#Transpose
M_transpose = M1.T
print("matriks transpose:")
print(M_transpose)

#Perkalian Matriks dengan Transpose
M_perkalian = M1 @ M2.T
print("perkalian matriks:")
print(M_perkalian)