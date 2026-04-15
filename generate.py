import re, os, json
from pathlib import Path
from collections import defaultdict

QEEPL_REF = "https://qeepl.com/ru/map?discount=SBUHJKBO"
RADICAL_PARAMS = "?erid=2VtzqvWLUd3&track_id=c29a6ef0036745e991d79dad4-549016&utm_term=travelpayouts"
SITE_DOMAIN = "bag-catalog.vercel.app"  # <-- замени на свой домен

def radical_city_url(slug):
    return f"https://radicalstorage.com/ru/kamery-hranenija/{slug}/{RADICAL_PARAMS}"

def radical_poi_url(city, district="", poi=""):
    if poi:
        return f"https://radicalstorage.com/ru/kamery-hranenija/{city}/{district}/{poi}/{RADICAL_PARAMS}"
    elif district:
        return f"https://radicalstorage.com/ru/kamery-hranenija/{city}/{district}/{RADICAL_PARAMS}"
    return radical_city_url(city)

# Запускай: python generate.py
# Читает SIa.txt, генерирует папки с index.html для каждого города
# Деплой: vercel --prod из папки luggage-site/
