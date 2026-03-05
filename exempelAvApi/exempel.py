# Natte 05.03.2026
# Exempel som visar hur man kan använda shatAPI
# Här tas fraser från en input.txt och görs igenon shatAPI för att sedan sätta svaren i en output.txt




import codecs
import sys
sys.path.append('..')   # får rätt mapp för shatAPI

from shatGpt import shatAPI   # importera shatAPI


# läser input.txt och kör dem igenom shatAPI
out = []

with open("input.txt") as f:
    for i in f:
        out.append(shatAPI(i))


# skriver svaren i output.txt (skapar denna fil om den inte finns från förr)
file = codecs.open("output.txt", "w", "utf-8")
for i in out:
    file.write(i + "\n")
file.close()