import numpy as np
from scipy.linalg import lu

# Metode Matriks Balikan
def inverse_matrix_method(A, b):
    A_inv = np.linalg.inv(A)
    return np.dot(A_inv, b)

# Metode Dekomposisi LU Gauss
def lu_decomposition_method(A, b):
    P, L, U = lu(A)
    y = np.linalg.solve(np.dot(P, L), b)
    return np.linalg.solve(U, y)

# Metode Dekomposisi Crout
def crout_decomposition_method(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.eye(n)
    for j in range(n):
        for i in range(j, n):
            L[i, j] = A[i, j] - L[i, :j] @ U[:j, j]
        for i in range(j+1, n):
            U[j, i] = (A[j, i] - L[j, :j] @ U[:j, i]) / L[j, j]
    y = np.linalg.solve(L, b)
    return np.linalg.solve(U, y)

# Banner program
print("=== PROGRAM PENYELESAIAN PERSAMAAN LINIER ===")
print("=== ADI NUR FI YAN - 21120122120010 ===")
print("==== MATA KULIAH METODE NUMERIK KELAS B ====")

# Meminta input dari pengguna
n = int(input("Masukkan ukuran matriks: "))
A = np.zeros((n, n))
print("Masukkan elemen-elemen matriks A(masukkan 1per 1 angka lalu enter):")
for i in range(n):
    for j in range(n):
        A[i, j] = float(input(f"Elemen baris {i+1}, kolom {j+1}: "))
b = np.zeros(n)
print("Masukkan elemen-elemen vektor b(masukkan 1per 1 angka lalu enter):")
for i in range(n):
    b[i] = float(input(f"Elemen {i+1}: "))

# Meminta pengguna memilih metode
print("Pilih metode solusi: matriks balikan (1), dekomposisi LU Gauss (2), dekomposisi Crout (3)")
choice = int(input("Pilihan Anda: "))
if choice == 1:
    print("Solusi dengan metode matriks balikan:", inverse_matrix_method(A, b))
elif choice == 2:
    print("Solusi dengan metode dekomposisi LU Gauss:", lu_decomposition_method(A, b))
elif choice == 3:
    print("Solusi dengan metode dekomposisi Crout:", crout_decomposition_method(A, b))
else:
    print("Pilihan tidak valid.")
