# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Cs2SEONo8qHs0k7oGt6pS9EFOEvhrI_
"""

def poytaxt_tashxisi(davlat):
    if davlat == "O'zbekiston":
        return "Toshkent"
    elif davlat == "AQSh":
        return "Vashington"
    elif davlat == "Rossiya":
        return "Moskva"
    elif davlat == "Fransiya":
        return "Parij"
    elif davlat == "Xitoy":
        return "Pekin"
    elif davlat == "Hindiston":
        return "Nyu-Delhi"
    elif davlat == "Braziliya":
        return "Braziliya shahri"
    elif davlat == "Germaniya":
        return "Berlin"
    elif davlat == "Yaponiya":
        return "Tokio"
    elif davlat == "Buyuk Britaniya":
        return "London"
    else:
        return "Bu davlatning poytaxti ma'lum emas"

davlat = input("Davlat nomini kiriting: ")
poytaxt = poytaxt_tashxisi(davlat)
print(f"{davlat}ning poytaxti: {poytaxt}")