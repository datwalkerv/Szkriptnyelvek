#!/usr/bin/env python3

def char_distance(a, b):
    return str(abs(ord(a) - ord(b)))

def main():
    characters = [('a', 'c'), ('a', 'a'), ('a', 'c'), ('a', 'f')]
    result = ''.join(char_distance(a, b) for a, b in characters)
    print(result)

if __name__ == "__main__":
    main()
