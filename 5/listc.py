#!/usr/bin/env python3

def main():
    feladat1 = [word.upper() + '!' for word in ['auto', 'villamos', 'metro']]
    feladat2 = [word.capitalize() for word in ['aladar', 'bela', 'cecil']]
    feladat3 = [0 for _ in range(10)]
    feladat4 = [num * 2 for num in range(1, 11)]
    feladat5 = [int(num) for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]
    feladat6 = [int(char) for char in "1234567"]
    feladat7 = [len(word) for word in 'The quick brown fox jumps over the lazy dog'.split()]
    feladat8 = [word[0] for word in "python is an awesome language".split()]
    feladat9 = [(word, len(word)) for word in 'The quick brown fox jumps over the lazy dog'.split()]
    feladat10 = [num for num in range(10) if num % 2 == 0]
    feladat11 = [num**2 for num in range(20) if (num**2) % 2 == 0]
    feladat12 = [num**2 for num in range(20) if str(num**2).endswith('4')]
    feladat13 = ''.join([chr(code) for code in range(65, 91)])
    feladat14 = [word.strip() for word in [' apple ', ' banana ', ' kiwi']]
    feladat15 = ''.join([str(num) for num in [1, 0, 1, 1, 0, 1, 0, 0]])

    print(feladat1)
    print(feladat2)
    print(feladat3)
    print(feladat4)
    print(feladat5)
    print(feladat6)
    print(feladat7)
    print(feladat8)
    print(feladat9)
    print(feladat10)
    print(feladat11)
    print(feladat12)
    print(feladat13)
    print(feladat14)
    print(feladat15)


if __name__ == "__main__":
    main()