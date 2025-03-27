#!/usr/bin/env python3

def loop(n, debug=False):
    if debug:
        print("# ciklus kezdete:")
    
    for i in range(1, n + 1):
        print(i, end=" ")
    
    if debug:
        print("\n# ciklus vége")

def main():
    loop(5) 
    print()
    loop(5, debug=True)

if __name__ == "__main__":
    main()
