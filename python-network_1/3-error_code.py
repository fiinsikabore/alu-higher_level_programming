#!/usr/bin/python3
"""
Script qui prend une URL en argument, envoie une requête et affiche
le corps de la réponse décodé en UTF-8, tout en gérant les HTTPError.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
