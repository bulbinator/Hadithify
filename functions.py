import os
import requests
import urllib.parse

from flask import redirect, render_template, request


def get_hadith():
    response = requests.get("https://www.thaqalayn-api.net/api/random")
    hadith = response.json()

    #critera of hadith
    words = len(hadith["englishText"].split())
    if words >= 100 or hadith["book"] == "Rijāl Ibn al-Ghaḍā'irī":
        return get_hadith()
    if "Al-Kāfi" in hadith["book"]:
        hadith["book"] = "Al-Kāfi"
    if "ʿUyūn akhbār al-Riḍā" in hadith["book"]:
        hadith["book"] = "ʿUyūn akhbār al-Riḍā"

    for i in range(10):
        hadith["arabicText"] = hadith["arabicText"].replace(str(i), '')

    #return the correct hadith
    return {
        "arabic": hadith["arabicText"],
        "english": hadith["englishText"],
        "author": hadith["author"],
        "book": hadith["book"],
        "URL": hadith["URL"],
    }