# -*- coding: UTF-8 -*-

#kapital = input("Podaj wartość kapitału początkowego: ")

print("Program oblicz sumę odsetek z lokaty")

kapital = float(input("Wprowadź kapitał początkowy: "))
opr = float(input("Wprowadź oprocenotwanie loakty (np. 2.7 == 2.7%): "))
liczbaLat = float(input("Wprowadź okres lokaty: "))

"""
Założenia:
    --kapitalizacja odsetek następuje co miesiac
    --oprocenowanie podawane jest jako % poczym zamieniany jest na ułamek dziesiętny
    --liczbaLat może zostać podana jako ułamek dziesiętny np. 0.25 - oznacza 3 miesięca; 0.3333 oznacza 4 miesiace 
"""

odsetki = ((1+(opr/100)/12)**(12*liczbaLat)-1)*kapital
inflacja = ((1+2.5/100)**liczbaLat-1)*kapital;

print("Twoje początkowe {:.2f}zł przez {:.2f} lat na lokacie {:.2f}% urośnie do {:.2f}" .format(kapital, liczbaLat, opr, odsetki+kapital))
print("-"*50)
print("Kapitał początkowy:      {:15.2f} zł".format(kapital))
print("Oprocentowanie:          {:15.2f}".format(opr))
print("Okres lokaty:            {:15.2f}".format(liczbaLat))
print("Odsetki brutto:          {:15.2f} zł".format(odsetki))
print("Odsetki netto:           {:15.2f} zł".format(odsetki*0.81))
print("-"*50)
print("Kapitał po {:.2f} latach:      {:15.2f} zł".format(liczbaLat,odsetki*0.81+kapital))
print("Wartość nabywcza po {:.2f} latach i uwzględnieniu średniej inflacji(2.5%): {:.2f}".format(liczbaLat,odsetki*0.81+kapital-inflacja))
