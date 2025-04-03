#!/usr/bin/env python3
# coding: utf-8

TEXT = """A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.
A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.
A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre."""

def remove_accents(text):
    accent_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ö': 'o', 'ő': 'o', 
        'ú': 'u', 'ü': 'u', 'ű': 'u'
    }
    new_text = ""
    for char in text:
        if char in accent_map:
            new_text += accent_map[char]
        else:
            new_text += char
    return new_text

def main():
    transformed_text = remove_accents(TEXT)
    print(transformed_text)

if __name__ == '__main__':
    main()
