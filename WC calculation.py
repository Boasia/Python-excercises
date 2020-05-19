#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
#pytam o ilośc osób na piętrze budynku, 
#eliminuję błedne wprowadzenia danych

#assert(float(ludzie)> 0, "Blad")

try:
  ludzie=input("Ile osób znajduje się na piętrze?\n")
  ludzie=float(ludzie)
except ValueError:
  print("Błąd. Podaj poprawnie liczbę.")
  ludzie=input("Ile osób znajduje się na piętrze?\n")
  ludzie=float(ludzie)
else:
  while ludzie<=0:
    print("Błąd. Podaj poprawnie liczbę.")
    ludzie=input("Ile osób znajduje się na piętrze?\n")
    ludzie=float(ludzie)

print("\n")

#dzielę ludzi na kobiety i mezczyzn
kobiety=float(ludzie/2.0)
mezczyzni=float(ludzie/2.0)

#obliczenia do WC 
wc_kobiety=float(kobiety/20.0)
wc_mezczyzni=float(mezczyzni/30.0)

#obliczenia do pisuarów
pisuar=wc_mezczyzni

#obliczenia do umywalek
vanity_kobiety=wc_kobiety
vanity_mezczyzni=wc_mezczyzni

#podaję wyniki KOBIETY
print("PODSUMOWANIE KOBIETY:\n ilość kobiet: "+str(kobiety)+"\n"+" ilość kobiet w zaokrągleniu: "+str(math.ceil(kobiety))+"\n"+" kabiny wc kobiet: "+str(wc_kobiety)+"\n"+" kabiny wc kobiet w zaokrągleniu: " +str(math.ceil(wc_kobiety))+"\n"+" ilość umywalek kobiet: "+str(vanity_kobiety)+"\n"+" ilośc umywalek kobiet w zaokrągleniu: "+str(math.ceil(vanity_kobiety)))

print("\n")

#podaję wyniki MĘŻCZYŹNI
print("PODSUMOWANIE MĘŻCZYŹNI:\n ilość mężczyzn: "+str(mezczyzni)+"\n"+" ilość mężczyzn w zaokrągleniu: "+str(math.ceil(mezczyzni))+"\n"+" kabiny wc mężczyzn: "+str(wc_mezczyzni)+"\n"+" kabiny wc mężczyzn w zaokrągleniu: " +str(math.ceil(wc_mezczyzni))+"\n"+ " ilość pisuarów: "+str(pisuar)+"\n"+" ilość pisuarów w zaokrągleniu: "+str(math.ceil(pisuar))+"\n"+" ilość umywalek mężczyzn: "+str(vanity_mezczyzni)+"\n"+" ilośc umywalek mężczyzn w zaokrągleniu: "+str(math.ceil(vanity_mezczyzni)))

print("\n")

#podaję SUMY KABIN WC
print("KABINY WC RAZEM: "+str((math.ceil(wc_kobiety))+(math.ceil(wc_mezczyzni))))
print(" w tym damskie: "+str(math.ceil(wc_kobiety))+" oraz męskie: "+str(math.ceil(wc_mezczyzni)))

#podaję SUMY UMYWALEK
print("UMYWALKI RAZEM: "+str((math.ceil(vanity_kobiety))+(math.ceil(vanity_mezczyzni))))
print(" w tym damskie: "+str(math.ceil(vanity_kobiety))+" oraz męskie: "+str(math.ceil(vanity_mezczyzni)))

print("PISUARY RAZEM: "+str(math.ceil(pisuar)))


# In[ ]:




