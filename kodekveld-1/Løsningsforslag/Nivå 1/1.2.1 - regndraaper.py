"""
Oppgave 1.2.1:
I denne oppgaven skal du printe ut en string basert på om et tall er faktor av 3, 5 eller 7.
Reglene for programmer er som følger:
	- 3 som faktor: print ut "Pling".
	- 5 som faktor: print ut "Plang".
	- 7 som faktor: print ut "Plong".
	- Hverken 3, 5 eller 7 som faktor: skriv ut tallet.
Hvis tallet inneholder mer enn en av faktorene skal programmet skrive ut en samling av stringer
basert på faktorene. Eksempel: 3 og 5 som faktor: print ut "PlingPlang".
"""

def convert(number):
    string = ''
    if number % 3 == 0:
        string += 'Pling'
    if number % 5 == 0:
        string += 'Plang'
    if number % 7 == 0:
        string += 'Plong'
    if string == '':
        string = str(number)
    return string

print(convert(9)) # Tallet 9 er faktor av 3 og vil printe ut 'Pling'
print(convert(15)) # Tallet 15 er faktor av både 3 og 5, dette vil printe ut 'PlingPlang'
print(convert(35)) # Tallet 35 er faktor av både 5 og 7, dette vil printe ut 'PlangPlong'