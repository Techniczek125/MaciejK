***Zadanie 2.***
Wygeneruj dowolne ciąg arytmetyczny o kroku różnym od jeden i niebędący liczbą całkowitą, używając w tym celu funkcji *[arange](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html)* oraz *[linspace](https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linspace.html)*. Przeanalizuj otrzymane rezultaty.

#%%

#Tworzy ciąg na podstawie podanych odleglosci miedzy wyrazami ciagu, domyslnie skok o 1
print(np.arange(2., 36., step = 3.3))

#Tworzy ciag na podstawie podanej docelowej ilosci wyrazow ciagu, domyslnie 50 wyrazow
print(np.linspace(2., 36, num = 12, retstep=True))

***Zadanie3.***
Napisać funkcję $fib(n)$ zwracającą wektor pierszych n elementów * [ciągu Fibonnaciego](https: // pl.wikipedia.org / wiki / Ci % C4 % 85 g_Fibonacciego) *.

# %%

# ROZWIAZANIE

def fib(n):
    lista = [1, 1]

    while len(lista) < n:
        lista.append(lista[-2] + lista[-1])

    return lista


print(fib(8))


***Zadanie4.***
Zadeklaruj macierz:

$\mathbf{M} =\left[ \begin{matrix}
a & 1 & -a\\
0 & 1 & 1\\
-a & a & 1
\end{matrix}\right]
$
dla $a = \sqrt{2}$.

Dla zadeklarowanej macierzy wyznacz numerycznie macierz odwrotną $\mathbf{Minv}$, macierz transponowaną $\mathbf{Mt}$ i wyznacznik macierzy $\mathbf{Mdet}$. Wypisz otrzymane wyniki.
***Wskazówki:*** Do tworzenia obiektów mających własności macierzy w języku Python używa się klasy *[array](https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.array.html)* z pakietu *[numpy](http://www.numpy.org/)*, przykładowe użycie:

#%%

import numpy as np # słowo kluczowe "as" oznacza przesłania nazwę numpy i pozwala
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
A = np.array([[1,2],[3,4]])
print("Wektor poziomy:\n {0}".format(a))
print("Wektor pionowy:\n {0}".format(b))
print("Macierz:\n {0}".format(A))

#%% md

Do wykonania operacji odwracania macierzy należy użyć funkcji *[inv](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html)*, do obliczenia wyznacznika macierzy st

*Ciekawostka:* Python natywnie nie zawiera struktury danych typu tablica, na poziomie języka jest to rozwiązane poprzez strukturę listy list do której elementów odwołuje się poprzez indeksy jak w C/C++.

#%%

import numpy as np

M = np.array([[math.sqrt(2), 1, -math.sqrt(2)], [0, 1, 1], [-math.sqrt(2), math.sqrt(2), 1]])    #Macierz dana
Minv = np.linalg.inv(M)    #Macierz odwrotna
Mt = np.transpose(M)       #Macierz transponowana
Mdet = np.linalg.det(M)    #Wyznacznik

print(M)

#%% md

***Zadanie 6.***
Napisać funkcję $custom\_matrix(m, n)$, gdzie parametry m, n określają wymiary macierzy wynikowej, która
będzie wypełniona w/g algorytmu: jeśli indeks wiersza jest większy od indeksu kolumny
wartością komórki jest indeks wiersza, w przeciwnym wypadku wartością komórki jest indeks
kolumny. Na koniec wyświetlić wynikową macierz dla dowolnych argumentów $m$, $n$ z przedziału $\langle3,7\rangle$.

***Wskazówka:*** Inicjalizacja pustej macierz wykonywana jest w pakiecie Numpy przy pomocy funkcji  *[zeros](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.zeros.html)*, zaś macierzy składającej się z jedynek *[ones](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html)*. Wypełnienie macierzy można wykonać stosując pętle **for**.

#%%

# ROZWIAZANIE


def custom_matrix(m, n):
    base_matrix = np.zeros((m, n))  # inicjalizacja pustej macierzy

    #
    # Wersja gdy zwracamy indeksy liczac od (0,0)
    #

    for i in range(m):
        for j in range(n):
            if i > j:
                base_matrix[i, j] = i
            else:
                base_matrix[i, j] = j

    return base_matrix


#
# Wersja gdy zwracamy indeksy liczac od (1,1)
#
#     for i in range(m):
#         for j in range(n):
#             if i>j:
#                 base_matrix[i,j] = i+1
#             else:
#                 base_matrix[i,j] = j+1

#     return base_matrix

print(custom_matrix(4, 6))

# %%

zero_matrix = np.zeros((2, 2))
ones_matrix = np.ones((3, 1))

print('zero_matrix: \n{}'.format(zero_matrix))
print('ones_matrix: \n{}'.format(ones_matrix))

# %% md

***Zadanie 8.***
Zainicjalizować macierz $m_1$:

$m_1 = \begin{bmatrix}1&-7&3\\-12&3&4\\5&13&-3\end{bmatrix}$

Następnie wykonać operacje i wypisać ich wynik:
- $3m_1$
- $3m_1 + \begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}$
- $m_1^T$
- $m_1 \circ v_1$
- $v_2^T \circ m_1$

#%%

# ROZWIAZANIE

M1 = np.array([[1, -7, 3], [-12, 3, 4], [5, 13, -3]])

# Mnozenie macierzy przez skalar:
M1_3M = 3 * M1

# Dodawanie macierzy:
M1_s = 3 * M1 + np.ones([3, 3])
# M1_s = M1_3M + np.ones([3,3])

# Transpozycja macierzy:
M1_T = M1.T

# Mnozenie macierzowe:
M2_c = M1 @ v1
M3_c = v2 @ M1

# Wypisanie wynikow:
print('M1 =\n', M1)
print('\nM1_3M =\n', M1_3M)
print('\nM1_s =\n', M1_s)
print('\nM1_T =\n', M1_T)
print('\nM2_c =\n', M2_c)
print('\nM3_c =\n', M3_c)

#%% md

