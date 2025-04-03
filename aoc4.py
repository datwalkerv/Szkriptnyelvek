#!/usr/bin/env python3
# coding: utf-8

DATA = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

def is_valid_passphrase(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))  # Az ismétlődés ellenőrzése

def count_valid_passphrases(data):
    passphrases = data.strip().split("\n")  # Sorokra bontás
    valid_count = sum(1 for phrase in passphrases if is_valid_passphrase(phrase))
    return valid_count

def main():
    result = count_valid_passphrases(DATA)
    print(result)

if __name__ == '__main__':
    main()
