from myLib import *

def main():
    # Test rimuovi_punteggiatura
    print(rimuovi_punteggiatura("Ciao, mondo!\n"))  # Output atteso: "Ciao mondo"
    print(rimuovi_punteggiatura("Hello, world!"))  # Output atteso: "Hello world"
    print(rimuovi_punteggiatura("Python. Programming;"))  # Output atteso: "Python Programming"

    # Test rimuovi_spazi
    print(rimuovi_spazi("Ciao mondo"))  # Output atteso: "Ciaomondo"
    print(rimuovi_spazi("Hello world"))  # Output atteso: "Helloworld"
    print(rimuovi_spazi("Python Programming"))  # Output atteso: "PythonProgramming"

    # Test convertibile
    print(convertibile("123", int))  # Output atteso: True
    print(convertibile("abc", int))  # Output atteso: False
    print(convertibile("123.45", float))  # Output atteso: True

    # Test rimuovi_caratteri
    print(rimuovi_caratteri("Ciao mondo", 'a', 'o'))  # Output atteso: "Ci mnd"
    print(rimuovi_caratteri("Hello world", 'l', 'o'))  # Output atteso: "He wrd"
    print(rimuovi_caratteri("Python Programming", 'P', 'g'))  # Output atteso: "ython Pro rammin"

    # Test is_bisestile
    print(is_bisestile(2020))  # Output atteso: True
    print(is_bisestile(1900))  # Output atteso: False
    print(is_bisestile(2000))  # Output atteso: True

    # Test divisori
    print(divisori(28))  # Output atteso: [1, 2, 4, 7, 14, 28]
    print(divisori(15))  # Output atteso: [1, 3, 5, 15]
    print(divisori(13))  # Output atteso: [1, 13]

    # Test is_primo
    print(is_primo(29))  # Output atteso: True
    print(is_primo(28))  # Output atteso: False
    print(is_primo(13))  # Output atteso: True

    # Test mcd
    print(mcd(48, 18))  # Output atteso: 6
    print(mcd(20, 8))  # Output atteso: 4
    print(mcd(100, 25))  # Output atteso: 25

    # Test mcm
    print(mcm(4, 5))  # Output atteso: 20
    print(mcm(6, 8))  # Output atteso: 24
    print(mcm(7, 3))  # Output atteso: 21

    # Test media
    print(media([1, 2, 3, 4]))  # Output atteso: 2.5
    print(media([10, 20, 30]))  # Output atteso: 20.0
    print(media([5, 5, 5, 5]))  # Output atteso: 5.0

    # Test parabola
    print(parabola(1, -3, 2, 2))  # Output atteso: 2
    print(parabola(1, 0, -4, 1))  # Output atteso: -3
    print(parabola(2, -4, 2, 2))  # Output atteso: 2

    # Test fattoriale
    print(fattoriale(5))  # Output atteso: 120
    print(fattoriale(0))  # Output atteso: 1
    print(fattoriale(3))  # Output atteso: 6

    # Test decimale_binario
    print(decimale_binario(10))  # Output atteso: "1010"
    print(decimale_binario(0))  # Output atteso: "0"
    print(decimale_binario(255))  # Output atteso: "11111111"

    # Test binario_decimale
    print(binario_decimale("1010"))  # Output atteso: 10
    print(binario_decimale("0"))  # Output atteso: 0
    print(binario_decimale("11111111"))  # Output atteso: 255

    # Test esadecimale_binario
    print(esadecimale_binario("A"))  # Output atteso: "1010"
    print(esadecimale_binario("0"))  # Output atteso: "0"
    print(esadecimale_binario("FF"))  # Output atteso: "11111111"

    # Test esadecimale_decimale
    print(esadecimale_decimale("A"))  # Output atteso: 10
    print(esadecimale_decimale("0"))  # Output atteso: 0
    print(esadecimale_decimale("FF"))  # Output atteso: 255

    # Test FrazBin2FrazDecimale
    print(FrazBin2FrazDecimale("101"))  # Output atteso: 0.625
    print(FrazBin2FrazDecimale("11"))  # Output atteso: 0.75
    print(FrazBin2FrazDecimale("01"))  # Output atteso: 0.5

    # Test ex2cp2
    print(ex2cp2("0A"))  # Output atteso: "00001010"
    print(ex2cp2("F5"))  # Output atteso: "11110101"
    print(ex2cp2("7F"))  # Output atteso: "01111111"

if __name__ == "__main__":
    main()
