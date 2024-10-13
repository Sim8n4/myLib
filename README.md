# myLib
Questa libreria Python, myLib.py, contiene una serie di funzioni utili per varie operazioni matematiche e di manipolazione delle stringhe. Ecco una spiegazione dettagliata di ciascuna funzione:

### Funzioni di Manipolazione delle Stringhe

rimuovi_punteggiatura(stringa):
  Rimuove tutti i caratteri di punteggiatura e i caratteri di a capo (\n) da una stringa.
  Utilizza string.punctuation per ottenere tutti i caratteri di punteggiatura predefiniti.

rimuovi_spazi(stringa):
  Rimuove tutti gli spazi da una stringa.
  Utilizza il metodo replace per sostituire gli spazi con una stringa vuota.

rimuovi_caratteri(stringa, *caratteri_da_rimuovere):
  Rimuove una serie di caratteri specificati da una stringa.
  Utilizza una comprensione di lista per filtrare i caratteri indesiderati.

### Funzioni di Conversione e Controllo
convertibile(variabile, tipo):
Controlla se una variabile può essere convertita in un tipo specificato.
Utilizza un blocco try-except per tentare la conversione e catturare eventuali eccezioni ValueError.
Funzioni Matematiche

is_bisestile(anno):
  Controlla se un anno è bisestile.
  Utilizza le regole del calendario gregoriano per determinare se l'anno è divisibile per 4, 100 e 400.

is_primo(numero):
  Controlla se un numero è primo.
  Utilizza la funzione divisori per determinare se il numero ha esattamente due divisori (1 e se stesso).

### Funzioni matematiche
divisori(numero):
  Restituisce una lista di tutti i divisori di un numero.
  Utilizza una comprensione di lista per trovare i divisori.

mcd(numero1, numero2):
  Calcola il massimo comune divisore (MCD) tra due numeri.
  Utilizza l'algoritmo di Euclide.

mcm(numero1, numero2):
  Calcola il minimo comune multiplo (MCM) tra due numeri.
  Utilizza la formula (numero1 * numero2) // mcd(numero1, numero2).

media(lista_numeri):
  Calcola la media di una lista di numeri.
  Utilizza le funzioni sum e len per calcolare la somma e la lunghezza della lista.
  
parabola(a, b, c, x):
  Calcola il valore di y per una parabola data dall'equazione y = ax^2 + bx + c.
  Utilizza i coefficienti a, b, c e il valore di x.

fattoriale(numero):
  Calcola il fattoriale di un numero.
  Utilizza una definizione ricorsiva per calcolare il fattoriale.

Queste funzioni coprono una vasta gamma di operazioni comuni che possono essere utili in vari contesti di programmazione, dalla manipolazione delle stringhe alle operazioni matematiche di base.

# test.py
Semplicemente un file con delle chiamate alle funzioni per testarne il corretto funzionamento
