from random import randrange

ilosc_prob = 10
poprawne = 0
odpowiedz = ""

for _ in range (ilosc_prob):
    liczba = randrange(10)+1

    # petla w celu wyeliminowania zlego wejscia uzytkownika
    while(True):
        odpowiedz = input("Czy liczba jest liczba poarzysta? (t/n)")
        if odpowiedz != "t" and odpowiedz != "n":
            print("Zle wejscie! Podaj odpowiedz jeszcze raz.")
        else:
            break
    
    # jesli odpowiedz sie zgadza, to dodaj do wyniku 1
    if (odpowiedz == "t" and liczba%2 == 0) or (odpowiedz == "n" and liczba%2 != 0):
        poprawne += 1

print("Trafnosc odpowiedzi: ", (float(poprawne)/ilosc_prob)*100, "%")