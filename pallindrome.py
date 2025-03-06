#!/usr/bin/env python3

def isPallindrome(a):
  return a.lower()==a[::-1].lower()

def main():
    name="Anna"
    print(isPallindrome(name))

if __name__ == "__main__":
    main()
