#!/usr/bin/env python3

# A függvény eldönti, hogy a szám palindrom-e vagy sem.
def Palindrom(szam: int | str) -> bool:
    szam_str = str(szam)
    for i in range(len(szam_str) // 2):
        if szam_str[i] != szam_str[-i - 1]:
            return False
    return True

# Ez a függvény eldönti, hogy az input prím-e vagy sem.
def Primszam(szam: int) -> bool:
    if szam < 2:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False
    return True

# Ez a függvény megkeresi a legkisebb prímszámot, ami nagyobb, mint az input és palindrom is.
def Fuggveny(N: int) -> None:
    M = N
    while True:
        if Primszam(M) and Palindrom(M):
            print(M)
            break
        M += 1

# A main programrészben meghívjuk a függvényt.
def main() -> None:
    N = int(input("Adjon meg egy számot: "))
    Fuggveny(N)

if __name__ == "__main__":
    main()
