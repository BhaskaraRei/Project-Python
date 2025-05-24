# -*- coding: utf-8 -*- criado do Jogo BHASKARA DEVELOPER
import random
saldoConta = 0

textoJogoTrigre = (
        "Para pontuar, você deve Fazer uma Tricar de Animais \n"
        "Exemplo:🦁 🦁 🦁 , uma dupla, Exemplo: 🐯 🐯 🐼\n"
            "⚠️  ATENCÃO cada Aposta custa R$ 20 ATENÇÃO ⚠️\n"
)
textoJogoRoleta = (
             "Para pontuar, você deve acerta o nuemero que vai sair \n"
      "Exemplo:Seu numero 1️⃣ 5️⃣ , numero Sorteado 1️⃣ 5️⃣ , você Ganhou uma rodada\n"
 "Valores da Roleta : 1️⃣ 0️⃣ ,1️⃣ 5️⃣ ,2️⃣ 5️⃣ ,3️⃣ 0️⃣ ,4️⃣ 0️⃣ , 9️⃣  ,  5️⃣  ,5️⃣ 0️⃣ , 3️⃣ ,6️⃣ 0️⃣  para escolher\n"
                "⚠️  ATENCÃO Aposta minima R$ 10 ATENÇÃO ⚠️\n"
)
def RoletaSorte(saldoContar):
   arrayNovofigurasRl = []
   pesosFigurasRl = []
   resul = 0
   arrayNumeros = [
    {"emoji":"1️⃣  0️⃣", "peso": 10},
    {"emoji":"1️⃣  5️⃣", "peso": 15},
    {"emoji":"2️⃣  5️⃣", "peso": 25},
    {"emoji":"3️⃣  0️⃣","peso": 30},
    {"emoji":"4️⃣  0️⃣","peso": 40},
    {"emoji":"9️⃣","peso": 9},
    {"emoji":"5️⃣","peso": 5},
    {"emoji":"5️⃣  0️⃣","peso": 50},
    {"emoji":"3️⃣","peso": 3},
    {"emoji":"6️⃣  0️⃣","peso": 10}
 ]
   print('🎰 Bem-vindo ao Jogo Roleta da Sorte 🎰')
   print('Como o jogo funciona ?\n')
   print(textoJogoRoleta)

   for emoji in arrayNumeros:
        arrayNovofigurasRl.extend([emoji["emoji"]] * emoji["peso"])
        pesosFigurasRl.extend([emoji["peso"]] * emoji["peso"])

   while True:
    if saldoContar >= 10:
       print('Saldo R$ 💵💰: ',saldoContar)
       comando = input('Digite "Apostar" para começa cada rodada ou "Sair": ')
       if comando.lower() == 'sair':
            print('Obrigado por Jogar, até a próxima 😁🤭')
            return saldoContar
       elif comando.lower() == 'apostar':
          valorUsuario = int(input("Digite o seu numero da Sorte (Sem casas Decimais): "))
          aposta = float(input("Digite o Valor da Sua Aposta 😁 R$: "))
          indece = random.randint(0,len(arrayNovofigurasRl) - 1)
          peso = pesosFigurasRl[indece]
          emoji = arrayNovofigurasRl[indece]
          print('-' * 10)
          print(f'|{emoji}  |')
          print('-' * 10)
          if valorUsuario == peso:
             resul = aposta * peso
             saldoContar = (saldoContar - aposta) + resul
             return saldoContar
          else:
            saldoContar = saldoContar - aposta
       else:
          print('Opção não reconhecida 🚫')

    else:
      print(" ⚠️ Descupe você não possui saldo sulficiente para jogar, DEPOSITE no Menu inicial ⚠️")
      return saldoContar
      
