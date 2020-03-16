"""
Oppgave 1.2.2:
For et gitt ord skal du i denne oppgaven gi det en score.

            Bokstaver:                  Verdi:
    A, E, I, O, U, L, N, R, S, T          1
               D, G                       2
            B, C, M, P                    3
          F, H, V, W, Y                   4
                K                         5
               J, K                       8
               Q, Z                       10

Eksempel: For ordet Python får vi følgende regnskap:
3 poeng for 'P', 4 poeng for 'Y', 1 poeng for 'T', 4 for 'H', 1 for 'O' og 1 for 'N'.
Til sammen blir dette: 14    
"""

def score(word):
    return sum(get_value(letter) for letter in word.upper())

def get_value(letter):
    if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
        return 1
    elif letter in ['D', 'G']:
        return 2
    elif letter in ['B', 'C', 'M', 'P']:
        return 3
    elif letter in ['F', 'H', 'V', 'W', 'Y']:
        return 4
    elif letter in ['K']:
        return 5
    elif letter in ['J', 'X']:
        return 8
    else:
        return 10

print(score("python")) # Gir tallet 14


