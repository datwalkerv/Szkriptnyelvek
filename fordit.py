#!/usr/bin/env python3

def fordit(n: int) -> int:
    return int(str(n)[::-1])

def main():
    print(fordit(1969))

if __name__ == "__main__":
    main()
