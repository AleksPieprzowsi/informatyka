#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Przedmiot:
Kierunek studiów:
Semestr:
Rok akademicki:
Data (dzień-miesiąc-rok):
Imię:
Nazwisko:
Numer albumu ZUT:
"""

import random

def wczytaj_plik(nazwa_pliku):  # Wczytuje dane do słownika (najpierw typu zbiór(set), później zamieniony na tuplę(tuple).
    slownik = set()
    with open(nazwa_pliku, "r", encoding="utf-8") as fh:
        dane = fh.readlines()

    for linia in dane:
        wyrazy = linia.split()
        for wyraz in wyrazy:
            wyraz = ''.join([znak for znak in wyraz if znak.isalpha()])  # Oczyszczenie słów z niepożądanych znaków.
            if len(wyraz) >= 5:
                slownik.add(wyraz)
    return tuple(slownik)

def znajdz_wyrazy(slownik):  # Szuka wyrazów do ułożenia krzyzówki
    def znajdz_wyraz(min_dlugosc):  # Znajduje wyraz (losowo) niekrótszy niż min_dlugosc
        rozmiar_slownika = len(slownik)
        wyraz  = ""
        while len(wyraz) < min_dlugosc:
            indeks = random.randint(0, rozmiar_slownika)
            wyraz = slownik[indeks].lower()
        return wyraz

    def dopasuj_wyraz(wyraz1, wyraz2):  # Dopasowuje wyrazy - szuka części wspólnej miedzy trzema wyrazami.
        indeks = 0
        wyraz = None
        zbior1 = set()
        zbior2 = set()
        while indeks < len(slownik):
            wyraz = slownik[indeks].lower()
            if len(wyraz) >= 7:
                pc_w = wyraz[1:int(len(wyraz)/2)]
                dc_w = wyraz[1+int(len(wyraz)/2):-1]
                p_zbior = set(pc_w)
                d_zbior = set(dc_w)
                if p_zbior.intersection(set(wyraz1[2:-2])):
                    if d_zbior.intersection(set(wyraz2[2:-2])):
                        zbior1 = p_zbior.intersection(set(wyraz1[2:-2]))
                        zbior2 = d_zbior.intersection(set(wyraz2[2:-2]))
                        break
            indeks += 1

        return (wyraz1, wyraz2, wyraz, zbior1, zbior2)

    wyraz1 = znajdz_wyraz(10)
    wyraz2 = znajdz_wyraz(10)
    return dopasuj_wyraz(wyraz1, wyraz2)

def wyswietl_krzyzowke(wyraz1, wyraz2, wyraz, zbior1, zbior2):  # Wyświetla krzyżówkę na ekranie
    print("\nKrzyżówka\n")
    print(f"\nDwa pierwsze wyrazy (wyświetlane poziomo): '{wyraz1}' i '{wyraz2}'. Trzeci, dobrany do nich wyraz (wyświetlany pionowo): '{wyraz}'.")
    print(f"( znaki wspólne z wyrazem 1: {zbior1} i wyrazem 2: {zbior2}. )")

    pn = len(wyraz) + 5
    pz = 41
    krzyzowka = [[" " for row in range(pz)] for col in range(pn)]

    for i in range(len(wyraz)):
        krzyzowka[i+2][20] = wyraz[i]

    znak1 = zbior1.pop()
    znak2 = zbior2.pop()
    wiersz = wyraz.index(znak1) + 2
    kolumna = 20 - wyraz1.index(znak1)

    for i in range(len(wyraz1)):
        krzyzowka[wiersz][i + kolumna] = wyraz1[i]

    wiersz2 = wyraz.rindex(znak2) + 2
    kolumna2 = 20 - wyraz2.rindex(znak2)

    for i in range(len(wyraz2)):
        krzyzowka[wiersz2][i + kolumna2] = wyraz2[i]

    for linia in krzyzowka:
        linia = ''.join(linia)
        print(linia)


slownik = wczytaj_plik("Wpustyniiwpuszczy.txt")
wyswietl_krzyzowke(*znajdz_wyrazy(slownik))
