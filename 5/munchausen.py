#!/usr/bin/env python3

def is_munchausen(n):
    return n == sum(int(digit) ** int(digit) if int(digit) > 0 else 0 for digit in str(n))


def main():
    munchausen_numbers_under_10000 = [n for n in range(10000) if is_munchausen(n)]
    print("10 000-nél kisebb Münchausen-számok:", munchausen_numbers_under_10000)

    munchausen_numbers = [n for n in range(440000000) if is_munchausen(n)]
    print("Összes Münchausen-szám:", munchausen_numbers)



if __name__ == "__main__":
    main()