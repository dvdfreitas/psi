from os.path import exists

file_exists = exists("projetos/fibonnacci.txt")

if (file_exists):
    # Ver os últimos números da sequência
    print("Existe")
else:
    # Criar o ficheiro e começar a gerar a sequência
    print("Não existe")