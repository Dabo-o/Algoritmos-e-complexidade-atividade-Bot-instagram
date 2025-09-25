import os
import time

while True:
    os.system('cls||clear')
    print("==============================")
    print("MENU")
    print("==============================")
    print("1 - Rodar Scraper do G1")
    print("2 - Rodar Bot do Instagram")
    print("0 - Sair")
    print("==============================")
    
    op = input("Digite a opcao: ")

    if op == '1':
        print("Rodando g1_scraper.py...")
        os.system('python g1_scraper.py')
        print("Finalizado.")
        time.sleep(4)
    elif op == '2':
        print("Rodando bot_login.py...")
        os.system('python bot_login.py')
        print("Finalizado.")
        time.sleep(4)
    elif op == '0':
        break
    else:
        print("Opcao invalida.")
        time.sleep(2)