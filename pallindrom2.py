#!/usr/bin/env python3

# A függvény eldönti, hogy a szám palindrom-e vagy sem.
def Palindrom(szam: int | str) -> bool:
    szam_str = str(szam)
    for i in range(len(szam_str) // 2):
        if szam_str[i] != szam_str[-i - 1]:
            return False
    return True

# Ez a függvény visszaadja a számok összegét, amik palindromok decimálisan és binárisan is.
def Fuggveny(N: int) -> int:
    result = 0
    for i in range(1, N):
        if Palindrom(i) and Palindrom(bin(i)[2:]):
            result += i
    return result

# A main programrészben meghívjuk a függvényt és kiíratjuk a visszatérési értékét.
def main() -> None:
    print(Fuggveny(1000000))

if __name__ == "__main__":
    main()