def fortunaTigre(saldoContar):

    arrayNovofigurasTg = []
    pesosFigurasTg = []
    resul = 0
    
    arrayFiguras = [
    {"emoji":"🐮", "peso": 1},
    {"emoji":"🐱", "peso": 2},
    {"emoji":"🐼", "peso": 3},
    {"emoji":"🐷","peso": 4},
    {"emoji":"🐵","peso": 5},
    {"emoji":"🐶","peso": 6},
    {"emoji":"🦁","peso": 7},
    {"emoji":"🐯","peso": 10}
    
 ]
    print('🎰 Bem-vindo ao Jogo Fortuna Tigre 🎰')
    print('Como o jogo funciona ?\n')
    print(textoJogoTrigre)

    for emoji in arrayFiguras:
        arrayNovofigurasTg.extend([emoji["emoji"]] * emoji["peso"])
        pesosFigurasTg.extend([emoji["peso"]] * emoji["peso"])
    while True:
        if saldoContar >= 20:
           print('Saldo R$ 💵💰: ',saldoContar)
           comando = input('Digite "Apostar" para começa cada rodada ou "Sair": ')
           if comando.lower() == 'sair':
            print('Obrigado por Jogar, até a próxima 😁🤭')
            return saldoContar
           elif comando.lower() == 'apostar':
            saldoContar = saldoContar - 20
            indece1 = random.randint(0,len(arrayNovofigurasTg) - 1)
            indece2 = random.randint(0,len(arrayNovofigurasTg) - 1)
            indece3 = random.randint(0,len(arrayNovofigurasTg) - 1)

            peso1 = pesosFigurasTg[indece1]
            peso2 = pesosFigurasTg[indece2]
            peso3 = pesosFigurasTg[indece3]

            emoji1 = arrayNovofigurasTg[indece1]
            emoji2 = arrayNovofigurasTg[indece2]
            emoji3 = arrayNovofigurasTg[indece3]

            print('-' * 10)
            print(f'|{emoji1}|{emoji2}|{emoji3}|')
            print('-' * 10)
            if emoji1 == emoji2 == emoji3:
              resul  = peso1 * peso2 * peso3 
              print(f"Parabens, você acertou uma trica de animais, você ganhou: {resul}")
              saldoContar += resul
            elif emoji1 == emoji2:
              resul = peso1 * peso2
              print(f"Parabens, você acertou uma dupla de animais, você ganhou: {resul}")
              saldoContar += resul
            elif emoji2 == emoji3:
              resul = peso2 * peso3
              print(f"Parabens, você acertou uma dupla de animais, você ganhou: {resul}")
              saldoContar += resul
            elif emoji3 == emoji1:
              print(f"Parabens, você acertou uma dupla de animais, você ganhou: {resul}")
              resul = peso3 * peso1
              saldoContar += resul
           else:
            print('Opção não reconhecida 🚫')
        else:
           print(" ⚠️ Descupe você não possui saldo sulficiente para jogar, DEPOSITE no Menu inicial ⚠️")
           return saldoContar
        
        
def jogosXpythonBet(saldoContar):
    while True:
        print("Seu saldo: ",saldoContar)
        print('☘️  - Jogos Disponiveis - ☘️\n')
        print('☘️ 🐯 Fortuna Tigre ☘️ 🐯')
        print('💲 🎰 Roleta da Sorte 🎰 💲')
        print('❌ Voltar ao Inicio ❌\n')
        print('☘️ ','-' * 21,'☘️')
        opcJogo = input('Digite o Jogo Desejado: ')
        if opcJogo.lower() == 'fortuna tigre':
            retorno = fortunaTigre(saldoContar)
            return retorno
        elif opcJogo.lower() == 'roleta da sorte':
            retorno = RoletaSorte(saldoContar)
            return retorno
        elif opcJogo.lower() == 'voltar ao inicio':
            break
        else:
            print('Opção não reconhecida 🚫')

def DepositarDinheiro(saldoContar):
    print('Saldo R$ 💵💰: ',saldoContar)
    NovoDeposito = int(input('Digite quanto você quer DEPOSITAR em R$: '))
    saldoContar += NovoDeposito
    print('Valor Depositado com Sucesso 🤭')
    return saldoContar

def SacarDinheiro(saldoContar):
    while True:
       print(f'Saldo R$ 💵💰: R${saldoContar}')
       SacarDinheiro = float(input('Digite quanto você que Sacar em R$: '))
       print('⚠️ Valor minimo em conta R$ 10')
       if saldoContar == 0:
          print(" ⚠️ Descupe você não possui saldo sulficiente para jogar, DEPOSITE no Menu inicial ⚠️")
          break
       elif saldoContar > SacarDinheiro:
          saldoContar -= SacarDinheiro
          print(f'Valor Sacado com Sucesso, Valor Sacado R$: {SacarDinheiro}')
          return saldoContar
       elif saldoContar - SacarDinheiro >= 10:
           saldoContar  -= SacarDinheiro
           print(f'Valor Sacado com Sucesso, Valor Saldo R$: {saldoContar}')
           return saldoContar
       else:
           return False

while True:
    print('🎲 +-------------------+ 🎲\n')
    print(f'Saldo R$ 💰: R${saldoConta}')
    print('Bem vindo, a Xpython Bet\n')
    print('💰 Depositar 💰')
    print('💵 Sacar 💵')
    print('☘️  Jogos ☘️')
    print('❌ Sair ❌\n')
    print('⚠️  Por favor, escreva à palavra da opção desejada Exemplo:"depositar"')
    print('ou "Fortuna tigre" respeitado ate os espaços ⚠️\n')
    print('🎲 +-------------------+ 🎲')
    opc = input('Digite a opção que você deseja: ')
    if opc.lower() == 'depositar':
        retorno = DepositarDinheiro(saldoConta)
        saldoConta += retorno
    elif opc.lower() == 'sacar':
        retorno = SacarDinheiro(saldoConta)
        if retorno:
          saldoConta = retorno
        else:
            print(f'Valor Minímo Atigindo é R$10, Saldo Atual: {saldoConta}😨😥')
    elif opc.lower() == 'jogos':
        retorno = jogosXpythonBet(saldoConta)
        saldoConta = retorno
    elif opc.lower() == 'sair':
        break
    else:
        print(' Ops, opção não Reconheecida ! 🚫')