import os
TEMPLATES = {
    "1": ("alap.py", """#!/usr/bin/env python3

def main():
    print('Py3')

##############################################################################

if __name__ == "__main__":
    main()
"""),
    "2": ("alap.c", """#include <stdio.h>

int main() {
    printf("Hello, C!\\n");
    return 0;
}
"""),
}

def main():
    while True:
        print("\n---------------------------")
        print("Create an empty source file")
        print("---------------------------")
        print("1) Python [py]")
        print("2) C      [c]")
        print("q) quit")
        choice = input("> ").strip()

        if choice == "q":
            print("Kilépés...")
            break
        elif choice in TEMPLATES:
            filename, content = TEMPLATES[choice]
            if os.path.exists(filename):
                print(f"Hiba: A '{filename}' már létezik!")
            else:
                with open(filename, "w") as f:
                    f.write(content)
                print(f"'{filename}' sikeresen létrehozva!")
        else:
            print("Érvénytelen választás, próbáld újra.")

if __name__ == "__main__":
    main()
