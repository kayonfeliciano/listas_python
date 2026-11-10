# Vamos criar um jogo de pedra, papel ou tesoura
print ("====== BEM VINDO AO JO-KEN-PO ====== ")

jogador1 = input("Olá jogador1, qual o seu nome?")
escolha1 = int(input("Jogador,você quer,\n1- pedra, \n2 - papel, \n3 - tesoura?"))

jogador2 = input("Olá jogador2, qual o seu nome?")
escolha2 = int(input("jogador, você quer,\n1 - pedra, \n2 - papel, \n3 - tesoura?"))

if escolha1 == 1 and escolha2 == 3:
    print(f"{jogador1} ganhou")
elif escolha1 == 2 and escolha2 == 3:
    print(f"{jogador2} ganhou")
elif escolha1 == 3 and escolha2 == 1:
    print(f"{jogador2} ganhou")
else:
    print("Sem vencedor, foi empate")