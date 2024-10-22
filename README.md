# myLib
Questa libreria Python, myLib.py, contiene una serie di funzioni utili per varie operazioni matematiche e di manipolazione delle stringhe. Ecco una spiegazione dettagliata di ciascuna funzione:

### Funzioni di Manipolazione delle Stringhe
**rimuovi_punteggiatura(stringa):**
- Rimuove tutti i caratteri di punteggiatura e i caratteri di a capo (\n) da una stringa.
- Utilizza string.punctuation per ottenere tutti i caratteri di punteggiatura predefiniti.

**rimuovi_spazi(stringa):**
- Rimuove tutti gli spazi da una stringa.
- Utilizza il metodo replace per sostituire gli spazi con una stringa vuota.

**rimuovi_caratteri(stringa, \*caratteri_da_rimuovere):**
- Rimuove una serie di caratteri specificati da una stringa.
- Utilizza una comprensione di lista per filtrare i caratteri indesiderati.

### Funzioni di Conversione e Controllo
**convertibile(variabile, tipo):**
- Controlla se una variabile può essere convertita in un tipo specificato.
- Utilizza un blocco try-except per tentare la conversione e catturare eventuali eccezioni ValueError.

**is_bisestile(anno):**
- Controlla se un anno è bisestile.
- Utilizza le regole del calendario gregoriano per determinare se l'anno è divisibile per 4, 100 e 400.

**is_primo(numero):**
- Controlla se un numero è primo.
- Utilizza la funzione divisori per determinare se il numero ha esattamente due divisori (1 e se stesso).

### Funzioni matematiche
**divisori(numero):**
- Restituisce una lista di tutti i divisori di un numero.
- Utilizza una comprensione di lista per trovare i divisori.

**mcd(numero1, numero2):**
- Calcola il massimo comune divisore (MCD) tra due numeri.
- Utilizza l'algoritmo di Euclide.

**mcm(numero1, numero2):**
- Calcola il minimo comune multiplo (MCM) tra due numeri.
- Utilizza la formula (numero1 * numero2) // mcd(numero1, numero2).

**media(lista_numeri):**
- Calcola la media di una lista di numeri.
- Utilizza le funzioni sum e len per calcolare la somma e la lunghezza della lista.
  
**parabola(a, b, c, x):**
- Calcola il valore di y per una parabola data dall'equazione y = ax^2 + bx + c.
- Utilizza i coefficienti a, b, c e il valore di x.

**fattoriale(numero):**
- Calcola il fattoriale di un numero.
- Utilizza una definizione ricorsiva per calcolare il fattoriale.

**decimale_binario(numero):**
- Converte un numero decimale in una stringa rappresentante il suo equivalente binario.
- Il principio è quello di dividere ripetutamente il numero per 2 e concatenare i resti (0 o 1) all'inizio di una stringa finché il quoziente non diventa 0.
- Esempio: decimale_binario(13) restituisce "1101".

**binario_decimale(binario):**
- Converte una stringa binaria in un numero decimale.
- Utilizza la funzione int() con la base 2 per eseguire la conversione direttamente.
- Esempio: binario_decimale("1101") restituisce 13.

**esadecimale_binario(esadecimale):**
- Converte un numero esadecimale in una stringa binaria.
- Prima converte l'esadecimale in decimale utilizzando int() con base 16, poi chiama la funzione decimale_binario() per ottenere la rappresentazione binaria.

**esadecimale_decimale(esadecimale):**
- Converte un numero esadecimale in un numero decimale.
- Utilizza la funzione int() con la base 16 per eseguire la conversione direttamente.

Queste funzioni coprono una vasta gamma di operazioni comuni che possono essere utili in vari contesti di programmazione, dalla manipolazione delle stringhe alle operazioni matematiche di base.

# test.py
Semplicemente un file con delle chiamate alle funzioni per testarne il corretto funzionamento
