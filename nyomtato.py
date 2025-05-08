#!/usr/bin/env python3

# Az alábbi függvény visszaadja a nyomtatni kívánt konkrét oldalakat. Pl.: 1,2,3,5-7,12,14-17 -> 1,2,3,5,6,7,12,14,15,16,17
def nyomtatas() -> str:
    s: str = input("Adja meg a nyomtatni kívánt oldalakat: ")
    s = s.split(",")
    result: list[str] = []
    for i in s:
        if "-" in i:
            i2 = i.split("-")
            for j in range(int(i2[0]), int(i2[1]) + 1):
                result.append(str(j))
        else:
            result.append(i)
    return ",".join(result)

# A main programrészben meghívjuk a függvényt és kiíratjuk a visszatérési értékét.
def main() -> None:
    print(Nyomtatas())

if __name__ == "__main__":
    main()
