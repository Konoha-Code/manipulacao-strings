from models.konoha_phrase import KonohaPhrase


def main():
    kp = KonohaPhrase(input("Informe uma frase para ser analisada: "))

    print(f"Letras maiúsculas: {kp.uppercase_count()}") 
    print(f"Letras minúsculas: {kp.lowercase_count()}") 
    print(f"Números: {kp.numeric_count()}") 
    print(f"Espaços: {kp.space_count()}") 
    print(f"Outros: {kp.other_count()}") 
    print(f"Contagem Konoha: {kp.konoha_count()}") 
    print(f"Frase tratada: {kp.treat_phrase()}") 

if __name__ == "__main__":
    main()