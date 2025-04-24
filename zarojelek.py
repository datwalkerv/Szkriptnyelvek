#!/usr/bin/env python3
# encoding: utf-8


def zarojeles(kifejezes):
    zarojelek = []
    for i in kifejezes:
        if i == "{" or i == "(" or i == "[":
            zarojelek.append(i)
        elif i == "}" or i == ")" or i == "]":
            if len(zarojelek) == 0:
                return False
            elif i == "}" and zarojelek[-1] == "{":
                zarojelek.pop()
            elif i == ")" and zarojelek[-1] == "(":
                zarojelek.pop()
            elif i == "]" and zarojelek[-1] == "[":
                zarojelek.pop()
            else:
                return False
    if len(zarojelek) == 0:
        return True
    else:
        return False


def main():
    print(zarojeles("((5+3)*2+1)"))
    print(zarojeles("{[(3+1)+2]+}"))
    print(zarojeles("(3+{1-1)}"))
    print(zarojeles("[1+1]+(2*2)-{3/3}"))
    print(zarojeles("(({[(((1)-2)+3)-3]/3}-3)"))


if __name__ == "__main__":
    main()
