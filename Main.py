
kontrolNokta = [
    [[0.25, 0.5, 0.75, 1], [0.25, 1.4, 0.45, 1], [0.25, 1.1, 0.25, 1]],
    [[0.45, 0.5, 0.75, 1], [0.45, 1.4, 0.45, 1], [0.45, 1.1, 0.25, 1]],
    [[0.8, 0.5, 0.75, 1], [0.8, 1.4, 0.45, 1], [0.8, 1.1, 0.25, 1]],
    [[1.25, 0.5, 0.75, 1], [1.25, 1.4, 0.45, 1], [1.25, 1.1, 0.25, 1]]
]

izometrikMatris = [[0.707,-0.408,0,0],
                   [0,0.816,0,0],
                   [-0.707,-0.408,0,0],
                   [0,0,0,1]]

def Faktoriyel(n):
    toplam = 1
    for i in range(1,n + 1):
        toplam *= i
    return toplam

def Kombinasyon(n,r):
    return  Faktoriyel(n) // (Faktoriyel(r) * Faktoriyel(n - r))

def Matris_Carpim(A, B):
    satirA = len(A)
    sutunA = len(A[0])
    sutunB = len(B[0])
    C = []
    for i in range(satirA):
        C.append([])
        for j in range(sutunB):
            toplam = 0
            for k in range(sutunA):
                toplam += A[i][k] * B[k][j]
            C[i].append(toplam)
    return C

def Bernstein(i,n,u):
    return Kombinasyon(n, i) * (u ** i) * ((1 - u) ** (n - i))

def Bezier_Yuzey(u,w):
    x = 0
    y = 0
    z = 0
    for i in range(4):
        for j in range(3):
            bn = Bernstein(i,3,u)
            bm = Bernstein(j,2,w)
            P = kontrolNokta[i][j]

            x += bn * bm * P[0]
            y += bn * bm * P[1]
            z += bn * bm * P[2]

    return x,y,z
def main():
    P0x, P0y, P0z = Bezier_Yuzey(0.35, 0.85)
    P1x, P1y, P1z = Bezier_Yuzey(0, 1)

    P0 = [[P0x, P0y, P0z, 1]]
    P1 = [[P1x, P1y, P1z, 1]]

    P0_Izometrik = Matris_Carpim(P0,izometrikMatris)
    P1_Izometrik = Matris_Carpim(P1,izometrikMatris)

    print(f"P0 için x = {P0[0][0]:8.5f} y = {P0[0][1]:8.5f} z = {P0[0][2]:8.5f}")
    print(f"P1 için x = {P1[0][0]:8.5f} y = {P1[0][1]:8.5f} z = {P1[0][2]:8.5f}")


    print("             İzometrik İzdüşüm sonrası:")

    print(f"P0 için x = {P0_Izometrik[0][0]:8.5f} y = {P0_Izometrik[0][1]:8.5f} z = {P0_Izometrik[0][2]:8.5f}")
    print(f"P1 için x = {P1_Izometrik[0][0]:8.5f} y = {P1_Izometrik[0][1]:8.5f} z = {P1_Izometrik[0][2]:8.5f}")


main()