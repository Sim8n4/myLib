from myLib import *

def main():
    # Test rimuovi_punteggiatura
    print(rimuovi_punteggiatura("Ciao, mondo!\n"))  # Output atteso: "Ciao mondo"

    # Test rimuovi_spazi
    print(rimuovi_spazi("Ciao mondo"))  # Output atteso: "Ciaomondo"

    # Test convertibile
    print(convertibile("123", int))  # Output atteso: True
    print(convertibile("abc", int))  # Output atteso: False

    # Test rimuovi_caratteri
    print(rimuovi_caratteri("Ciao mondo", 'a', 'o'))  # Output atteso: "Ci mnd"

    # Test is_bisestile
    print(is_bisestile(2020))  # Output atteso: True
    print(is_bisestile(1900))  # Output atteso: False

    # Test divisori
    print(divisori(28))  # Output atteso: [1, 2, 4, 7, 14, 28]

    # Test is_primo
    print(is_primo(29))  # Output atteso: True
    print(is_primo(28))  # Output atteso: False

    # Test mcd
    print(mcd(48, 18))  # Output atteso: 6

    # Test mcm
    print(mcm(4, 5))  # Output atteso: 20

    # Test media
    print(media([1, 2, 3, 4]))  # Output atteso: 2.5

    # Test parabola
    print(parabola(1, -3, 2, 1))  # Output atteso: 0

    # Test fattoriale
    print(fattoriale(5))  # Output atteso: 120

    # Test decimale_binario
    print(decimale_binario(10))  # Output atteso: "1010"

    # Test binario_decimale
    print(binario_decimale("1010"))  # Output atteso: 10

    # Test esadecimale_binario
    print(esadecimale_binario("A"))  # Output atteso: "1010"

    # Test esadecimale_decimale
    print(esadecimale_decimale("A"))  # Output atteso: 10

    # Test FrazBin2FrazDecimale
    print(FrazBin2FrazDecimale("101"))  # Output atteso: 0.625

    # Test ex2cp2
    print(ex2cp2("0A"))  # Output atteso: "1A"

if __name__ == "__main__":
    main()
