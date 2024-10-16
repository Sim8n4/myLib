import string
import math

# Funzione per rimuovere la punteggiatura da una stringa e il carattere di a capo
def rimuovi_punteggiatura(stringa):
    punteggiatura = string.punctuation + '\n'  # Stringa contenente tutti i caratteri di punteggiatura e il carattere di a capo
    stringa_senza_punteggiatura = ''.join(carattere for carattere in stringa if carattere not in punteggiatura)  # Rimuove i caratteri di punteggiatura dalla stringa
    return stringa_senza_punteggiatura

# Funzione per rimuovere gli spazi da una stringa
def rimuovi_spazi(stringa):
    stringa_senza_spazi = stringa.replace(' ', '')  # Rimuove gli spazi dalla stringa
    return stringa_senza_spazi

# Funzione per controllare se una variabile è convertibile in un certo tipo
def convertibile(variabile, tipo):
    try:
        tipo(variabile)  # Prova a convertire la variabile nel tipo specificato
        return True  # Se la conversione ha successo, restituisce True
    except ValueError:
        return False  # Se la conversione fallisce, restituisce False

# Funzione per rimuovere più caratteri da una stringa in un solo colpo
def rimuovi_caratteri(stringa, *caratteri_da_rimuovere):
    stringa_senza_caratteri = ''.join(carattere for carattere in stringa if carattere not in caratteri_da_rimuovere)  # Rimuove i caratteri specificati dalla stringa
    return stringa_senza_caratteri

# Funzione per controllare se un anno è bisestile
def is_bisestile(anno):
    if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                return True  # Se l'anno è divisibile per 400, è bisestile
            else:
                return False  # Se l'anno è divisibile per 100 ma non per 400, non è bisestile
        else:
            return True  # Se l'anno è divisibile per 4 ma non per 100, è bisestile
    else:
        return False  # Se l'anno non è divisibile per 4, non è bisestile

# Funzione per stampare tutti i divisori di un numero
def divisori(numero):
    divisori = [divisore for divisore in range(1, numero + 1) if numero % divisore == 0]  # Lista dei divisori del numero
    return divisori

# Funzione per controllare se un numero è primo
def is_primo(numero):
    divisori_numero = divisori(numero)
    if len(divisori_numero) == 2:
        return True  # Se il numero ha esattamente due divisori (1 e se stesso), è primo
    else:
        return False  # Altrimenti, non è primo

# Funzione che calcola il massimo comun divisore tra due numeri
def mcd(numero1, numero2):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2  # Calcola il resto della divisione tra numero1 e numero2 e assegna il valore a numero2
    return numero1  # Restituisce il massimo comun divisore

# Funzione che calcola il minimo comune multiplo tra due numeri
def mcm(numero1, numero2):
    mcm = (numero1 * numero2) // mcd(numero1, numero2)  # Calcola il minimo comune multiplo utilizzando la formula (numero1 * numero2) / mcd(numero1, numero2)
    return mcm

# Funzione che calcola la media di una lista di numeri (cioè un array di numeri tipo n = [1, 2, 3, 4])
def media(lista_numeri):
    media = sum(lista_numeri) / len(lista_numeri)  # Calcola la somma dei numeri nella lista e la divide per il numero di elementi nella lista
    return media

# Funzione che calcola l'equazione di una parabola y = ax^2 + bx + c
def parabola(a, b, c, x):
    y = a * (x ** 2) + b * x + c  # Calcola il valore di y utilizzando i coefficienti a, b, c e il valore di x
    return y

# Funzione per calcolare il fattoriale di un numero
def fattoriale(numero):
    if numero == 0:
        return 1  # Il fattoriale di 0 è 1
    else:
        return numero * fattoriale(numero - 1)  # Calcola il fattoriale ricorsivamente
