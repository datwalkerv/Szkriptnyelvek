#!/usr/bin/env python3

def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    header = data[0]
    header_row = " | ".join(f"{header[i]:<{col_widths[i]}}" for i in range(len(header)))
    print(f"{header_row}")
    print("-" * (sum(col_widths) + 3 * (len(header) - 1)))
    for row in data[1:]:
        print(" | ".join(f"{row[i]:<{col_widths[i]}}" for i in range(len(row))))

def main():
    data = [
      ["Név", "Kor", "Egyenleg"],
      ["János", 28, 1234.567],
      ["Eszter", 34, 2345.678],
      ["Zoltán", 22, 3456.789]
    ]

    print_table(data)

if __name__ == "__main__":
    main()
